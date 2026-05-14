#!/usr/bin/env python3
"""Export Markdown research reports to PDF with robust scientific math handling."""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from pathlib import Path


GREEK = {
    "alpha": r"\alpha",
    "beta": r"\beta",
    "gamma": r"\gamma",
    "delta": r"\delta",
    "epsilon": r"\epsilon",
    "eta": r"\eta",
    "theta": r"\theta",
    "lambda": r"\lambda",
    "mu": r"\mu",
    "nu": r"\nu",
    "xi": r"\xi",
    "pi": r"\pi",
    "rho": r"\rho",
    "sigma": r"\sigma",
    "tau": r"\tau",
    "phi": r"\phi",
    "chi": r"\chi",
    "psi": r"\psi",
    "omega": r"\omega",
    "Gamma": r"\Gamma",
    "Delta": r"\Delta",
    "Theta": r"\Theta",
    "Lambda": r"\Lambda",
    "Xi": r"\Xi",
    "Pi": r"\Pi",
    "Sigma": r"\Sigma",
    "Phi": r"\Phi",
    "Psi": r"\Psi",
    "Omega": r"\Omega",
}

ACCENTS = ("dot", "ddot", "bar", "hat", "vec", "tilde")
UNIT_NAMES = (
    "kWh",
    "MWh",
    "MeV",
    "keV",
    "eV",
    "MW",
    "MW_abs",
    "kJ",
    "Gy",
    "Pa",
    "kg",
    "umol",
    "μmol",
    "mol",
    "molecule",
    "J",
    "m",
    "s",
    "V",
    "F",
    "C",
    "K",
    "yr",
)
UNIT_TEX = {
    "MW_abs": r"\mathrm{MW}_{\mathrm{abs}}",
    "umol": r"\mu\mathrm{mol}",
    "μmol": r"\mu\mathrm{mol}",
}
UNIT_RE = r"(?:MW_abs|molecule|kWh|MWh|MeV|keV|eV|MW|kJ|Gy|Pa|kg|umol|μmol|mol|J|m|s|V|F|C|K|yr)"
POWER_RE = r"(?:\^\{[-+]?\d+\}|\^-?\d+)?"
UNIT_TOKEN_RE = rf"{UNIT_RE}{POWER_RE}"
UNIT_EXPR_RE = re.compile(
    rf"(?<![A-Za-z0-9_\\])"
    rf"(?:(?:\d+(?:\.\d+)?\s+)?{UNIT_TOKEN_RE}(?:\s+{UNIT_TOKEN_RE})+|{UNIT_RE}\^\{{[-+]?\d+\}})"
    rf"(?![A-Za-z0-9_])"
)
KNOWN_UNIT_TOKEN_RE = re.compile(
    r"(?<![A-Za-z\\{])"
    r"(MW_abs|molecule|kWh|MWh|MeV|keV|eV|MW|kJ|Gy|Pa|kg|umol|μmol|mol|yr)"
    r"(?:\^\{([-+]?\d+)\})?"
    r"(?![A-Za-z])"
)

CODE_SPAN_RE = re.compile(r"(`+)([^`]*?)\1")
INLINE_MATH_RE = re.compile(r"(\$[^$\n]+\$|\\\([^)]*\\\))")
MERMAID_FENCE_RE = re.compile(
    r"(?ms)^(?P<indent>[ \t]*)(?P<fence>`{3,}|~{3,})[ \t]*mermaid[^\n]*\n(?P<body>.*?)(?P=indent)(?P=fence)[ \t]*$"
)
INLINE_FORMULA_TOKEN_RE = re.compile(
    r"(?<![A-Za-z0-9_\\$/.-])"
    r"("
    r"(?:(?:dot|ddot|bar|hat|vec|tilde)\{[A-Za-z][A-Za-z0-9]*\}(?:_\{[^{}\n]+\}|_[A-Za-z0-9]+)?(?:\^\{[^{}\n]+\}|\^[A-Za-z0-9+-]+)?)"
    r"|(?:(?:alpha|beta|gamma|delta|epsilon|eta|theta|lambda|mu|nu|xi|pi|rho|sigma|tau|phi|chi|psi|omega|Gamma|Delta|Theta|Lambda|Xi|Pi|Sigma|Phi|Psi|Omega)(?:_\{[^{}\n]+\}|_[A-Za-z0-9]+)?(?:\^\{[^{}\n]+\}|\^[A-Za-z0-9+-]+)?)"
    r"|(?:[A-Z](?:_\{[^{}\n]+\}|_[A-Za-z0-9]+)(?:\^\{[^{}\n]+\}|\^[A-Za-z0-9+-]+)?)"
    r"|(?:[A-Za-z](?:\^\{[^{}\n]+\}|\^[A-Za-z0-9+-]+)(?:_\{[^{}\n]+\}|_[A-Za-z0-9]+)?)"
    r"|(?:[A-Z][a-z]?_\d+[A-Za-z0-9]*(?:\^\{[^{}\n]+\})?)"
    r"|(?:e_\{aq\}\^\{-\}|e_aq\^\{-\})"
    r")"
    r"(?![A-Za-z0-9_\\$/.-])"
)

