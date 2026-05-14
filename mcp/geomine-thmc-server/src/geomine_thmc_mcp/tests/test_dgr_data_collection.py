from __future__ import annotations

from geomine_thmc_mcp.storage import THMCStorage
from geomine_thmc_mcp.tools import (
    build_dgr_calibration_dataset,
    ingest_dgr_in_situ_stress,
    ingest_dgr_packer_test,
    ingest_dgr_rock_core_measurement,
    ingest_dgr_sensor_timeseries,
    ingest_dgr_water_sample,
    list_dgr_data_campaigns,
    register_dgr_borehole,
    save_dgr_data_package,
    validate_dgr_thmc_dataset,
)


PROJECT_ID = "om-prj-dgr-001"
CAMPAIGN_ID = "dgr-campaign-revell-mock-001"
REQUIRED_KEYS = {"ok", "mode", "tool", "query", "results", "assets", "provenance", "warnings", "errors"}


def assert_response(payload: dict, tool: str) -> None:
    assert REQUIRED_KEYS.issubset(payload)
    assert payload["ok"] is True
    assert payload["mode"] == "mock"
    assert payload["tool"] == tool


def test_dgr_data_collection_round_trip(tmp_path):
    storage = THMCStorage(cache_dir=tmp_path, mode="mock")
    assert_response(list_dgr_data_campaigns(project_id=PROJECT_ID, storage=storage), "list_dgr_data_campaigns")
    register_dgr_borehole(
        PROJECT_ID,
        "DGR-BH-001",
        {"x": -93.6, "y": 49.7},
        950.0,
        campaign_id=CAMPAIGN_ID,
        storage=storage,
    )
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
    ingest_dgr_water_sample(
        PROJECT_ID,
        CAMPAIGN_ID,
        "DGR-W-001",
        "DGR-BH-001",
        640.0,
        "2026-01-02",
        {"pH": 7.8},
        {"Cl": {"value": 12000, "unit": "mg/L"}},
        storage=storage,
    )
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
    ingest_dgr_packer_test(
        PROJECT_ID,
        CAMPAIGN_ID,
        "DGR-BH-001",
        {"from_m": 610.0, "to_m": 630.0},
        hydraulic_conductivity_m_s=1e-12,
        storage=storage,
    )
    ingest_dgr_in_situ_stress(
        PROJECT_ID,
        CAMPAIGN_ID,
        "DGR-BH-001",
        700.0,
        "hydraulic_fracturing",
        {"sigma_H": 24.0, "sigma_h": 14.0, "sigma_v": 18.0},
        storage=storage,
    )
    validation = validate_dgr_thmc_dataset(PROJECT_ID, CAMPAIGN_ID, storage=storage)
    assert_response(validation, "validate_dgr_thmc_dataset")
    assert validation["results"][0]["ready_for_calibration"] is True
    calibration = build_dgr_calibration_dataset(PROJECT_ID, CAMPAIGN_ID, storage=storage)
    assert_response(calibration, "build_dgr_calibration_dataset")
    assert calibration["assets"][0]["record_count"] >= 5
    package = save_dgr_data_package(
        PROJECT_ID,
        "mock-package",
        campaign_id=CAMPAIGN_ID,
        dataset_ids=calibration["assets"][0]["record_ids"],
        storage=storage,
    )
    assert_response(package, "save_dgr_data_package")
