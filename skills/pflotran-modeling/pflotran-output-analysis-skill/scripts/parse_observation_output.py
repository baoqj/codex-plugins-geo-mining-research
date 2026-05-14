#!/usr/bin/env python3
"""Parse a simple PFLOTRAN observation CSV/TSV into JSON."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


def parse_table(path: Path, delimiter: str | None = None) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    sample = text[:2048]
    if delimiter is None:
        delimiter = "\t" if "\t" in sample and sample.count("\t") >= sample.count(",") else ","
    return [dict(row) for row in csv.DictReader(text.splitlines(), delimiter=delimiter)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--delimiter", choices=[",", "\\t"], default=None)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    rows = parse_table(args.input, "\t" if args.delimiter == "\\t" else args.delimiter)
    payload = {"row_count": len(rows), "columns": list(rows[0].keys()) if rows else [], "rows": rows}
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
