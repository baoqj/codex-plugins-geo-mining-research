#!/usr/bin/env python3
"""Batch-render GeoMine normalized Markdown papers to PDF.

This utility delegates formula handling and PDF rendering to
build_pdf_with_math.py, while enforcing the convention
`paper.normalized.md -> paper.normalized.pdf`.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def iter_normalized_markdown(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.normalized.md")
        if path.is_file()
        and not path.name.endswith(".render.normalized.md")
        and ".normalized.normalized." not in path.name
    )


def render_one(source: Path, renderer: Path, dry_run: bool) -> tuple[bool, str]:
    pdf_output = source.with_suffix(".pdf")
    html_output = source.with_suffix(".html")
    temp_normalized = source.with_name(f"{source.stem}.render.md")

    cmd = [
        sys.executable,
        str(renderer),
        str(source),
        "--output",
        str(pdf_output),
        "--html-output",
        str(html_output),
        "--normalized-output",
        str(temp_normalized),
        "--title",
        source.stem.replace("_", " "),
    ]

    if dry_run:
        print("DRY-RUN", " ".join(cmd))
        return True, str(pdf_output)

    completed = subprocess.run(
        cmd,
        cwd=str(source.parent),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if completed.returncode == 0:
        temp_normalized.unlink(missing_ok=True)
        print(f"OK {pdf_output}")
        return True, str(pdf_output)

    print(f"FAIL {source}")
    print(completed.stdout)
    return False, str(pdf_output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="report", help="Root directory to scan")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    renderer = Path(__file__).resolve().with_name("build_pdf_with_math.py")

    if not root.exists():
        print(f"Root not found: {root}", file=sys.stderr)
        return 2
    if not renderer.exists():
        print(f"Renderer not found: {renderer}", file=sys.stderr)
        return 2

    sources = iter_normalized_markdown(root)
    print(f"Found {len(sources)} normalized Markdown files")
    failures: list[tuple[Path, str]] = []

    for source in sources:
        ok, output = render_one(source.resolve(), renderer, args.dry_run)
        if not ok:
            failures.append((source, output))

    if failures:
        print("Failed normalized PDF exports:")
        for source, output in failures:
            print(f"- {source} -> {output}")
        return 1

    print("All normalized PDF exports completed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
