#!/usr/bin/env python3
"""Create a QGIS layout checklist for a map-based academic figure."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


def build_plan(title: str, crs: str, layers: list[str], output_format: str) -> str:
    layer_lines = "\n".join(f"- [ ] Add layer: {layer.strip()}" for layer in layers if layer.strip())
    if not layer_lines:
        layer_lines = "- [ ] Add verified GIS layers with source, date, license, and CRS."
    return f"""# QGIS Layout Plan: {title}

- [ ] Confirm project CRS: {crs}
- [ ] Set map extent and AOI boundary.
{layer_lines}
- [ ] Add legend with layer names and symbols.
- [ ] Add scale bar.
- [ ] Add north arrow.
- [ ] Add inset map for regional context if needed.
- [ ] Add data source, date, CRS, and spatial precision note.
- [ ] Add caveat for approximate, inferred, or conceptual layers.
- [ ] Export as {output_format} plus a PNG preview.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", default="Academic Map Figure")
    parser.add_argument("--crs", default="EPSG:4326")
    parser.add_argument("--layers", default="", help="Comma-separated layer names")
    parser.add_argument("--output-format", default="PDF/SVG")
    parser.add_argument("--output", "-o", type=Path)
    args = parser.parse_args()

    plan = build_plan(args.title, args.crs, args.layers.split(","), args.output_format)
    if args.output:
        args.output.write_text(plan, encoding="utf-8")
    else:
        print(plan, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main())
