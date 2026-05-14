import json
from pathlib import Path


SCHEMA_ROOT = Path(__file__).resolve().parents[1] / "schemas"


def load_schema(name: str) -> dict:
    return json.loads((SCHEMA_ROOT / name).read_text(encoding="utf-8"))


def test_schemas_are_valid_json_and_expose_required_contracts():
    for path in SCHEMA_ROOT.glob("*.json"):
        json.loads(path.read_text(encoding="utf-8"))

    output_schema = load_schema("output.schema.json")
    required = set(output_schema["required"])
    assert {
        "title",
        "abstract",
        "keywords",
        "research_questions",
        "hypotheses",
        "paper_outline",
        "evidence_matrix",
        "limitations",
        "references",
        "peer_review_checklist",
    }.issubset(required)
    assert output_schema["properties"]["equations"]["items"]["$ref"].startswith(
        "equation_registry.schema.json"
    )
    assert output_schema["properties"]["evidence_matrix"]["items"]["$ref"].startswith(
        "evidence_matrix.schema.json"
    )


def test_input_schema_defaults_support_academic_paper_generation():
    input_schema = load_schema("input.schema.json")
    assert input_schema["properties"]["target_paper_type"]["default"] == "research_article"
    assert input_schema["properties"]["citation_style"]["default"] == "ACS"
    assert input_schema["properties"]["include_equations"]["default"] is True
    assert "Research Questions and Hypotheses" in input_schema["properties"][
        "required_sections"
    ]["default"]
    assert "Equation Registry" in input_schema["properties"]["required_sections"][
        "default"
    ]
    assert "Evidence Matrix" in input_schema["properties"]["required_sections"][
        "default"
    ]
