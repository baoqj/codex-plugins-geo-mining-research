import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def test_manifest_required_fields():
    manifest = json.loads((ROOT / ".codex-plugin/plugin.json").read_text())
    assert manifest["name"] == "geo-mining-research"
    assert manifest["version"] == "0.2.0"
    assert "skills" not in manifest
    assert "mcpServers" not in manifest
    assert manifest["interface"]["displayName"] == "GeoMine Research"


def test_no_root_mcp_config_by_default():
    assert not (ROOT / ".mcp.json").exists()


def test_mcp_example_config_required_fields():
    config = json.loads((ROOT / "references" / "geomine.mcp.example.json").read_text())
    assert set(config) == {"geomine"}
    geomine = config["geomine"]
    assert geomine["command"] == "uv"
    assert "--no-project" in geomine["args"]
    assert geomine["enabled"] is False
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


def test_thmc_data_mcp_example_config_required_fields():
    config = json.loads((ROOT / "references" / "geomine-thmc-data.mcp.example.json").read_text())
    assert set(config) == {"geomine_thmc_data"}
    server = config["geomine_thmc_data"]
    assert server["command"] == "uv"
    assert server["args"] == ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-thmc-data-mcp"]
    assert server["enabled"] is False
    assert server["required"] is False
    assert server["enabled_tools"] == [
        "list_dgr_data_campaigns",
        "get_dgr_data_campaign",
        "register_dgr_borehole",
        "ingest_dgr_sensor_timeseries",
        "ingest_dgr_water_sample",
        "ingest_dgr_rock_core_measurement",
        "ingest_dgr_packer_test",
        "ingest_dgr_in_situ_stress",
        "validate_dgr_thmc_dataset",
        "build_dgr_calibration_dataset",
        "save_dgr_data_package",
        "get_dgr_data_package",
        "list_dgr_data_packages",
    ]


def test_pflotran_mcp_example_config_required_fields():
    config = json.loads((ROOT / "references" / "geomine-pflotran.mcp.example.json").read_text())
    assert set(config) == {"geomine_pflotran"}
    server = config["geomine_pflotran"]
    assert server["command"] == "uv"
    assert server["args"] == ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-pflotran-mcp"]
    assert server["enabled"] is False
    assert server["required"] is False
    assert server["enabled_tools"] == [
        "validate_input_deck",
        "build_input_deck",
        "build_run_manifest",
        "parse_observation_output",
        "generate_result_summary",
        "save_model_package",
        "get_model_package",
        "list_model_packages",
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
