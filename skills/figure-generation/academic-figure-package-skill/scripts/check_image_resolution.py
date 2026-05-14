#!/usr/bin/env python3
"""Check basic image dimensions and likely 300 dpi print suitability."""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path


def png_size(data: bytes) -> tuple[int, int] | None:
    if data.startswith(b"\x89PNG\r\n\x1a\n") and len(data) >= 24:
        width, height = struct.unpack(">II", data[16:24])
        return width, height
    return None


def jpeg_size(data: bytes) -> tuple[int, int] | None:
    if not data.startswith(b"\xff\xd8"):
        return None
    idx = 2
    while idx + 9 < len(data):
        if data[idx] != 0xFF:
            idx += 1
            continue
        marker = data[idx + 1]
        idx += 2
        if marker in (0xD8, 0xD9):
            continue
        if idx + 2 > len(data):
            break
        length = struct.unpack(">H", data[idx : idx + 2])[0]
        if marker in range(0xC0, 0xCF) and marker not in (0xC4, 0xC8, 0xCC):
            height, width = struct.unpack(">HH", data[idx + 3 : idx + 7])
            return width, height
        idx += length
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("image", type=Path, help="PNG or JPEG image")
    parser.add_argument("--print-width-in", type=float, default=6.0)
    parser.add_argument("--min-dpi", type=float, default=300.0)
    args = parser.parse_args()

    data = args.image.read_bytes()
    size = png_size(data) or jpeg_size(data)
    if size is None:
        print("Could not read dimensions with standard-library parser", file=sys.stderr)
        return 2
    width, height = size
    effective_dpi = width / args.print_width_in
    print(f"Image size: {width} x {height} px")
    print(f"Effective DPI at {args.print_width_in:g} in width: {effective_dpi:.1f}")
    if effective_dpi < args.min_dpi:
        print("WARNING: image may be below target print resolution")
        return 1
    print("Resolution check: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
