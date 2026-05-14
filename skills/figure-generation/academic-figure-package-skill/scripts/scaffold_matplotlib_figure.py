#!/usr/bin/env python3
"""Create a lightweight Matplotlib plotting scaffold from figure metadata."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path


TEMPLATE = '''#!/usr/bin/env python3
"""Matplotlib scaffold for {title}."""

from pathlib import Path

import matplotlib.pyplot as plt


def main():
    # Replace placeholder data with verified, provenance-tracked values.
    x = [0, 1, 2, 3]
    y = [0, 1, 1.5, 2.2]
    fig, ax = plt.subplots(figsize=({width}, {height}), constrained_layout=True)
    ax.plot(x, y, marker="o", label="{series_label}")
    ax.set_title("{title}")
    ax.set_xlabel("{xlabel}")
    ax.set_ylabel("{ylabel}")
    ax.grid(True, alpha=0.25)
    ax.legend()
    output = Path("{output}")
    fig.savefig(output, dpi=300)
    print(f"wrote {{output}}")


if __name__ == "__main__":
    main()
'''


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--title", default="Academic Data Figure")
    parser.add_argument("--xlabel", default="x")
    parser.add_argument("--ylabel", default="y")
    parser.add_argument("--series-label", default="verified data")
    parser.add_argument("--width", type=float, default=6.5)
    parser.add_argument("--height", type=float, default=4.0)
    parser.add_argument("--figure-output", default="figure.png")
    parser.add_argument("--output", "-o", type=Path, help="Write scaffold script to this path")
    args = parser.parse_args()

    script = TEMPLATE.format(
        title=args.title.replace('"', "'"),
        xlabel=args.xlabel.replace('"', "'"),
        ylabel=args.ylabel.replace('"', "'"),
        series_label=args.series_label.replace('"', "'"),
        width=args.width,
        height=args.height,
        output=args.figure_output,
    )
    if args.output:
        args.output.write_text(script, encoding="utf-8")
    else:
        print(script)
    return 0


if __name__ == "__main__":
    sys.exit(main())
