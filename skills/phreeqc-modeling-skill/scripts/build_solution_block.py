#!/usr/bin/env python3
"""Build a PHREEQC SOLUTION block from one row of a local chemistry table."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path


FIELD_ALIASES = {
    "sample_id": ("sample_id", "sample", "id"),
    "temperature_c": ("temperature_c", "temp_c", "temperature", "temp"),
    "ph": ("ph", "pH"),
    "pe": ("pe",),
    "eh_mv": ("eh_mv", "Eh_mV", "eh", "Eh"),
    "units": ("units", "unit"),
    "density": ("density", "density_kg_L", "density_kg_l"),
    "alkalinity": ("alkalinity", "alk", "alkalinity_mg_l", "alkalinity_mg_l_as_caco3"),
}
ELEMENT_ALIASES = {
    "Ca": ("Ca", "ca", "calcium"),
    "Mg": ("Mg", "mg", "magnesium"),
    "Na": ("Na", "na", "sodium"),
    "K": ("K", "k", "potassium"),
    "Cl": ("Cl", "cl", "chloride"),
    "S(6)": ("S(6)", "SO4", "so4", "sulfate"),
    "Fe": ("Fe", "fe", "iron"),
    "Al": ("Al", "al", "aluminum", "aluminium"),
    "Mn": ("Mn", "mn", "manganese"),
    "U": ("U", "u", "uranium"),
    "Ra": ("Ra", "ra", "radium"),
    "Pb": ("Pb", "pb", "lead"),
    "Zn": ("Zn", "zn", "zinc"),
    "Cu": ("Cu", "cu", "copper"),
    "Ni": ("Ni", "ni", "nickel"),
    "As": ("As", "as", "arsenic"),
}


def _load_rows(path: Path) -> list[dict[str, str]]:
    if path.suffix.lower() == ".json":
        data = json.loads(path.read_text(encoding="utf-8"))
        if isinstance(data, dict):
            data = data.get("rows", [])
        return [dict(row) for row in data]
    delimiter = "\t" if path.suffix.lower() in {".tsv", ".tab"} else ","
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return [dict(row) for row in csv.DictReader(handle, delimiter=delimiter)]


def _lookup(row: dict[str, str], aliases: tuple[str, ...]) -> str | None:
    lower = {key.lower(): key for key in row}
    for alias in aliases:
        key = lower.get(alias.lower())
        if key is not None and str(row.get(key, "")).strip() != "":
            return str(row[key]).strip()
    return None


def _find_row(rows: list[dict[str, str]], sample_id: str | None) -> dict[str, str]:
    if not rows:
        raise ValueError("input table has no rows")
    if not sample_id:
        return rows[0]
    for row in rows:
        row_sample = _lookup(row, FIELD_ALIASES["sample_id"])
        if row_sample == sample_id:
            return row
    raise ValueError(f"sample_id not found: {sample_id}")


def build_solution(row: dict[str, str], solution_number: int, default_units: str, charge_balance: bool) -> str:
    sample_id = _lookup(row, FIELD_ALIASES["sample_id"]) or "<sample_id>"
    temp = _lookup(row, FIELD_ALIASES["temperature_c"]) or "<temperature_C>"
    ph = _lookup(row, FIELD_ALIASES["ph"]) or "<pH_value>"
    pe = _lookup(row, FIELD_ALIASES["pe"]) or "<pe_value>"
    units = _lookup(row, FIELD_ALIASES["units"]) or default_units
    density = _lookup(row, FIELD_ALIASES["density"])
    alkalinity = _lookup(row, FIELD_ALIASES["alkalinity"])

    lines = [
        f"SOLUTION {solution_number} {sample_id}",
        f"  temp {temp}",
        f"  units {units}",
        f"  pH {ph}{' charge' if charge_balance else ''}",
        f"  pe {pe}",
    ]
    if density:
        lines.append(f"  density {density}")
    if alkalinity:
        if any(key.lower() == "alkalinity_mg_l_as_caco3" for key in row):
            lines.append(f"  Alkalinity {alkalinity} as CaCO3")
        else:
            lines.append(f"  Alkalinity {alkalinity}")

    for element, aliases in ELEMENT_ALIASES.items():
        value = _lookup(row, aliases)
        if value is None:
            continue
        if element == "S(6)" and any(alias.lower() in {"so4", "sulfate"} for alias in aliases):
            lines.append(f"  {element} {value} as SO4")
        else:
            lines.append(f"  {element} {value}")
    lines.append("END")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="CSV, TSV, or JSON chemistry table")
    parser.add_argument("--sample-id", help="Sample ID to select; defaults to first row")
    parser.add_argument("--solution-number", type=int, default=1)
    parser.add_argument("--default-units", default="mg/L")
    parser.add_argument("--charge-balance", action="store_true", help="Append charge to the pH line")
    parser.add_argument("--output", type=Path, help="Optional output .phr path")
    args = parser.parse_args()

    block = build_solution(_find_row(_load_rows(args.input), args.sample_id), args.solution_number, args.default_units, args.charge_balance)
    if args.output:
        args.output.write_text(block, encoding="utf-8")
    else:
        print(block, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
