import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_manifest_required_fields():
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    assert manifest["name"] == "geo-mining-research"
    assert manifest["version"] == "0.2.0"
    assert manifest["skills"] == "./skills/"
    assert manifest["mcpServers"] == "./.mcp.json"
    assert manifest["interface"]["displayName"] == "GeoMine Research"


def test_mcp_config_required_fields():
    config = json.loads((ROOT / ".mcp.json").read_text())
    assert set(config) == {"geomine"}
    geomine = config["geomine"]
    assert geomine["command"] == "uv"
    assert "--no-project" in geomine["args"]
    assert geomine["enabled"] is True
    assert geomine["required"] is False
    assert geomine["enabled_tools"] == [
        "normalize_aoi",
        "search_canada_geodata",
        "search_cdogs_surveys",
        "search_bc_minfile",
        "search_ontario_omi",
        "search_saskatchewan_mineral_data",
        "fetch_dataset_metadata",
        "summarize_dataset_provenance",
        "query_claim_neighbors",
        "calculate_infrastructure_distance",
    ]


def test_validate_plugin_script_passes():
    result = subprocess.run(
        [sys.executable, "scripts/validate_plugin.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
