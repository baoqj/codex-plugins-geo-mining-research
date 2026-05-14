#!/usr/bin/env python3
"""Validate the GeoMine THMC Modeling skill family."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THMC_ROOT = ROOT / "skills" / "thmc-modeling"
REQUIRED_SKILLS = [
    "thmc-groundwater-router-skill",
    "conceptual-thmc-model-skill",
    "governing-equations-skill",
    "hydro-transport-skill",
    "geochemical-reaction-network-skill",
    "thermal-gradient-heat-transport-skill",
    "mechanical-damage-permeability-skill",
    "solver-selection-skill",
    "dgr-field-data-acquisition-skill",
    "phreeqc-coupling-skill",
    "ogs-pflotran-remote-run-skill",
    "reactive-transport-implementation-skill",
    "calibration-validation-skill",
    "uncertainty-sensitivity-skill",
    "thmc-paper-figure-skill",
    "thmc-report-synthesis-skill",
]
SCENARIOS = [
    "acid_mine_drainage",
    "radionuclide_transport",
    "uranium_mine_groundwater",
    "tailings_seepage",
    "nuclear_waste_repository",
    "bentonite_buffer_evolution",
    "geothermal_fluid_rock_interaction",
    "co2_storage_reactive_transport",
    "fractured_rock_contaminant_transport",
    "mining_heat_pollution",
    "groundwater_metal_mobility",
    "long_term_environmental_risk",
    "reactive_transport_benchmark",
    "custom_thmc_model",
]
COUPLING_LEVELS = ["H", "HC", "THC", "HM", "THM", "THMC"]
PACKAGE_SECTIONS = [
    "Research Objective",
    "Scenario Classification",
    "Conceptual THMC Model",
    "THMC Coupling Matrix",
    "Model Domain and Geometry",
    "Primary Variables",
    "Governing Equations",
    "Boundary and Initial Conditions",
    "Geochemical Reaction Network",
    "Parameters and Data Requirements",
    "Solver / Software Recommendation",
    "Implementation Plan",
    "Calibration and Validation Plan",
    "Sensitivity and Uncertainty Plan",
    "Expected Outputs",
    "Publication Figure Plan",
    "Limitations and Assumptions",
    "Machine-readable JSON Model Spec",
]
ROOT_REFERENCES = [
    "thmc-scenario-taxonomy.md",
    "thmc-coupling-map.md",
    "thmc-evidence-and-data-requirements.md",
    "thmc-modeling-limitations.md",
    "thmc-publication-caveats.md",
]
TEMPLATES = [
    "conceptual-thmc-model-skill/templates/conceptual-model-template.md",
    "conceptual-thmc-model-skill/templates/coupling-matrix-template.md",
    "geochemical-reaction-network-skill/templates/reaction-network-table-template.md",
    "geochemical-reaction-network-skill/templates/phreeqc-reaction-network-draft.md",
    "reactive-transport-implementation-skill/templates/implementation-plan-template.md",
    "reactive-transport-implementation-skill/templates/model-input-manifest-template.md",
    "calibration-validation-skill/templates/calibration-validation-plan-template.md",
    "calibration-validation-skill/templates/benchmark-selection-template.md",
    "uncertainty-sensitivity-skill/templates/sensitivity-analysis-plan-template.md",
    "uncertainty-sensitivity-skill/templates/uncertainty-analysis-plan-template.md",
    "thmc-paper-figure-skill/templates/thmc-figure-plan-template.md",
    "dgr-field-data-acquisition-skill/SKILL.md",
    "thmc-report-synthesis-skill/templates/thmc-modeling-package-template.md",
    "thmc-report-synthesis-skill/templates/thmc-model-spec-schema.json",
    "templates/thmc-modeling-package-2.0-template.md",
    "templates/thmc-model-spec.schema.json",
    "templates/thmc-run-record.schema.json",
    "templates/thmc-parameter-table-template.csv",
    "templates/thmc-reaction-network-template.md",
]


def _frontmatter(path: Path) -> dict[str, str] | None:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return None
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return data
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip("'").strip('"')
    return None


def failures() -> list[str]:
    errors: list[str] = []
    if not THMC_ROOT.exists():
        return [f"missing THMC root: {THMC_ROOT}"]

    for skill in REQUIRED_SKILLS:
        skill_md = THMC_ROOT / skill / "SKILL.md"
        if not skill_md.exists():
            errors.append(f"missing SKILL.md: {skill}")
            continue
        frontmatter = _frontmatter(skill_md)
        if frontmatter is None:
            errors.append(f"missing frontmatter: {skill}")
            continue
        if frontmatter.get("name") != skill:
            errors.append(f"name mismatch: {skill}")
        if not frontmatter.get("description"):
            errors.append(f"missing description: {skill}")

    router_text = (THMC_ROOT / "thmc-groundwater-router-skill" / "SKILL.md").read_text(
        encoding="utf-8"
    )
    for scenario in SCENARIOS:
        if scenario not in router_text:
            errors.append(f"router missing scenario: {scenario}")
    for level in COUPLING_LEVELS:
        if f"`{level}`" not in router_text and f'"{level}"' not in router_text:
            errors.append(f"router missing coupling level: {level}")

    synthesis_text = (
        THMC_ROOT
        / "thmc-report-synthesis-skill"
        / "templates"
        / "thmc-modeling-package-template.md"
    ).read_text(encoding="utf-8")
    for section in PACKAGE_SECTIONS:
        if section not in synthesis_text:
            errors.append(f"package template missing section: {section}")

    schema_path = (
        THMC_ROOT
        / "thmc-report-synthesis-skill"
        / "templates"
        / "thmc-model-spec-schema.json"
    )
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation should report context.
        errors.append(f"invalid JSON schema: {exc}")
    else:
        levels = schema["properties"]["coupling_level"]["enum"]
        if levels != COUPLING_LEVELS:
            errors.append("schema coupling_level enum mismatch")

    for reference in ROOT_REFERENCES:
        if not (ROOT / "references" / "thmc-modeling" / reference).exists():
            errors.append(f"missing root reference: {reference}")
    for template in TEMPLATES:
        if not (THMC_ROOT / template).exists():
            errors.append(f"missing template: {template}")
    return errors


def main() -> int:
    errors = failures()
    if errors:
        print("THMC skill family validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("THMC skill family validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
