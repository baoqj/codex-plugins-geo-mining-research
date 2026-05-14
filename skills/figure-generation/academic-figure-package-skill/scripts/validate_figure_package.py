#!/usr/bin/env python3
"""Validate an Academic Figure Package Markdown or JSON file."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REQUIRED_SECTIONS = [
    "## 1. Figure Strategy",
    "## 2. Figure Inventory",
    "## 3. Figure Specifications",
    "## 4. Cross-Figure Visual Consistency",
    "## 5. Data and Provenance Requirements",
    "## 6. Caveats",
    "## 7. Machine-Readable JSON Summary",
]
FIGURE_FIELDS = [
    "#### Intent",
    "#### Scientific Content",
    "#### Visual Grammar",
    "#### Layout Plan",
    "#### Toolchain",
    "#### Drawing Prompt",
    "#### Script / Rendering Plan",
    "#### Caption Draft",
    "#### Publication Checklist",
]
GIS_TERMS = ("gis / map", "gis figure", "study area", "claim map", "claim location", "location map", "geological setting")
GIS_REQUIREMENTS = ("crs", "scale bar", "north arrow", "legend", "source")
GEOCHEM_TERMS = ("geochemical-anomaly", "geochemical anomaly", "anomaly", "pathfinder", "assay")
GEOCHEM_REQUIREMENTS = ("unit", "sample medium", "qaqc", "qa/qc", "detection limit")


def _figure_blocks(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"^### Figure\s+\d+\.?\s*(.*)$", text, re.MULTILINE))
    blocks: list[tuple[str, str]] = []
    for idx, match in enumerate(matches):
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        title = match.group(0).strip()
        blocks.append((title, text[start:end]))
    return blocks


def validate_markdown(path: Path) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    lowered = text.lower()
    errors: list[str] = []
    warnings: list[str] = []

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"missing required section: {section}")

    blocks = _figure_blocks(text)
    if not blocks:
        errors.append("no figure specifications found")

    for title, block in blocks:
        block_lower = block.lower()
        for field in FIGURE_FIELDS:
            if field not in block:
                errors.append(f"{title}: missing {field}")

        if any(term in block_lower for term in GIS_TERMS):
            missing = [term for term in GIS_REQUIREMENTS if term not in block_lower]
            if missing:
                errors.append(f"{title}: GIS figure missing {', '.join(missing)}")

        if any(term in block_lower for term in GEOCHEM_TERMS):
            has_qaqc = "qaqc" in block_lower or "qa/qc" in block_lower
            missing = [
                term
                for term in GEOCHEM_REQUIREMENTS
                if term not in ("qaqc", "qa/qc") and term not in block_lower
            ]
            if not has_qaqc:
                missing.append("QA/QC")
            if missing:
                errors.append(f"{title}: geochemistry figure missing {', '.join(missing)}")

    if "qualified person" not in lowered and "qp" not in lowered:
        warnings.append("mining/disclosure caveat does not mention QP or Qualified Person")
    if "not investment advice" not in lowered:
        warnings.append("caveats do not explicitly say not investment advice")
    return errors, warnings


def validate_json(path: Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    data = json.loads(path.read_text(encoding="utf-8"))
    package = data.get("figure_package")
    if not isinstance(package, dict):
        return ["JSON missing figure_package object"], warnings
    figures = package.get("figures")
    if not isinstance(figures, list) or not figures:
        errors.append("figure_package.figures must be a non-empty list")
        return errors, warnings
    for idx, figure in enumerate(figures, start=1):
        if not isinstance(figure, dict):
            errors.append(f"Figure {idx}: figure entry must be an object")
            continue
        for key in [
            "figure_id",
            "title",
            "figure_type",
            "main_message",
            "toolchain",
            "caption_draft",
            "publication_checklist",
            "caveats",
        ]:
            if key not in figure:
                errors.append(f"Figure {idx}: missing {key}")
    return errors, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="Figure Package Markdown or JSON file")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable report")
    args = parser.parse_args()

    if not args.path.exists():
        print(f"missing file: {args.path}", file=sys.stderr)
        return 2

    try:
        if args.path.suffix.lower() == ".json":
            errors, warnings = validate_json(args.path)
        else:
            errors, warnings = validate_markdown(args.path)
    except Exception as exc:  # noqa: BLE001 - validation should report context.
        print(f"validation failed to read {args.path}: {exc}", file=sys.stderr)
        return 2

    report = {
        "path": str(args.path),
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
    }
    if args.json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"Figure Package validation: {'PASS' if not errors else 'FAIL'}")
        for error in errors:
            print(f"ERROR: {error}")
        for warning in warnings:
            print(f"WARNING: {warning}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