DEFAULT_CSS = """@page {
  size: A4;
  margin: 18mm 16mm;
}

body {
  color: #172026;
  font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", "Hiragino Sans GB",
    "Noto Sans CJK SC", "Microsoft YaHei", Arial, sans-serif;
  font-size: 10.5pt;
  line-height: 1.65;
  max-width: 920px;
  margin: 0 auto;
}

h1, h2, h3, h4 {
  color: #0f2f3d;
  font-weight: 700;
  line-height: 1.25;
  page-break-after: avoid;
}

h1 {
  font-size: 24pt;
  margin: 0 0 16pt;
  border-bottom: 2px solid #d7e4ea;
  padding-bottom: 10pt;
}

h2 { font-size: 17pt; margin: 24pt 0 9pt; }
h3 { font-size: 13pt; margin: 18pt 0 7pt; }
h4 { font-size: 11pt; margin: 14pt 0 6pt; }
p { margin: 0 0 8pt; }
a { color: #0b63a3; text-decoration: none; }

table {
  border-collapse: collapse;
  width: 100%;
  margin: 10pt 0 14pt;
  page-break-inside: auto;
  font-size: 9.2pt;
}

thead { display: table-header-group; }
tr { page-break-inside: avoid; page-break-after: auto; }
th, td {
  border: 1px solid #b8c7cf;
  padding: 5pt 6pt;
  vertical-align: top;
  overflow-wrap: anywhere;
}
th {
  background: #e9f1f4;
  color: #102b36;
  font-weight: 700;
}

blockquote {
  margin: 12pt 0;
  padding: 8pt 12pt;
  border-left: 4px solid #8ab4c6;
  background: #f4f8fa;
}

code {
  font-family: "SFMono-Regular", Menlo, Consolas, "Liberation Mono", monospace;
  font-size: 0.92em;
  background: #f3f6f8;
  border-radius: 3px;
  padding: 0.08em 0.25em;
}

pre {
  background: #f3f6f8;
  border: 1px solid #d7e0e5;
  border-radius: 6px;
  padding: 9pt;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
  page-break-inside: avoid;
}

pre code { background: transparent; padding: 0; }
ul, ol { padding-left: 20pt; margin: 0 0 9pt; }
li { margin: 2pt 0; }
img { max-width: 100%; height: auto; }

.geomine-mermaid-figure {
  margin: 13pt 0 16pt;
  page-break-inside: avoid;
  text-align: center;
}

.geomine-mermaid-figure svg {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 0 auto;
}

.geomine-mermaid-caption {
  margin-top: 5pt;
  color: #52616a;
  font-size: 8.8pt;
  text-align: center;
}

math[display="block"] {
  display: block math;
  margin: 10pt 0 12pt;
  overflow-x: auto;
  overflow-y: hidden;
  font-size: 10.5pt;
}

math[display="inline"] {
  display: inline math;
  margin: 0 0.04em;
  overflow: visible;
  font-size: 1em;
  vertical-align: -0.12em;
}

span.math { white-space: nowrap; }

@media print {
  body { max-width: none; }
}
"""

MANDATORY_MATH_LAYOUT_CSS = """
/* GeoMine mandatory MathML layout guard.
   Keep inline formulas in the text flow, and only break display formulas. */
math[display="block"] {
  display: block math;
  margin: 10pt 0 12pt;
  overflow-x: auto;
  overflow-y: hidden;
  font-size: 10.5pt;
}

math[display="inline"] {
  display: inline math;
  margin: 0 0.04em;
  overflow: visible;
  font-size: 1em;
  vertical-align: -0.12em;
}

span.math { white-space: nowrap; }
"""

MERMAID_LAYOUT_CSS = """
/* GeoMine Mermaid SVG print guard. */
.geomine-mermaid-figure {
  margin: 13pt 0 16pt;
  page-break-inside: avoid;
  text-align: center;
}

.geomine-mermaid-figure svg {
  display: block;
  max-width: 100%;
  height: auto;
  margin: 0 auto;
}

.geomine-mermaid-caption {
  margin-top: 5pt;
  color: #52616a;
  font-size: 8.8pt;
  text-align: center;
}
"""


class MermaidStats:
    def __init__(
        self,
        diagrams: int = 0,
        cli_rendered: int = 0,
        fallback_rendered: int = 0,
        skipped: int = 0,
        failed: int = 0,
    ) -> None:
        self.diagrams = diagrams
        self.cli_rendered = cli_rendered
        self.fallback_rendered = fallback_rendered
        self.skipped = skipped
        self.failed = failed


