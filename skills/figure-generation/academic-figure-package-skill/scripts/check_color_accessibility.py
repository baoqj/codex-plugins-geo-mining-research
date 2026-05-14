#!/usr/bin/env python3
"""Check figure text/specs for red-green-only color encoding risk."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def check_text(text: str) -> list[str]:
    lowered = text.lower()
    warnings: list[str] = []
    has_red_green = "red" in lowered and "green" in lowered
    has_redundant = any(term in lowered for term in ["symbol", "label", "line style", "hatching", "shape"])
    if has_red_green and not has_redundant:
        warnings.append("red/green encoding found without clear redundant symbols, labels, shapes, hatching, or line styles")
    if "colorblind" not in lowered and "accessib" not in lowered:
        warnings.append("no color accessibility note found")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path, help="Text or Markdown spec file")
    parser.add_argument("--text", help="Inline text to check")
    args = parser.parse_args()

    if args.text:
        text = args.text
    elif args.input:
        text = args.input.read_text(encoding="utf-8")
    else:
        print("provide a file or --text", file=sys.stderr)
        return 2

    warnings = check_text(text)
    if warnings:
        for warning in warnings:
            print(f"WARNING: {warning}")
        return 1
    print("Color accessibility check: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
