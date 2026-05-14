#!/usr/bin/env python3
"""Generate a PHREEQC SELECTED_OUTPUT block."""

from __future__ import annotations

import argparse
from pathlib import Path


def _split(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def build_block(number: int, output_file: str, totals: list[str], saturation_indices: list[str], molalities: list[str]) -> str:
    lines = [
        f"SELECTED_OUTPUT {number}",
        f"  -file {output_file}",
        "  -reset false",
        "  -simulation true",
        "  -state true",
        "  -solution true",
        "  -distance true",
        "  -time true",
        "  -step true",
        "  -pH true",
        "  -pe true",
        "  -temperature true",
        "  -alkalinity true",
        "  -ionic_strength true",
        "  -charge_balance true",
        "  -percent_error true",
        "  -water true",
    ]
    if totals:
        lines.append("  -totals " + " ".join(totals))
    if saturation_indices:
        lines.append("  -saturation_indices " + " ".join(saturation_indices))
    if molalities:
        lines.append("  -molalities " + " ".join(molalities))
    lines.append("END")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--number", type=int, default=1)
    parser.add_argument("--file", default="selected_output.sel", help="PHREEQC selected output filename")
    parser.add_argument("--totals", default="", help="Comma-separated elements")
    parser.add_argument("--saturation-indices", default="", help="Comma-separated minerals")
    parser.add_argument("--molalities", default="", help="Comma-separated species")
    parser.add_argument("--output", type=Path, help="Optional PHREEQC fragment path")
    args = parser.parse_args()

    block = build_block(args.number, args.file, _split(args.totals), _split(args.saturation_indices), _split(args.molalities))
    if args.output:
        args.output.write_text(block, encoding="utf-8")
    else:
        print(block, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
