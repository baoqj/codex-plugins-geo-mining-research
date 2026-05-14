from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "---"
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return data
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    raise AssertionError("frontmatter not closed")


def test_skill_manifest_and_assets_exist():
    frontmatter = parse_frontmatter(SKILL_ROOT / "SKILL.md")
    assert frontmatter["name"] == "academic-paper-research-writer"
    assert "academic paper" in frontmatter["description"]

    prompts = {
        "system.md",
        "research_framing.md",
        "literature_review.md",
        "mechanistic_reasoning.md",
        "equation_derivation.md",
        "evidence_synthesis.md",
        "academic_writing.md",
        "citation_style.md",
        "peer_review_check.md",
    }
    assert prompts == {path.name for path in (SKILL_ROOT / "prompts").glob("*.md")}

    schemas = {
        "input.schema.json",
        "output.schema.json",
        "paper_plan.schema.json",
        "evidence_matrix.schema.json",
        "equation_registry.schema.json",
    }
    assert schemas == {path.name for path in (SKILL_ROOT / "schemas").glob("*.json")}

    examples = {path.name for path in (SKILL_ROOT / "examples").glob("*.md")}
    assert {
        "porous_media_radiolysis_paper.md",
        "uranium_groundwater_migration_paper.md",
        "geochem_anomaly_paper.md",
        "gis_mineral_targeting_paper.md",
    }.issubset(examples)
