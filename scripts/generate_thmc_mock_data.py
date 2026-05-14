#!/usr/bin/env python3
"""Export GeoMine THMC mock data to a JSON file for demos and tests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
THMC_SRC = ROOT / "mcp" / "geomine-thmc-server" / "src"
sys.path.insert(0, str(THMC_SRC))

from geomine_thmc_mcp.storage import (  # noqa: E402
    MOCK_AOIS,
    MOCK_ASSETS,
    MOCK_LITHOLOGY,
    MOCK_MINERALS,
    MOCK_PROJECTS,
    MOCK_WATER_SAMPLES,
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="examples/thmc-mock-data.json")
    args = parser.parse_args()
    out = ROOT / args.output
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "projects": MOCK_PROJECTS,
        "aois": MOCK_AOIS,
        "water_samples": MOCK_WATER_SAMPLES,
        "lithology_units": MOCK_LITHOLOGY,
        "mineral_assemblages": MOCK_MINERALS,
        "assets": MOCK_ASSETS,
    }
    out.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
