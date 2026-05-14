#!/usr/bin/env python3
"""Parse a PHREEQC SELECTED_OUTPUT table into JSON or CSV."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def parse_selected_output(path: Path) -> list[dict[str, str]]:
    lines = [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip()]
    if not lines:
        return []
    header = lines[0].split()
    rows: list[dict[str, str]] = []
    for line in lines[1:]:
        values = line.split()
        row = {header[index]: values[index] if index < len(values) else "" for index in range(len(header))}
        rows.append(row)
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="PHREEQC selected output file")
    parser.add_argument("--format", choices=["json", "csv"], default="json")
    parser.add_argument("--output", type=Path, help="Optional output path")
    args = parser.parse_args()

    rows = parse_selected_output(args.input)
    if args.format == "json":
        text = json.dumps({"row_count": len(rows), "rows": rows}, indent=2, ensure_ascii=False) + "\n"
    else:
        if rows:
            from io import StringIO

            buffer = StringIO()
            writer = csv.DictWriter(buffer, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)
            text = buffer.getvalue()
        else:
            text = ""

    if args.output:
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