def normalize_markdown_math_text(text: str) -> str:
    """Normalize nonstandard scientific Markdown formulas to Pandoc math syntax."""
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    in_fence = False
    fence_marker = ""
    fence_is_math = False
    in_display_math = False
    display_math_end = ""

    for line in lines:
        fence = re.match(r"^(\s*)(`{3,}|~{3,})(.*?)(\r?\n)?$", line)
        if fence:
            marker = fence.group(2)
            info = fence.group(3).strip().lower()
            newline = fence.group(4) or ""
            if not in_fence:
                in_fence = True
                fence_marker = marker
                fence_is_math = info in {"math", "{.math}", ".math"} or info.startswith("math ")
                if fence_is_math:
                    out.append(f"{fence.group(1)}$${newline}")
                else:
                    out.append(line)
                continue
            if marker.startswith(fence_marker[0]) and len(marker) >= len(fence_marker):
                in_fence = False
                if fence_is_math:
                    out.append(f"{fence.group(1)}$${newline}")
                else:
                    out.append(line)
                fence_is_math = False
                fence_marker = ""
                continue

        if in_fence:
            if fence_is_math:
                out.append(_normalize_display_math_line(line))
            else:
                out.append(line)
            continue

        stripped = line.strip()
        if in_display_math:
            out.append(line)
            if stripped == display_math_end:
                in_display_math = False
                display_math_end = ""
            continue

        if stripped in {"$$", r"\["}:
            out.append(line)
            in_display_math = True
            display_math_end = "$$" if stripped == "$$" else r"\]"
            continue

        out.append(_normalize_inline_formula_segments(line))

    return "".join(out)


def prepare_markdown_for_pdf(text: str, *, mermaid_renderer: str = "auto") -> tuple[str, MermaidStats]:
    """Normalize scientific math and convert Mermaid fences to printable HTML/SVG."""
    normalized = normalize_markdown_math_text(text)
    return render_mermaid_blocks(normalized, renderer=mermaid_renderer)


def render_mermaid_blocks(text: str, *, renderer: str = "auto") -> tuple[str, MermaidStats]:
    """Render Mermaid fenced blocks to inline SVG-backed HTML figures.

    `renderer=auto` tries a local Mermaid CLI first and falls back to a small
    built-in flowchart renderer. The fallback is intentionally limited, but it
    handles common `flowchart TB/LR` research diagrams without adding runtime
    dependencies or network calls.
    """
    if renderer not in {"auto", "cli", "fallback", "none"}:
        raise ValueError("mermaid_renderer must be one of: auto, cli, fallback, none")

    stats = {
        "diagrams": 0,
        "cli_rendered": 0,
        "fallback_rendered": 0,
        "skipped": 0,
        "failed": 0,
    }

    def repl(match: re.Match[str]) -> str:
        stats["diagrams"] += 1
        body = match.group("body").strip("\n")
        index = stats["diagrams"]
        if renderer == "none":
            stats["skipped"] += 1
            return match.group(0)
        try:
            svg = None
            if renderer in {"auto", "cli"}:
                svg = _render_mermaid_with_cli(body)
                if svg:
                    stats["cli_rendered"] += 1
            if svg is None:
                if renderer == "cli":
                    raise RuntimeError("Mermaid CLI was not found or failed.")
                svg = _render_mermaid_fallback_svg(body, diagram_id=f"geomine-mermaid-{index}")
                stats["fallback_rendered"] += 1
            return _mermaid_svg_figure(svg, index=index)
        except Exception as exc:  # noqa: BLE001 - fallback should preserve source context.
            stats["failed"] += 1
            escaped = html.escape(body)
            return (
                f'<figure class="geomine-mermaid-figure geomine-mermaid-failed">'
                f'<figcaption class="geomine-mermaid-caption">Mermaid diagram {index} render failed: {html.escape(str(exc))}</figcaption>'
                f'<pre><code class="language-mermaid">{escaped}</code></pre>'
                f"</figure>"
            )

    rendered = MERMAID_FENCE_RE.sub(repl, text)
    return rendered, MermaidStats(**stats)


def _render_mermaid_with_cli(source: str) -> str | None:
    mmdc = os.environ.get("MERMAID_CLI") or shutil.which("mmdc")
    if not mmdc:
        return None
    with tempfile.TemporaryDirectory(prefix="geomine-mermaid-") as tmp:
        tmp_path = Path(tmp)
        input_path = tmp_path / "diagram.mmd"
        output_path = tmp_path / "diagram.svg"
        input_path.write_text(source + "\n", encoding="utf-8")
        result = subprocess.run(
            [
                mmdc,
                "--input",
                str(input_path),
                "--output",
                str(output_path),
                "--backgroundColor",
                "transparent",
            ],
            text=True,
            capture_output=True,
            check=False,
            timeout=45,
        )
        if result.returncode != 0 or not output_path.exists():
            return None
        return _clean_svg_for_inline(output_path.read_text(encoding="utf-8"))


def _clean_svg_for_inline(svg: str) -> str:
    svg = re.sub(r"(?s)<\?xml.*?\?>", "", svg).strip()
    svg = re.sub(r"(?s)<!DOCTYPE.*?>", "", svg).strip()
    return svg


def _mermaid_svg_figure(svg: str, *, index: int) -> str:
    return (
        f'<figure class="geomine-mermaid-figure" data-mermaid-index="{index}">\n'
        f"{svg}\n"
        f'<figcaption class="geomine-mermaid-caption">Mermaid diagram {index}</figcaption>\n'
        f"</figure>"
    )


