#!/usr/bin/env python3
"""Smoke test GeoMine THMC DGR data acquisition tools without an MCP client."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THMC_SRC = ROOT / "mcp" / "geomine-thmc-server" / "src"
sys.path.insert(0, str(THMC_SRC))

from geomine_thmc_mcp.storage import THMCStorage  # noqa: E402
from geomine_thmc_mcp.tools import (  # noqa: E402
    build_dgr_calibration_dataset,
    get_dgr_data_campaign,
    get_dgr_data_package,
    ingest_dgr_in_situ_stress,
    ingest_dgr_packer_test,
    ingest_dgr_rock_core_measurement,
    ingest_dgr_sensor_timeseries,
    ingest_dgr_water_sample,
    list_dgr_data_campaigns,
    list_dgr_data_packages,
    register_dgr_borehole,
    save_dgr_data_package,
    validate_dgr_thmc_dataset,
)


PROJECT_ID = "om-prj-dgr-001"
CAMPAIGN_ID = "dgr-campaign-revell-mock-001"
REQUIRED_KEYS = {"ok", "mode", "tool", "query", "results", "assets", "provenance", "warnings", "errors"}


def assert_response(payload: dict, expected_tool: str) -> None:
    missing = REQUIRED_KEYS.difference(payload)
    if missing:
        raise AssertionError(f"{expected_tool} missing keys: {sorted(missing)}")
    if payload["tool"] != expected_tool:
        raise AssertionError(f"{expected_tool} reported tool={payload['tool']}")
    if payload["mode"] != "mock":
        raise AssertionError(f"{expected_tool} should run in mock mode during smoke test")
    if not payload["ok"]:
        raise AssertionError(f"{expected_tool} failed unexpectedly: {payload['errors']}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="geomine-thmc-data-") as tmp:
        storage = THMCStorage(cache_dir=Path(tmp), mode="mock")
        responses: list[dict] = []
        responses.append(list_dgr_data_campaigns(project_id=PROJECT_ID, storage=storage))
        responses.append(get_dgr_data_campaign(CAMPAIGN_ID, storage=storage))
        responses.append(
            register_dgr_borehole(
                PROJECT_ID,
                "DGR-BH-001",
                {"x": -93.6, "y": 49.7, "z_m": 381.0},
                950.0,
                campaign_id=CAMPAIGN_ID,
                storage=storage,
            )
        )
        responses.append(
            ingest_dgr_sensor_timeseries(
                PROJECT_ID,
                CAMPAIGN_ID,
                "temperature",
                [{"time": "2026-01-01T00:00:00Z", "value": 18.4}],
                borehole_id="DGR-BH-001",
                depth_m=500.0,
                units={"temperature": "degC"},
                storage=storage,
            )
        )
        responses.append(
            ingest_dgr_water_sample(
                PROJECT_ID,
                CAMPAIGN_ID,
                "DGR-W-001",
                "DGR-BH-001",
                640.0,
                "2026-01-02",
                {"pH": 7.8, "Eh_mV": -120},
                {"Cl": {"value": 12000, "unit": "mg/L"}, "D2H": {"value": -110, "unit": "permil"}},
                storage=storage,
            )
        )
        responses.append(
            ingest_dgr_rock_core_measurement(
                PROJECT_ID,
                CAMPAIGN_ID,
                "CORE-001",
                "DGR-BH-001",
                {"from_m": 500.0, "to_m": 501.0},
                "thermal_conductivity",
                {"thermal_conductivity": 2.6},
                {"thermal_conductivity": "W/m/K"},
                storage=storage,
            )
        )
        responses.append(
            ingest_dgr_packer_test(
                PROJECT_ID,
                CAMPAIGN_ID,
                "DGR-BH-001",
                {"from_m": 610.0, "to_m": 630.0},
                hydraulic_conductivity_m_s=1e-12,
                storage=storage,
            )
        )
        responses.append(
            ingest_dgr_in_situ_stress(
                PROJECT_ID,
                CAMPAIGN_ID,
                "DGR-BH-001",
                700.0,
                "hydraulic_fracturing",
                {"sigma_H": 24.0, "sigma_h": 14.0, "sigma_v": 18.0},
                storage=storage,
            )
        )
        responses.append(validate_dgr_thmc_dataset(PROJECT_ID, CAMPAIGN_ID, storage=storage))
        responses.append(build_dgr_calibration_dataset(PROJECT_ID, CAMPAIGN_ID, storage=storage))
        record_ids = [item["record_id"] for item in storage.list_dgr_records(project_id=PROJECT_ID, campaign_id=CAMPAIGN_ID)]
        package = save_dgr_data_package(
            PROJECT_ID,
            "mock-dgr-thmc-calibration-v0",
            campaign_id=CAMPAIGN_ID,
            dataset_ids=record_ids,
            package_spec={"target_processes": ["T", "H", "M", "C"], "use": "calibration_design"},
            storage=storage,
        )
        package_id = package["results"][0]["package_id"]
        responses.append(package)
        responses.append(get_dgr_data_package(package_id, storage=storage))
        responses.append(list_dgr_data_packages(PROJECT_ID, CAMPAIGN_ID, storage=storage))

        for response in responses:
            assert_response(response, response["tool"])

        print(json.dumps({"ok": True, "tool_count": len({item["tool"] for item in responses}), "responses": len(responses)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
