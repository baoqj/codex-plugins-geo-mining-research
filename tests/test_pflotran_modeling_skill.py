import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FAMILY = ROOT / "skills" / "pflotran-modeling"


SUBSKILLS = [
    "pflotran-router-skill",
    "pflotran-conceptual-model-skill",
    "pflotran-input-deck-skill",
    "pflotran-grid-material-skill",
    "pflotran-flow-transport-skill",
    "pflotran-chemistry-skill",
    "pflotran-thc-skill",
    "pflotran-geomechanics-skill",
    "pflotran-run-management-skill",
    "pflotran-output-analysis-skill",
    "pflotran-calibration-validation-skill",
    "pflotran-paper-synthesis-skill",
]


def test_pflotran_family_structure():
    assert FAMILY.exists()
    assert not (ROOT / "skills" / "thmc-modeling" / "pflotran-modeling").exists()
    for subskill in SUBSKILLS:
        assert (FAMILY / subskill / "SKILL.md").exists()


def test_pflotran_templates_and_references_exist():
    required = [
        "README.md",
        "pflotran-input-deck-skill/templates/pflotran-input-deck-skeleton.in",
        "pflotran-input-deck-skill/templates/subsurface-flow-template.in",
        "pflotran-input-deck-skill/templates/reactive-transport-template.in",
        "pflotran-input-deck-skill/templates/thermal-hydrologic-template.in",
        "pflotran-input-deck-skill/templates/chemistry-template.in",
        "pflotran-input-deck-skill/templates/output-template.in",
        "pflotran-grid-material-skill/templates/structured-grid-template.md",
        "pflotran-grid-material-skill/templates/material-property-table-template.csv",
        "pflotran-grid-material-skill/templates/region-definition-template.md",
        "pflotran-flow-transport-skill/references/flow-transport-mode-selection.md",
        "pflotran-flow-transport-skill/references/boundary-condition-patterns.md",
        "pflotran-flow-transport-skill/references/transport-configuration-rules.md",
        "pflotran-chemistry-skill/references/chemistry-block-rules.md",
        "pflotran-chemistry-skill/references/thermodynamic-database-rules.md",
        "pflotran-chemistry-skill/references/mineral-reaction-patterns.md",
        "pflotran-chemistry-skill/references/sorption-ion-exchange-patterns.md",
        "pflotran-chemistry-skill/references/uranium-reactive-transport-pattern.md",
        "pflotran-chemistry-skill/references/acid-mine-drainage-pattern.md",
        "pflotran-chemistry-skill/references/tailings-seepage-pattern.md",
        "pflotran-thc-skill/references/thermal-hydrologic-chemical-coupling.md",
        "pflotran-thc-skill/references/temperature-dependent-chemistry.md",
        "pflotran-thc-skill/references/heat-source-boundary-patterns.md",
        "pflotran-geomechanics-skill/references/geomechanics-scope-and-limits.md",
        "pflotran-geomechanics-skill/references/porosity-permeability-feedback.md",
        "pflotran-geomechanics-skill/references/biot-coupling-notes.md",
        "pflotran-paper-synthesis-skill/templates/pflotran-modeling-package-template.md",
        "pflotran-paper-synthesis-skill/templates/methods-section-template.md",
        "pflotran-paper-synthesis-skill/templates/results-section-template.md",
        "pflotran-paper-synthesis-skill/templates/model-limitations-template.md",
        "pflotran-paper-synthesis-skill/templates/machine-readable-model-manifest-schema.json",
        "examples/pflotran-tailings-seepage.md",
        "examples/pflotran-uranium-reactive-transport.md",
        "examples/pflotran-thc-geothermal-groundwater.md",
    ]
    missing = [rel for rel in required if not (FAMILY / rel).exists()]
    assert missing == []


def test_pflotran_scripts_run_help():
    script_dirs = [
        FAMILY / "pflotran-run-management-skill" / "scripts",
        FAMILY / "pflotran-output-analysis-skill" / "scripts",
    ]
    for script_dir in script_dirs:
        for script in script_dir.glob("*.py"):
            result = subprocess.run(
                [sys.executable, str(script), "--help"],
                text=True,
                capture_output=True,
                check=False,
            )
            assert result.returncode == 0, result.stdout + result.stderr
            assert "usage:" in result.stdout


def test_pflotran_package_template_contract():
    text = (FAMILY / "pflotran-paper-synthesis-skill" / "templates" / "pflotran-modeling-package-template.md").read_text()
    for number in range(1, 27):
        assert f"## {number}." in text
    assert "Machine-readable Model Manifest" in text
    assert "Future MCP / Remote Compute Extension" in text


def test_pflotran_router_rules_exist():
    geomine = (ROOT / "skills" / "geomine-research-router-skill" / "SKILL.md").read_text()
    thmc = (ROOT / "skills" / "thmc-modeling" / "thmc-groundwater-router-skill" / "SKILL.md").read_text()
    assert "PFLOTRAN Modeling Integration" in geomine
    assert "pflotran-router-skill" in geomine
    assert "Handoff To PFLOTRAN" in thmc
    assert "not a child skill under THMC" in thmc
