#!/usr/bin/env python3
"""Audit a local groundwater chemistry table for PHREEQC readiness."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Iterable


CORE_FIELDS = {
    "sample_id": {"sample_id", "sample", "id"},
    "temperature_c": {"temperature_c", "temp_c", "temperature", "temp"},
    "ph": {"ph", "pH"},
    "units": {"units", "unit"},
    "alkalinity": {"alkalinity", "alk", "alkalinity_mg_l", "alkalinity_mg_l_as_caco3"},
}
RECOMMENDED_MAJOR_IONS = {
    "Ca": {"ca", "calcium"},
    "Mg": {"mg", "magnesium"},
    "Na": {"na", "sodium"},
    "K": {"k", "potassium"},
    "Cl": {"cl", "chloride"},
    "S(6)/SO4": {"s(6)", "so4", "sulfate"},
    "C(4)/HCO3": {"c(4)", "hco3", "bicarbonate", "dic"},
}


def _load_rows(path: Path, fmt: str) -> list[dict[str, object]]:
    if fmt == "auto":
        suffix = path.suffix.lower()
        if suffix == ".json":
            fmt = "json"
        elif suffix in {".tsv", ".tab"}:
            fmt = "tsv"
        else:
            fmt = "csv"

    if fmt == "json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("rows", [])
        if not isinstance(data, list):
            raise ValueError("JSON input must be a list of objects or an object with a rows list")
        return [dict(row) for row in data]

    delimiter = "\t" if fmt == "tsv" else ","
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [dict(row) for row in csv.DictReader(handle, delimiter=delimiter)]


def _canonical_columns(columns: Iterable[str]) -> dict[str, str]:
    normalized = {column.strip().lower(): column for column in columns}
    result: dict[str, str] = {}
    for field, aliases in CORE_FIELDS.items():
        for alias in aliases:
            match = normalized.get(alias.lower())
            if match:
                result[field] = match
                break
    return result


def _blank(value: object) -> bool:
    return value is None or str(value).strip() == ""


def audit(path: Path, fmt: str) -> dict[str, object]:
    rows = _load_rows(path, fmt)
    columns = list(rows[0].keys()) if rows else []
    canonical = _canonical_columns(columns)
    missing_core = [field for field in CORE_FIELDS if field not in canonical]
    normalized_columns = {column.strip().lower() for column in columns}
    present_major_ions = sorted(
        ion for ion, aliases in RECOMMENDED_MAJOR_IONS.items() if normalized_columns.intersection(aliases)
    )

    row_warnings: list[dict[str, object]] = []
    sample_col = canonical.get("sample_id")
    for index, row in enumerate(rows, start=1):
        missing_values = [field for field, column in canonical.items() if _blank(row.get(column))]
        if missing_values:
            row_warnings.append(
                {
                    "row": index,
                    "sample_id": row.get(sample_col, f"row-{index}") if sample_col else f"row-{index}",
                    "missing_values": missing_values,
                }
            )

    return {
        "ok": bool(rows) and not missing_core,
        "row_count": len(rows),
        "columns": columns,
        "recognized_core_fields": canonical,
        "missing_core_fields": missing_core,
        "present_major_ions": present_major_ions,
        "missing_recommended_major_ions": sorted(set(RECOMMENDED_MAJOR_IONS) - set(present_major_ions)),
        "row_warnings": row_warnings,
        "interpretation_limits": [
            "Missing pH, temperature, units, or alkalinity limits PHREEQC speciation reliability.",
            "Missing major ions prevents robust charge-balance and saturation-index interpretation.",
            "Missing pe/Eh requires explicit redox assumptions; do not infer redox speciation automatically.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV, TSV, or JSON chemistry table")
    parser.add_argument("--format", choices=["auto", "csv", "tsv", "json"], default="auto")
    parser.add_argument("--output", type=Path, help="Optional JSON output path")
    args = parser.parse_args()

    result = audit(args.input, args.format)
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
