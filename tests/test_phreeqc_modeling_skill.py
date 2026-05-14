import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "phreeqc-modeling-skill"


def test_phreeqc_skill_required_files_exist():
    required = [
        "SKILL.md",
        "references/phreeqc-keywords.md",
        "references/phreeqc-database-selection.md",
        "references/groundwater-chemistry-data-schema.md",
        "references/uranium-radionuclide-reaction-patterns.md",
        "references/acid-mine-drainage-reaction-patterns.md",
        "references/tailings-seepage-reaction-patterns.md",
        "references/phreeqc-paper-methods-writing.md",
        "templates/phreeqc-modeling-package-template.md",
        "templates/solution-template.phr",
        "templates/equilibrium-phases-template.phr",
        "templates/kinetics-template.phr",
        "templates/surface-complexation-template.phr",
        "templates/exchange-template.phr",
        "templates/transport-1d-template.phr",
        "templates/selected-output-template.phr",
        "templates/paper-methods-template.md",
        "scripts/validate_water_chemistry_table.py",
        "scripts/build_solution_block.py",
        "scripts/generate_selected_output.py",
        "scripts/parse_selected_output.py",
        "scripts/make_phreeqc_run_manifest.py",
        "examples/phreeqc-uranium-groundwater.md",
        "examples/phreeqc-acid-mine-drainage.md",
        "examples/phreeqc-tailings-seepage.md",
    ]
    missing = [rel for rel in required if not (SKILL / rel).exists()]
    assert missing == []


def test_phreeqc_scripts_run_help():
    for script in (SKILL / "scripts").glob("*.py"):
        result = subprocess.run(
            [sys.executable, str(script), "--help"],
            text=True,
            capture_output=True,
            check=False,
        )
        assert result.returncode == 0, result.stdout + result.stderr
        assert "usage:" in result.stdout


def test_phreeqc_modeling_package_template_contract():
    text = (SKILL / "templates" / "phreeqc-modeling-package-template.md").read_text()
    required_sections = [
        "Research Objective",
        "Model Type Classification",
        "Input Data Audit",
        "Database Recommendation",
        "PHREEQC Keyword Plan",
        "Generated Input",
        "Run Instructions",
        "Selected Output Design",
        "Interpretation Plan",
        "Paper Methods Draft",
        "Limitations And Uncertainty",
    ]
    for section in required_sections:
        assert section in text


def test_phreeqc_router_mentions_new_skill():
    router = (ROOT / "skills" / "thmc-modeling" / "thmc-groundwater-router-skill" / "SKILL.md").read_text()
    assert "phreeqc-modeling-skill" in router
    assert "PHREEQC Routing Rules" in router