def _render_mermaid_fallback_svg(source: str, *, diagram_id: str) -> str:
    direction, nodes, edges = _parse_simple_mermaid_flowchart(source)
    if not edges:
        return _render_mermaid_source_as_svg(source, diagram_id=diagram_id)
    return _layout_flowchart_svg(direction=direction, nodes=nodes, edges=edges, diagram_id=diagram_id)


def _parse_simple_mermaid_flowchart(source: str) -> tuple[str, dict[str, str], list[dict[str, str]]]:
    direction = "TB"
    nodes: dict[str, str] = {}
    edges: list[dict[str, str]] = []
    edge_re = re.compile(
        r"^\s*(?P<src>[A-Za-z][A-Za-z0-9_]*)"
        r"(?:\[(?P<src_label>[^\]]+)\])?"
        r"\s*(?:-->|==>|-.->)"
        r"(?:\|(?P<edge_label>[^|]+)\|)?\s*"
        r"(?P<dst>[A-Za-z][A-Za-z0-9_]*)"
        r"(?:\[(?P<dst_label>[^\]]+)\])?"
        r"\s*$"
    )
    node_re = re.compile(r"^\s*(?P<id>[A-Za-z][A-Za-z0-9_]*)\[(?P<label>[^\]]+)\]\s*$")

    for raw_line in source.splitlines():
        line = raw_line.strip()
        if not line or line.startswith(("%%", "#")):
            continue
        flow = re.match(r"^(?:flowchart|graph)\s+(TB|TD|BT|LR|RL)\b", line, flags=re.IGNORECASE)
        if flow:
            direction = flow.group(1).upper()
            if direction == "TD":
                direction = "TB"
            continue
        edge = edge_re.match(line)
        if edge:
            src = edge.group("src")
            dst = edge.group("dst")
            nodes.setdefault(src, edge.group("src_label") or src)
            nodes.setdefault(dst, edge.group("dst_label") or dst)
            edges.append({"src": src, "dst": dst, "label": edge.group("edge_label") or ""})
            continue
        node = node_re.match(line)
        if node:
            nodes[node.group("id")] = node.group("label")
    return direction, nodes, edges


def _render_mermaid_source_as_svg(source: str, *, diagram_id: str) -> str:
    lines = ["Unsupported Mermaid block rendered as source:"] + source.splitlines()
    wrapped = [line for raw in lines for line in _wrap_label(raw, 72)]
    line_height = 20
    width = 860
    height = max(120, 30 + line_height * len(wrapped))
    text_lines = "\n".join(
        f'<text x="24" y="{32 + i * line_height}" class="geomine-mermaid-source">{html.escape(line)}</text>'
        for i, line in enumerate(wrapped)
    )
    return f"""<svg id="{diagram_id}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="Mermaid source fallback">
  <style>
    .geomine-mermaid-source-bg {{ fill: #f8fbfc; stroke: #b8c7cf; stroke-width: 1.2; }}
    .geomine-mermaid-source {{ font: 13px Menlo, Consolas, monospace; fill: #20313a; }}
  </style>
  <rect x="8" y="8" width="{width - 16}" height="{height - 16}" rx="8" class="geomine-mermaid-source-bg"/>
  {text_lines}
</svg>"""


def _layout_flowchart_svg(
    *,
    direction: str,
    nodes: dict[str, str],
    edges: list[dict[str, str]],
    diagram_id: str,
) -> str:
    ranks = _rank_flowchart_nodes(nodes, edges)
    by_rank: dict[int, list[str]] = {}
    for node_id, rank in ranks.items():
        by_rank.setdefault(rank, []).append(node_id)
    for rank_nodes in by_rank.values():
        rank_nodes.sort()

    dims = {node_id: _node_dimensions(label) for node_id, label in nodes.items()}
    horizontal = direction in {"LR", "RL"}
    if horizontal:
        positions, width, height = _layout_lr(by_rank, dims)
        if direction == "RL":
            positions = {node: (width - x - dims[node][0], y) for node, (x, y) in positions.items()}
    else:
        positions, width, height = _layout_tb(by_rank, dims)
        if direction == "BT":
            positions = {node: (x, height - y - dims[node][1]) for node, (x, y) in positions.items()}

    edge_svg = "\n".join(_edge_svg(edge, positions, dims, horizontal=horizontal) for edge in edges)
    node_svg = "\n".join(_node_svg(node_id, nodes[node_id], positions[node_id], dims[node_id]) for node_id in nodes)
    return f"""<svg id="{diagram_id}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-label="Mermaid flowchart">
  <defs>
    <marker id="{diagram_id}-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#2d5364"/>
    </marker>
  </defs>
  <style>
    .gm-node {{ fill: #f8fbfc; stroke: #2d5364; stroke-width: 1.5; }}
    .gm-node-text {{ font: 13px -apple-system, BlinkMacSystemFont, "PingFang SC", "Noto Sans CJK SC", Arial, sans-serif; fill: #172026; }}
    .gm-edge {{ fill: none; stroke: #2d5364; stroke-width: 1.5; marker-end: url(#{diagram_id}-arrow); }}
    .gm-edge-label-bg {{ fill: rgba(255,255,255,0.88); stroke: #d7e4ea; stroke-width: 0.8; }}
    .gm-edge-label {{ font: 12px -apple-system, BlinkMacSystemFont, "PingFang SC", "Noto Sans CJK SC", Arial, sans-serif; fill: #35505b; }}
  </style>
  <rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="10" fill="#ffffff" stroke="#edf3f5"/>
  {edge_svg}
  {node_svg}
</svg>"""


