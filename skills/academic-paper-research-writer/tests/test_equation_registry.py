import json
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def test_equation_schema_requires_units_and_boundary_conditions():
    schema = json.loads(
        (SKILL_ROOT / "schemas" / "equation_registry.schema.json").read_text(
            encoding="utf-8"
        )
    )
    variable_required = set(schema["$defs"]["variable"]["required"])
    equation_required = set(schema["$defs"]["equation"]["required"])
    assert {"symbol", "definition", "unit"}.issubset(variable_required)
    assert {
        "equation_id",
        "latex",
        "variables",
        "assumptions",
        "boundary_conditions",
    }.issubset(equation_required)


def test_examples_define_equations_as_registry_items():
    porous = (SKILL_ROOT / "examples" / "porous_media_radiolysis_paper.md").read_text(
        encoding="utf-8"
    )
    assert "## Equation Registry" in porous
    assert "Variables" in porous
    assert "Units" in porous
    assert "Boundary Conditions" in porous
    assert "```math" in porous
    assert "S_i^{rad}" in porous
    assert "mol m^{-3} s^{-1}" in porous
