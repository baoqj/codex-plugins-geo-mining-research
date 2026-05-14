#!/usr/bin/env python3
"""Validate a PFLOTRAN input deck skeleton without executing PFLOTRAN."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_BLOCKS = ["SIMULATION", "SUBSURFACE", "END_SUBSURFACE"]
RECOMMENDED_BLOCKS = ["GRID", "REGION", "MATERIAL_PROPERTY", "CHEMISTRY", "OUTPUT"]


def validate_deck(path: Path) -> dict[str, object]:
    text = path.read_text(encoding="utf-8", errors="replace")
    upper = text.upper()
    missing_required = [block for block in REQUIRED_BLOCKS if block not in upper]
    missing_recommended = [block for block in RECOMMENDED_BLOCKS if block not in upper]
    placeholders = sorted(set(re.findall(r"<[^>\n]+>", text)))
    warnings = []
    if placeholders:
        warnings.append("Input deck contains placeholders and is not ready for execution.")
    if missing_recommended:
        warnings.append("Recommended PFLOTRAN blocks are missing or not detected.")
    return {
        "ok": not missing_required,
        "input": str(path),
        "missing_required_blocks": missing_required,
        "missing_recommended_blocks": missing_recommended,
        "placeholder_count": len(placeholders),
        "placeholders": placeholders,
        "warnings": warnings,
        "status": "draft_not_executed",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = validate_deck(args.input)
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
