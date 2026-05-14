#!/usr/bin/env python3
"""Validate GeoMine THMC MCP packaging and optional activation config."""

from __future__ import annotations

import json
import sys
from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]
THMC_TOOLS = [
    "list_openmine_projects",
    "get_openmine_project",
    "get_project_aoi",
    "query_water_chemistry_samples",
    "query_lithology_units",
    "query_mineral_assemblages",
    "get_thmc_mesh_catalog",
    "fetch_mesh_or_parameter_field",
    "build_phreeqc_input",
    "run_phreeqc_job",
    "submit_ogs_job",
    "submit_pflotran_job",
    "get_compute_job_status",
    "fetch_compute_job_results",
    "save_thmc_model_version",
    "get_thmc_model_version",
    "list_thmc_model_versions",
    "save_thmc_run_record",
    "get_thmc_run_record",
    "list_thmc_run_records",
]
THMC_DATA_TOOLS = [
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
PFLOTRAN_TOOLS = [
    "validate_input_deck",
    "build_input_deck",
    "build_run_manifest",
    "parse_observation_output",
    "generate_result_summary",
    "save_model_package",
    "get_model_package",
    "list_model_packages",
]


def failures() -> list[str]:
    errors: list[str] = []
    if (ROOT / ".mcp.json").exists():
        errors.append("plugin root .mcp.json must stay absent by default")
    config_path = ROOT / "references" / "geomine-thmc.mcp.example.json"
    try:
        config = json.loads(config_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        return [f"cannot read references/geomine-thmc.mcp.example.json: {exc}"]
    server = config.get("geomine_thmc")
    if not isinstance(server, dict):
        errors.append("THMC MCP config must define geomine_thmc")
        return errors
    if server.get("command") != "uv":
        errors.append("geomine_thmc.command must be uv")
    if server.get("args") != ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-thmc-mcp"]:
        errors.append("geomine_thmc.args mismatch")
    if server.get("enabled") is not False:
        errors.append("geomine_thmc.enabled must be false by default")
    if server.get("required") is not False:
        errors.append("geomine_thmc.required must be false")
    if server.get("enabled_tools") != THMC_TOOLS:
        errors.append("geomine_thmc.enabled_tools mismatch")
    if "OPENMINE_API_TOKEN" not in server.get("env_vars", []):
        errors.append("geomine_thmc.env_vars must include OPENMINE_API_TOKEN")
    if server.get("env", {}).get("GEOMINE_THMC_MODE") != "mock":
        errors.append("geomine_thmc.env.GEOMINE_THMC_MODE must default to mock")

    data_config_path = ROOT / "references" / "geomine-thmc-data.mcp.example.json"
    try:
        data_config = json.loads(data_config_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"cannot read references/geomine-thmc-data.mcp.example.json: {exc}")
        data_server = None
    else:
        data_server = data_config.get("geomine_thmc_data")
        if not isinstance(data_server, dict):
            errors.append("THMC data MCP config must define geomine_thmc_data")
            data_server = None
    if data_server:
        if data_server.get("command") != "uv":
            errors.append("geomine_thmc_data.command must be uv")
        if data_server.get("args") != ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-thmc-data-mcp"]:
            errors.append("geomine_thmc_data.args mismatch")
        if data_server.get("enabled") is not False:
            errors.append("geomine_thmc_data.enabled must be false by default")
        if data_server.get("required") is not False:
            errors.append("geomine_thmc_data.required must be false")
        if data_server.get("enabled_tools") != THMC_DATA_TOOLS:
            errors.append("geomine_thmc_data.enabled_tools mismatch")
        if data_server.get("env", {}).get("GEOMINE_THMC_MODE") != "mock":
            errors.append("geomine_thmc_data.env.GEOMINE_THMC_MODE must default to mock")

    pflotran_config_path = ROOT / "references" / "geomine-pflotran.mcp.example.json"
    try:
        pflotran_config = json.loads(pflotran_config_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001
        errors.append(f"cannot read references/geomine-pflotran.mcp.example.json: {exc}")
        pflotran_server = None
    else:
        pflotran_server = pflotran_config.get("geomine_pflotran")
        if not isinstance(pflotran_server, dict):
            errors.append("PFLOTRAN MCP config must define geomine_pflotran")
            pflotran_server = None
    if pflotran_server:
        if pflotran_server.get("command") != "uv":
            errors.append("geomine_pflotran.command must be uv")
        if pflotran_server.get("args") != ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-pflotran-mcp"]:
            errors.append("geomine_pflotran.args mismatch")
        if pflotran_server.get("enabled") is not False:
            errors.append("geomine_pflotran.enabled must be false by default")
        if pflotran_server.get("required") is not False:
            errors.append("geomine_pflotran.required must be false")
        if pflotran_server.get("enabled_tools") != PFLOTRAN_TOOLS:
            errors.append("geomine_pflotran.enabled_tools mismatch")
        if pflotran_server.get("env", {}).get("GEOMINE_THMC_MODE") != "mock":
            errors.append("geomine_pflotran.env.GEOMINE_THMC_MODE must default to mock")

    mcp_root = ROOT / "mcp" / "geomine-thmc-server"
    for rel in [
        "pyproject.toml",
        "src/geomine_thmc_mcp/server.py",
        "src/geomine_thmc_mcp/data_server.py",
        "src/geomine_thmc_mcp/pflotran_server.py",
        "src/geomine_thmc_mcp/tools/phreeqc_service.py",
        "src/geomine_thmc_mcp/tools/remote_compute.py",
        "src/geomine_thmc_mcp/tools/pflotran_modeling.py",
        "src/geomine_thmc_mcp/tools/model_registry.py",
        "src/geomine_thmc_mcp/tools/run_records.py",
        "src/geomine_thmc_mcp/tools/dgr_data_collection.py",
    ]:
        if not (mcp_root / rel).exists():
            errors.append(f"missing THMC MCP file: {rel}")

    pyproject = tomllib.loads((mcp_root / "pyproject.toml").read_text(encoding="utf-8"))
    if pyproject.get("project", {}).get("scripts", {}).get("geomine-thmc-mcp") != "geomine_thmc_mcp.server:main":
        errors.append("geomine-thmc-mcp script entrypoint mismatch")
    if pyproject.get("project", {}).get("scripts", {}).get("geomine-thmc-data-mcp") != "geomine_thmc_mcp.data_server:main":
        errors.append("geomine-thmc-data-mcp script entrypoint mismatch")
    if pyproject.get("project", {}).get("scripts", {}).get("geomine-pflotran-mcp") != "geomine_thmc_mcp.pflotran_server:main":
        errors.append("geomine-pflotran-mcp script entrypoint mismatch")
    return errors


def main() -> int:
    errors = failures()
    if errors:
        print("GeoMine THMC MCP config validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("GeoMine THMC MCP config validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