def _rank_flowchart_nodes(nodes: dict[str, str], edges: list[dict[str, str]]) -> dict[str, int]:
    ranks = {node_id: 0 for node_id in nodes}
    for _ in range(max(1, len(nodes))):
        changed = False
        for edge in edges:
            src = edge["src"]
            dst = edge["dst"]
            target = ranks.get(src, 0) + 1
            if target > ranks.get(dst, 0):
                ranks[dst] = target
                changed = True
        if not changed:
            break
    return ranks


def _node_dimensions(label: str) -> tuple[int, int, list[str]]:
    lines = _wrap_label(label, 28)
    max_width = max((_visual_width(line) for line in lines), default=1)
    width = min(360, max(150, max_width * 7 + 32))
    height = max(56, len(lines) * 18 + 24)
    return width, height, lines


def _layout_tb(
    by_rank: dict[int, list[str]],
    dims: dict[str, tuple[int, int, list[str]]],
) -> tuple[dict[str, tuple[int, int]], int, int]:
    rank_gap = 82
    node_gap = 34
    margin = 28
    rank_widths: dict[int, int] = {}
    rank_heights: dict[int, int] = {}
    for rank, node_ids in by_rank.items():
        rank_widths[rank] = sum(dims[node][0] for node in node_ids) + node_gap * max(0, len(node_ids) - 1)
        rank_heights[rank] = max(dims[node][1] for node in node_ids)
    width = max(760, max(rank_widths.values(), default=0) + 2 * margin)
    positions: dict[str, tuple[int, int]] = {}
    y = margin
    for rank in sorted(by_rank):
        row_width = rank_widths[rank]
        x = (width - row_width) // 2
        for node in by_rank[rank]:
            node_width, node_height, _ = dims[node]
            positions[node] = (x, y + (rank_heights[rank] - node_height) // 2)
            x += node_width + node_gap
        y += rank_heights[rank] + rank_gap
    height = y - rank_gap + margin
    return positions, width, height


def _layout_lr(
    by_rank: dict[int, list[str]],
    dims: dict[str, tuple[int, int, list[str]]],
) -> tuple[dict[str, tuple[int, int]], int, int]:
    rank_gap = 96
    node_gap = 28
    margin = 28
    rank_widths: dict[int, int] = {}
    rank_heights: dict[int, int] = {}
    for rank, node_ids in by_rank.items():
        rank_widths[rank] = max(dims[node][0] for node in node_ids)
        rank_heights[rank] = sum(dims[node][1] for node in node_ids) + node_gap * max(0, len(node_ids) - 1)
    height = max(360, max(rank_heights.values(), default=0) + 2 * margin)
    positions: dict[str, tuple[int, int]] = {}
    x = margin
    for rank in sorted(by_rank):
        column_height = rank_heights[rank]
        y = (height - column_height) // 2
        for node in by_rank[rank]:
            node_width, node_height, _ = dims[node]
            positions[node] = (x + (rank_widths[rank] - node_width) // 2, y)
            y += node_height + node_gap
        x += rank_widths[rank] + rank_gap
    width = x - rank_gap + margin
    return positions, width, height


def _node_svg(node_id: str, label: str, pos: tuple[int, int], dim: tuple[int, int, list[str]]) -> str:
    x, y = pos
    width, height, lines = dim
    escaped_id = html.escape(node_id)
    text_y = y + height / 2 - (len(lines) - 1) * 9
    tspans = "\n".join(
        f'<tspan x="{x + width / 2:.1f}" y="{text_y + i * 18:.1f}">{html.escape(line)}</tspan>'
        for i, line in enumerate(lines)
    )
    return f"""<g class="gm-node-group" data-node-id="{escaped_id}">
    <rect x="{x}" y="{y}" width="{width}" height="{height}" rx="8" class="gm-node"/>
    <text text-anchor="middle" class="gm-node-text">{tspans}</text>
  </g>"""


def _edge_svg(
    edge: dict[str, str],
    positions: dict[str, tuple[int, int]],
    dims: dict[str, tuple[int, int, list[str]]],
    *,
    horizontal: bool,
) -> str:
    src = edge["src"]
    dst = edge["dst"]
    sx, sy = positions[src]
    dx, dy = positions[dst]
    sw, sh, _ = dims[src]
    dw, dh, _ = dims[dst]
    if horizontal:
        x1, y1 = sx + sw, sy + sh / 2
        x2, y2 = dx, dy + dh / 2
        mid_x = (x1 + x2) / 2
        path = f"M {x1:.1f} {y1:.1f} C {mid_x:.1f} {y1:.1f}, {mid_x:.1f} {y2:.1f}, {x2 - 7:.1f} {y2:.1f}"
    else:
        x1, y1 = sx + sw / 2, sy + sh
        x2, y2 = dx + dw / 2, dy
        mid_y = (y1 + y2) / 2
        path = f"M {x1:.1f} {y1:.1f} C {x1:.1f} {mid_y:.1f}, {x2:.1f} {mid_y:.1f}, {x2:.1f} {y2 - 7:.1f}"
    label = edge.get("label", "")
    label_svg = ""
    if label:
        lx, ly = (x1 + x2) / 2, (y1 + y2) / 2 - 5
        label_width = min(260, max(52, _visual_width(label) * 6 + 16))
        label_svg = (
            f'<rect x="{lx - label_width / 2:.1f}" y="{ly - 14:.1f}" width="{label_width}" height="20" rx="4" class="gm-edge-label-bg"/>'
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" class="gm-edge-label">{html.escape(label)}</text>'
        )
    return f'<path d="{path}" class="gm-edge"/>{label_svg}'


def _wrap_label(label: str, max_units: int) -> list[str]:
    chunks = re.split(r"(\s+|/|,|，|:|：)", label.strip())
    lines: list[str] = []
    current = ""
    for chunk in chunks:
        if not chunk:
            continue
        candidate = current + chunk
        if current and _visual_width(candidate) > max_units:
            lines.append(current.strip())
            current = chunk.strip()
        else:
            current = candidate
    if current.strip():
        lines.append(current.strip())
    if not lines:
        return [label.strip() or " "]
    expanded: list[str] = []
    for line in lines:
        if _visual_width(line) <= max_units:
            expanded.append(line)
            continue
        segment = ""
        for char in line:
            if segment and _visual_width(segment + char) > max_units:
                expanded.append(segment)
                segment = char
            else:
                segment += char
        if segment:
            expanded.append(segment)
    return expanded


def _visual_width(value: str) -> int:
    total = 0
    for char in value:
        total += 2 if unicodedata.east_asian_width(char) in {"F", "W"} else 1
    return total


def _normalize_inline_formula_segments(line: str) -> str:
    parts = INLINE_MATH_RE.split(line)
    for idx in range(0, len(parts), 2):
        parts[idx] = _normalize_inline_code_spans(parts[idx])
    parts = INLINE_MATH_RE.split("".join(parts))
    for idx in range(0, len(parts), 2):
        parts[idx] = _normalize_bare_formula_tokens(parts[idx])
    return "".join(parts)


def _normalize_display_math_line(line: str) -> str:
    newline = ""
    body = line
    if line.endswith("\r\n"):
        body = line[:-2]
        newline = "\r\n"
    elif line.endswith("\n"):
        body = line[:-1]
        newline = "\n"
    return _normalize_tex_expression(body) + newline


def _normalize_inline_code_spans(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        raw = match.group(2)
        if _is_formula_like(raw):
            return f"${_normalize_tex_expression(raw)}$"
        return match.group(0)

    return CODE_SPAN_RE.sub(repl, text)


def _normalize_bare_formula_tokens(text: str) -> str:
    out: list[str] = []
    pos = 0
    for match in CODE_SPAN_RE.finditer(text):
        out.append(_normalize_bare_formula_plain(text[pos : match.start()]))
        out.append(match.group(0))
        pos = match.end()
    out.append(_normalize_bare_formula_plain(text[pos:]))
    return "".join(out)


def _normalize_bare_formula_plain(text: str) -> str:
    text = UNIT_EXPR_RE.sub(lambda m: f"${_normalize_unit_expression(m.group(0))}$", text)
    return INLINE_FORMULA_TOKEN_RE.sub(lambda m: f"${_normalize_tex_expression(m.group(1))}$", text)


def _is_formula_like(value: str) -> bool:
    stripped = value.strip()
    if not stripped:
        return False
    if "$" in stripped:
        return False
    if "/" in stripped and "+/-" not in stripped and not re.search(r"\s/\s|[A-Za-z0-9)]/[A-Za-z0-9(]", stripped):
        return False
    if "\\" in stripped and not re.search(r"\\[A-Za-z]+", stripped):
        return False
    if re.search(r"\.(?:md|pdf|py|json|ts|tsx|js|mjs|html|css|toml)$", stripped):
        return False
    if stripped.startswith(("http:", "https:", "file:")):
        return False
    if UNIT_EXPR_RE.fullmatch(stripped) or _is_unit_equation(stripped):
        return True
    if re.search(r"\b(?:kWh|MWh|MW_abs|MW|kg|yr|mol|J|m|s|V|Gy)\b", stripped) and (
        re.search(r"\d|\^-?\d|\^\{[-+]?\d+\}|H2", stripped)
    ):
        return True
    if re.search(r"\\[A-Za-z]+|[=+*/~]|\\to|->|\+/-", stripped) and re.search(r"[A-Za-z0-9]", stripped):
        return True
    if any(stripped.startswith(f"{accent}{{") for accent in ACCENTS):
        return True
    if re.match(rf"^(?:{'|'.join(map(re.escape, GREEK))})(?:_|$|\^)", stripped):
        return True
    if re.match(r"^[A-Z](?:_\{?[^}]+\}?|_[A-Za-z0-9]+|\^\{[^}]+\}|\^[A-Za-z0-9+-]+)+$", stripped):
        return True
    if re.match(r"^[A-Za-z]_\{[^}]+\}(?:\^\{[^}]+\})?$", stripped):
        return True
    if re.match(r"^[A-Z][a-z]?_\d+[A-Za-z0-9]*(?:\^\{[^}]+\})?$", stripped):
        return True
    if re.fullmatch(r"G\((?:H2|H2O2|e_aq\^-|•OH)\)(?:\s*(?:=|~|\\sim)\s*[-+]?\d+(?:\.\d+)?)?", stripped):
        return True
    if stripped in {"H•", "•OH"}:
        return True
    if re.fullmatch(r"e_?\{?aq\}?\^-?", stripped):
        return True
    if stripped in {"H2O", "H_2O", "H2", "H_2", "H2O2", "H_2O_2", "OH^{-}", "H_3O^{+}", "e_{aq}^{-}"}:
        return True
    return False


def _is_unit_equation(value: str) -> bool:
    return bool(
        re.fullmatch(
            rf"\s*(?:{UNIT_TOKEN_RE}(?:\s+{UNIT_TOKEN_RE})*|\d+(?:\.\d+)?\s+{UNIT_RE})"
            rf"(?:\s*=\s*(?:{UNIT_TOKEN_RE}(?:\s+{UNIT_TOKEN_RE})*|\d+(?:\.\d+)?\s+{UNIT_RE}))*\s*",
            value,
        )
    )


def _normalize_tex_expression(expr: str) -> str:
    text = expr.strip()
    if _is_unit_equation(text):
        return _normalize_unit_equation(text)
    if UNIT_EXPR_RE.fullmatch(text):
        return _normalize_unit_expression(text)

    text = re.sub(r"\b(\d+(?:\.\d+)?)\s+eV\b", r"\1\\,\\mathrm{eV}", text)
    text = re.sub(r"\b(\d+(?:\.\d+)?)\s+x\s+10", r"\1\\times 10", text)
    text = re.sub(r"(?<=[0-9)])\s+x\s+10", r"\\times 10", text)
    text = re.sub(r"\^(-?\d+)", r"^{\1}", text)
    text = text.replace("+/-", r"\pm")
    text = re.sub(r"(?<!\\)~", r"\\sim", text)
    text = text.replace("->", r"\to")
    text = re.sub(r"\bG\(e_aq\^-\)", r"G(e_{aq}^{-})", text)
    text = re.sub(r"\bG\(H2O2\)", r"G(H_2O_2)", text)
    text = re.sub(r"\bG\(H2\)", r"G(H_2)", text)
    text = re.sub(rf"(?<!\\)\b({'|'.join(map(re.escape, GREEK))})(?=(_|\^|\b))", lambda m: GREEK[m.group(1)], text)
    text = re.sub(r"(?<!\\)\b(dot|ddot|bar|hat|vec|tilde)\{([^{}]+)\}", r"\\\1{\2}", text)
    text = UNIT_EXPR_RE.sub(lambda m: _normalize_unit_expression(m.group(0)), text)
    text = KNOWN_UNIT_TOKEN_RE.sub(_normalize_known_unit_token, text)
    text = re.sub(r"_([A-Za-z][A-Za-z0-9&,]{1,})(?![A-Za-z0-9])", lambda m: "_{" + _roman_or_math(m.group(1)) + "}", text)
    text = re.sub(r"\^\{([A-Za-z][A-Za-z0-9 ]*)\}", lambda m: "^{" + _roman_or_math(m.group(1)) + "}", text)
    text = re.sub(r"\bH2O2\b", r"H_2O_2", text)
    text = re.sub(r"\bH2O\b", r"H_2O", text)
    text = re.sub(r"\bH2\b", r"H_2", text)
    text = re.sub(r"\bG\(H_2\)", r"G(H_2)", text)
    text = re.sub(r"\be_aq\^\{-\}", r"e_{aq}^{-}", text)
    text = re.sub(r"\be_aq\^-", r"e_{aq}^{-}", text)
    text = re.sub(r"\bOH\^\{-\}", r"OH^{-}", text)
    return text


def _roman_or_math(value: str) -> str:
    if "," in value:
        return ",".join(_roman_or_math(part) for part in value.split(","))
    if len(value) == 1:
        return value
    chemical = re.fullmatch(r"([A-Z][a-z]?)(\d+)", value)
    if chemical:
        return f"{chemical.group(1)}_{chemical.group(2)}"
    escaped = value.replace("&", r"\&")
    return rf"\mathrm{{{escaped}}}"


def _normalize_unit_equation(value: str) -> str:
    return " = ".join(_normalize_unit_expression(part.strip()) for part in value.split("="))


def _normalize_known_unit_token(match: re.Match[str]) -> str:
    unit = match.group(1)
    power = match.group(2)
    tex = UNIT_TEX.get(unit, rf"\mathrm{{{unit}}}")
    if power is not None:
        tex += f"^{{{power}}}"
    return tex


def _normalize_unit_expression(value: str) -> str:
    parts = value.split()
    normalized: list[str] = []
    for part in parts:
        number_unit = re.fullmatch(rf"(\d+(?:\.\d+)?)({UNIT_RE})", part)
        if number_unit:
            normalized.append(number_unit.group(1) + r"\,\mathrm{" + number_unit.group(2) + "}")
            continue
        match = re.fullmatch(rf"({UNIT_RE})(?:\^\{{([-+]?\d+)\}}|\^([-+]?\d+))?", part)
        if match:
            unit = match.group(1)
            power = match.group(2) or match.group(3)
            tex = UNIT_TEX.get(unit, rf"\mathrm{{{unit}}}")
            if power is not None:
                tex += f"^{{{power}}}"
            normalized.append(tex)
        else:
            normalized.append(part)
    return r"\,".join(normalized)


def _find_chrome() -> str:
    candidates = [
        os.environ.get("CHROME_BIN"),
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
        shutil.which("google-chrome"),
        shutil.which("chromium"),
        shutil.which("chrome"),
    ]
    for candidate in candidates:
        if candidate and Path(candidate).exists():
            return candidate
    raise RuntimeError("Chrome/Chromium was not found. Set CHROME_BIN or install Google Chrome.")


def _effective_css_text(custom_css: str | None = None) -> str:
    if custom_css is None:
        return DEFAULT_CSS
    return custom_css.rstrip() + "\n\n" + MANDATORY_MATH_LAYOUT_CSS.lstrip() + "\n\n" + MERMAID_LAYOUT_CSS.lstrip()


def export_pdf(args: argparse.Namespace) -> None:
    input_path = Path(args.input).resolve()
    output_pdf = Path(args.output).resolve()
    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    stem = output_pdf.with_suffix("")
    normalized_md = Path(args.normalized_output).resolve() if args.normalized_output else stem.with_suffix(".normalized.md")
    output_html = Path(args.html_output).resolve() if args.html_output else stem.with_suffix(".html")
    source_css_path = Path(args.css).resolve() if args.css else None
    css_path = stem.with_suffix(".effective.css") if source_css_path else stem.with_suffix(".print.css")

    source = input_path.read_text(encoding="utf-8")
    normalized, mermaid_stats = prepare_markdown_for_pdf(source, mermaid_renderer=args.mermaid_renderer)
    normalized_md.write_text(normalized, encoding="utf-8")
    custom_css = source_css_path.read_text(encoding="utf-8") if source_css_path else None
    css_path.write_text(_effective_css_text(custom_css), encoding="utf-8")

    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise RuntimeError("pandoc was not found on PATH.")

    pandoc_cmd = [
        pandoc,
        str(normalized_md),
        "--standalone",
        "--toc",
        f"--toc-depth={args.toc_depth}",
        f"--metadata=lang={args.lang}",
        f"--metadata=title={args.title or input_path.stem}",
        "--mathml",
        f"--css={css_path}",
        "--embed-resources",
        f"--output={output_html}",
    ]
    subprocess.run(pandoc_cmd, check=True)

    chrome = _find_chrome()
    chrome_cmd = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",
        f"--print-to-pdf={output_pdf}",
        output_html.resolve().as_uri(),
    ]
    subprocess.run(chrome_cmd, check=True)

    html = output_html.read_text(encoding="utf-8")
    math_tags = html.count("<math")
    math_code_blocks = html.count('<pre class="math"')
    mermaid_code_blocks = html.count("language-mermaid")
    print(f"Generated {output_pdf}")
    print(f"HTML: {output_html}")
    print(f"Normalized Markdown: {normalized_md}")
    print(f"Math tags: {math_tags}")
    print(f"Unconverted math code blocks: {math_code_blocks}")
    print(f"Mermaid diagrams: {mermaid_stats.diagrams}")
    print(f"Mermaid CLI rendered: {mermaid_stats.cli_rendered}")
    print(f"Mermaid fallback rendered: {mermaid_stats.fallback_rendered}")
    print(f"Unconverted mermaid code blocks: {mermaid_code_blocks}")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Markdown source file")
    parser.add_argument("--output", "-o", required=True, help="PDF output path")
    parser.add_argument("--title", help="Document title metadata")
    parser.add_argument("--lang", default="zh-CN", help="Document language metadata")
    parser.add_argument("--toc-depth", type=int, default=3, help="Table-of-contents depth")
    parser.add_argument("--css", help="Optional print CSS file")
    parser.add_argument("--html-output", help="Optional HTML intermediate path")
    parser.add_argument("--normalized-output", help="Optional normalized Markdown intermediate path")
    parser.add_argument(
        "--mermaid-renderer",
        choices=["auto", "cli", "fallback", "none"],
        default="auto",
        help="Mermaid renderer: auto uses local mmdc when present and built-in SVG fallback otherwise.",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        export_pdf(args)
    except Exception as exc:  # noqa: BLE001 - CLI should show concise context.
        print(f"error: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
