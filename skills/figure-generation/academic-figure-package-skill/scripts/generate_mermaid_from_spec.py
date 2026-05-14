#!/usr/bin/env python3
"""Generate a Mermaid scaffold from a workflow or mechanism figure spec."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def build_mermaid(title: str, mode: str, nodes: list[str]) -> str:
    safe_nodes = [node.strip() for node in nodes if node.strip()]
    if not safe_nodes:
        safe_nodes = ["Research question", "Evidence", "Interpretation", "Figure output"]
    lines = ["flowchart LR", f'  title["{title}"]']
    previous = "title"
    for idx, node in enumerate(safe_nodes, start=1):
        node_id = f"n{idx}"
        label = node.replace('"', "'")
        lines.append(f'  {node_id}["{label}"]')
        arrow = "-->" if mode == "workflow" else "-.->"
        lines.append(f"  {previous} {arrow} {node_id}")
        previous = node_id
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", default="Academic Figure Scaffold")
    parser.add_argument("--mode", choices=["workflow", "mechanism"], default="workflow")
    parser.add_argument("--nodes", default="", help="Comma-separated node labels")
    parser.add_argument("--output", "-o", type=Path)
    args = parser.parse_args()

    mermaid = build_mermaid(args.title, args.mode, args.nodes.split(","))
    if args.output:
        args.output.write_text(mermaid, encoding="utf-8")
    else:
        print(mermaid, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
