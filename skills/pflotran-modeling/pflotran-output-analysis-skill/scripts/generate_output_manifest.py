#!/usr/bin/env python3
"""Generate an expected PFLOTRAN output manifest."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model-name", required=True)
    parser.add_argument("--variable", action="append", default=[])
    parser.add_argument("--observation", action="append", default=[])
    parser.add_argument("--spatial-output", action="append", default=[])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    payload = {
        "model_name": args.model_name,
        "variables": args.variable,
        "observation_points": args.observation,
        "spatial_outputs": args.spatial_output,
        "expected_files": ["pflotran.h5", "pflotran.out", "observation.csv"],
        "status": "planned",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    text = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
