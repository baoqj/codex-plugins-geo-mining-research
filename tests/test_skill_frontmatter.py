from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def parse_frontmatter(path: Path) -> dict[str, str]:
    lines = path.read_text().splitlines()
    assert lines[0] == "---"
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line == "---":
            return data
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip()
    raise AssertionError("frontmatter not closed")


def test_all_skills_have_name_and_description():
    skill_dirs = sorted((ROOT / "skills").glob("*-skill"))
    assert len(skill_dirs) == 9
    for skill_dir in skill_dirs:
        data = parse_frontmatter(skill_dir / "SKILL.md")
        assert data["name"] == skill_dir.name
        assert data["description"]
