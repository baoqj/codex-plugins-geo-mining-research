import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "academic-geochemistry-paper-architect"


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


def test_geochemistry_architect_skill_structure():
    metadata = parse_frontmatter(SKILL / "SKILL.md")
    assert metadata["name"] == "academic-geochemistry-paper-architect"
    assert "geochemistry academic paper architectures" in metadata["description"]
    assert len(list((SKILL / "references").glob("*.md"))) >= 5
    assert len(list((SKILL / "templates").glob("*.md"))) >= 2
    assert len(list((SKILL / "schemas").glob("*.json"))) >= 2
    assert len(list((SKILL / "examples").glob("*.md"))) >= 5
    assert (SKILL / "scripts" / "generate_paper_architecture.py").exists()


def test_geochemistry_architect_schemas_are_valid_json():
    for schema in (SKILL / "schemas").glob("*.json"):
        data = json.loads(schema.read_text(encoding="utf-8"))
        assert data["type"] == "object"


def test_generate_paper_architecture_help():
    result = subprocess.run(
        [sys.executable, str(SKILL / "scripts" / "generate_paper_architecture.py"), "--help"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "usage:" in result.stdout.lower()


def test_generate_paper_architecture_classifies_hydrogeochemistry():
    result = subprocess.run(
        [
            sys.executable,
            str(SKILL / "scripts" / "generate_paper_architecture.py"),
            "--topic",
            "Groundwater uranium migration using PHREEQC speciation and saturation index",
            "--region",
            "Canadian Shield",
            "--available-data",
            "groundwater chemistry",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Primary type: Hydrogeochemistry Paper" in result.stdout
    assert "Required data:\n- water chemistry, charge balance inputs" in result.stdout
    assert "\n- w\n" not in result.stdout
    assert "phreeqc-modeling-skill" in result.stdout
    assert "Research questions:" in result.stdout
    assert "Figure Architecture" in result.stdout
    assert "Machine-Readable Summary" in result.stdout


def test_router_mentions_geochemistry_architect():
    for router in [
        ROOT / "skills" / "research-router-skill" / "SKILL.md",
        ROOT / "skills" / "geomine-research-router-skill" / "SKILL.md",
        ROOT / "skills" / "academic-paper-research-writer" / "SKILL.md",
    ]:
        text = router.read_text(encoding="utf-8")
        assert "academic-geochemistry-paper-architect" in text
