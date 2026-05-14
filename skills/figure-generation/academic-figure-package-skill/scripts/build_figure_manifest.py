#!/usr/bin/env python3
"""Build a JSON figure manifest from a Figure Package Markdown file."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def _extract_section(block: str, heading: str) -> str:
    pattern = re.compile(
        rf"^{re.escape(heading)}\s*$([\s\S]*?)(?=^#### |\Z)", re.MULTILINE
    )
    match = pattern.search(block)
    return match.group(1).strip() if match else ""


def build_manifest(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    title_match = re.search(r"^# Figure Package:\s*(.+)$", text, re.MULTILINE)
    package_title = title_match.group(1).strip() if title_match else path.stem
    figure_matches = list(re.finditer(r"^### Figure\s+(\d+)\.?\s*(.*)$", text, re.MULTILINE))
    figures = []
    for idx, match in enumerate(figure_matches):
        start = match.start()
        end = figure_matches[idx + 1].start() if idx + 1 < len(figure_matches) else len(text)
        block = text[start:end]
        figure_id = f"Figure {match.group(1)}"
        title = match.group(2).strip() or figure_id
        intent_lines = _extract_section(block, "#### Intent").splitlines()
        figures.append(
            {
                "figure_id": figure_id,
                "title": title,
                "paper_section": "",
                "figure_type": intent_lines[0] if intent_lines else "",
                "main_message": "",
                "scientific_content": {
                    "entities": [],
                    "processes": [],
                    "relationships": [],
                    "data_layers": [],
                    "variables": [],
                    "uncertainties": [],
                    "caveats": [],
                },
                "visual_grammar": {
                    "colors": [],
                    "symbols": [],
                    "arrows": [],
                    "line_styles": [],
                    "fonts": [],
                    "panel_labels": [],
                },
                "layout": {
                    "panel_count": 1,
                    "panels": [],
                    "orientation": "",
                    "recommended_size": "",
                },
                "toolchain": {
                    "primary_tool": _extract_section(block, "#### Toolchain"),
                    "secondary_tools": [],
                    "export_formats": [],
                },
                "drawing_prompt": _extract_section(block, "#### Drawing Prompt"),
                "script_plan": _extract_section(block, "#### Script / Rendering Plan"),
                "caption_draft": _extract_section(block, "#### Caption Draft"),
                "provenance_requirements": [],
                "publication_checklist": _extract_section(block, "#### Publication Checklist").splitlines(),
                "caveats": [],
            }
        )
    return {
        "figure_package": {
            "title": package_title,
            "paper_title": package_title,
            "discipline": "",
            "target_journal": "",
            "created_for": "GeoMine Research",
            "figures": figures,
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown", type=Path, help="Figure Package Markdown file")
    parser.add_argument("--output", "-o", type=Path, help="Output JSON path")
    args = parser.parse_args()

    if not args.markdown.exists():
        print(f"missing file: {args.markdown}", file=sys.stderr)
        return 2
    manifest = build_manifest(args.markdown)
    output = json.dumps(manifest, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
