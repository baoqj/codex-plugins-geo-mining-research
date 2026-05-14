import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "figure-generation" / "academic-figure-package-skill"
SCRIPTS = SKILL / "scripts"


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


def test_figure_package_skill_structure():
    metadata = parse_frontmatter(SKILL / "SKILL.md")
    assert metadata["name"] == "academic-figure-package-skill"
    assert "publication-ready academic figure packages" in metadata["description"]
    assert len(list((SKILL / "references").glob("*.md"))) >= 10
    assert len(list((SKILL / "templates").glob("*"))) >= 8
    assert len(list((SKILL / "scripts").glob("*.py"))) >= 7
    assert len(list((SKILL / "examples").glob("*.md"))) >= 4


def test_figure_package_scripts_support_help():
    for script in SCRIPTS.glob("*.py"):
        result = subprocess.run(
            [sys.executable, str(script), "--help"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, script.name
        assert "usage:" in result.stdout.lower()


def test_figure_package_examples_validate():
    validator = SCRIPTS / "validate_figure_package.py"
    for example in (SKILL / "examples").glob("*.md"):
        result = subprocess.run(
            [sys.executable, str(validator), str(example), "--json"],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        report = json.loads(result.stdout)
        assert report["valid"] is True


def test_build_manifest_and_mermaid_scaffold(tmp_path):
    builder = SCRIPTS / "build_figure_manifest.py"
    example = SKILL / "examples" / "geomine-ai-workflow-figure-package.md"
    output = tmp_path / "manifest.json"
    result = subprocess.run(
        [sys.executable, str(builder), str(example), "--output", str(output)],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    manifest = json.loads(output.read_text(encoding="utf-8"))
    assert len(manifest["figure_package"]["figures"]) == 4

    mermaid = subprocess.run(
        [
            sys.executable,
            str(SCRIPTS / "generate_mermaid_from_spec.py"),
            "--title",
            "GeoMine Workflow",
            "--nodes",
            "Prompt,Router,Evidence,Synthesis",
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert mermaid.returncode == 0
    assert "flowchart LR" in mermaid.stdout
