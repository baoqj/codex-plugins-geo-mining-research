#!/usr/bin/env python3
"""Build basic numeric summaries from parsed PFLOTRAN observation rows."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def _float(value: object) -> float | None:
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path, help="JSON produced by parse_observation_output.py")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    rows = data.get("rows", [])
    summary: dict[str, dict[str, float | int]] = {}
    for column in data.get("columns", []):
        values = [v for row in rows if (v := _float(row.get(column))) is not None]
        if values:
            summary[column] = {"count": len(values), "min": min(values), "max": max(values), "last": values[-1]}
    payload = {"row_count": len(rows), "numeric_summary": summary, "status": "parsed_not_interpreted"}
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
