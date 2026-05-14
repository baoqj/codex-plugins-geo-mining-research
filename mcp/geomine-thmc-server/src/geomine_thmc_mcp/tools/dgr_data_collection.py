"""DGR-focused THMC field data acquisition MCP tools."""

from __future__ import annotations

from typing import Any

from ..provenance import provenance
from ..schemas import tool_response
from ..storage import THMCStorage, get_default_storage


PROCESS_RECORD_TYPES = {
    "T": {"sensor_timeseries", "thermal_property", "temperature_log"},
    "H": {"packer_test", "hydraulic_head", "sensor_timeseries", "water_sample"},
    "M": {"rock_core_measurement", "in_situ_stress", "microseismic_event", "deformation"},
    "C": {"water_sample", "isotope_sample", "rock_core_measurement"},
}


def _store(storage: THMCStorage | None) -> THMCStorage:
    return storage or get_default_storage()


def _acquisition_warnings(extra: list[str] | None = None) -> list[str]:
    return [
        "DGR data acquisition MCP is mock/local by default; do not treat records as field-verified unless provenance and QA/QC prove it.",
        "Real DGR datasets require chain-of-custody, instrument calibration, lab certificates, depth datum control, and professional review.",
    ] + (extra or [])


def list_dgr_data_campaigns(
    project_id: str | None = None,
    site_type: str | None = "deep_geological_repository",
    status: str | None = None,
    limit: int = 20,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    query = {"project_id": project_id, "site_type": site_type, "status": status, "limit": limit}
    return tool_response(
        tool="list_dgr_data_campaigns",
        query=query,
        mode="mock",
        results=store.list_dgr_campaigns(project_id=project_id, site_type=site_type, status=status, limit=limit),
        provenance=provenance("DGR THMC data acquisition registry", mode="mock"),
        warnings=_acquisition_warnings(["Campaigns are planning/mock records unless imported from a validated field database."]),
    )


def get_dgr_data_campaign(campaign_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = _store(storage)
    campaign = store.get_dgr_campaign(campaign_id)
    query = {"campaign_id": campaign_id}
    if not campaign:
        return tool_response(
            tool="get_dgr_data_campaign",
            query=query,
            mode="error",
            ok=False,
            provenance=provenance("DGR THMC data acquisition registry", mode="mock"),
            errors=[
                {
                    "code": "DGR_CAMPAIGN_NOT_FOUND",
                    "message": "DGR campaign was not found in the local/mock registry.",
                    "retryable": False,
                    "suggested_action": "Use list_dgr_data_campaigns to inspect available campaigns.",
                }
            ],
        )
    return tool_response(
        tool="get_dgr_data_campaign",
        query=query,
        mode="mock",
        results=[campaign],
        provenance=provenance("DGR THMC data acquisition registry", mode="mock"),
        warnings=_acquisition_warnings(),
    )


def register_dgr_borehole(
    project_id: str,
    borehole_id: str,
    collar: dict[str, Any],
    depth_m: float,
    campaign_id: str | None = None,
    crs: str = "EPSG:4326",
    metadata: dict[str, Any] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    record = store.save_dgr_record(
        "borehole",
        {
            "project_id": project_id,
            "campaign_id": campaign_id,
            "borehole_id": borehole_id,
            "depth_m": depth_m,
            "measurement_type": "borehole_metadata",
            "values": {"collar": collar, "crs": crs, "metadata": metadata or {}},
            "units": {"depth": "m"},
            "qaqc_flags": ["requires_survey_control", "requires_deviation_log"],
        },
    )
    return tool_response(
        tool="register_dgr_borehole",
        query={"project_id": project_id, "campaign_id": campaign_id, "borehole_id": borehole_id},
        mode="mock",
        results=[record],
        provenance=provenance("DGR borehole acquisition registry", mode="mock", crs=crs),
        warnings=_acquisition_warnings(["Borehole collar and deviation must be surveyed before calibration use."]),
    )


def ingest_dgr_sensor_timeseries(
    project_id: str,
    campaign_id: str,
    sensor_type: str,
    records: list[dict[str, Any]],
    borehole_id: str | None = None,
    depth_m: float | None = None,
    units: dict[str, str] | None = None,
    qaqc_flags: list[str] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    record = store.save_dgr_record(
        "sensor_timeseries",
        {
            "project_id": project_id,
            "campaign_id": campaign_id,
            "borehole_id": borehole_id,
            "depth_m": depth_m,
            "measurement_type": sensor_type,
            "values": {"records": records, "record_count": len(records)},
            "units": units or {},
            "qaqc_flags": qaqc_flags or ["requires_sensor_calibration", "requires_clock_sync_check"],
        },
    )
    return tool_response(
        tool="ingest_dgr_sensor_timeseries",
        query={"project_id": project_id, "campaign_id": campaign_id, "sensor_type": sensor_type, "record_count": len(records)},
        mode="mock",
        results=[record],
        provenance=provenance("DGR sensor data ingestion", mode="mock", units=units),
        warnings=_acquisition_warnings(["Time-series records are accepted structurally; no drift correction or outlier filtering has been applied."]),
    )


def ingest_dgr_water_sample(
    project_id: str,
    campaign_id: str,
    sample_id: str,
    borehole_id: str,
    depth_m: float,
    sample_date: str,
    field_parameters: dict[str, Any],
    analytes: dict[str, Any],
    units: dict[str, str] | None = None,
    qaqc_flags: list[str] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    record = store.save_dgr_record(
        "water_sample",
        {
            "project_id": project_id,
            "campaign_id": campaign_id,
            "borehole_id": borehole_id,
            "depth_m": depth_m,
            "measurement_type": "groundwater_chemistry",
            "values": {
                "sample_id": sample_id,
                "sample_date": sample_date,
                "field_parameters": field_parameters,
                "analytes": analytes,
            },
            "units": units or {"major_ions": "mg/L", "trace_metals": "ug/L", "isotopes": "reported_by_lab"},
            "qaqc_flags": qaqc_flags or ["requires_charge_balance", "requires_blank_duplicate_reference"],
        },
    )
    return tool_response(
        tool="ingest_dgr_water_sample",
        query={"project_id": project_id, "campaign_id": campaign_id, "sample_id": sample_id, "borehole_id": borehole_id},
        mode="mock",
        results=[record],
        provenance=provenance("DGR groundwater chemistry ingestion", mode="mock", units=record["units"]),
        warnings=_acquisition_warnings(["Chemistry record is not PHREEQC-ready until charge balance, redox handling, and species/database mapping are checked."]),
    )


def ingest_dgr_rock_core_measurement(
    project_id: str,
    campaign_id: str,
    core_id: str,
    borehole_id: str,
    depth_interval: dict[str, float],
    measurement_type: str,
    values: dict[str, Any],
    units: dict[str, str],
    lab_method: str | None = None,
    qaqc_flags: list[str] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    record = store.save_dgr_record(
        "rock_core_measurement",
        {
            "project_id": project_id,
            "campaign_id": campaign_id,
            "borehole_id": borehole_id,
            "depth_interval": depth_interval,
            "measurement_type": measurement_type,
            "values": {"core_id": core_id, "lab_method": lab_method, **values},
            "units": units,
            "qaqc_flags": qaqc_flags or ["requires_lab_certificate", "requires_depth_correlation"],
        },
    )
    return tool_response(
        tool="ingest_dgr_rock_core_measurement",
        query={"project_id": project_id, "campaign_id": campaign_id, "core_id": core_id, "measurement_type": measurement_type},
        mode="mock",
        results=[record],
        provenance=provenance("DGR rock core measurement ingestion", mode="mock", units=units),
        warnings=_acquisition_warnings(),
    )


def ingest_dgr_packer_test(
    project_id: str,
    campaign_id: str,
    borehole_id: str,
    interval_m: dict[str, float],
    hydraulic_conductivity_m_s: float | None = None,
    transmissivity_m2_s: float | None = None,
    pressure_observations: list[dict[str, Any]] | None = None,
    qaqc_flags: list[str] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    record = store.save_dgr_record(
        "packer_test",
        {
            "project_id": project_id,
            "campaign_id": campaign_id,
            "borehole_id": borehole_id,
            "depth_interval": interval_m,
            "measurement_type": "packer_hydraulic_test",
            "values": {
                "hydraulic_conductivity_m_s": hydraulic_conductivity_m_s,
                "transmissivity_m2_s": transmissivity_m2_s,
                "pressure_observations": pressure_observations or [],
            },
            "units": {"hydraulic_conductivity": "m/s", "transmissivity": "m2/s", "pressure": "kPa"},
            "qaqc_flags": qaqc_flags or ["requires_interval_isolation_check", "requires_pressure_recovery_fit"],
        },
    )
    return tool_response(
        tool="ingest_dgr_packer_test",
        query={"project_id": project_id, "campaign_id": campaign_id, "borehole_id": borehole_id, "interval_m": interval_m},
        mode="mock",
        results=[record],
        provenance=provenance("DGR packer test ingestion", mode="mock", units=record["units"]),
        warnings=_acquisition_warnings(["Hydraulic parameters are not calibrated model values until test interpretation is documented."]),
    )


def ingest_dgr_in_situ_stress(
    project_id: str,
    campaign_id: str,
    borehole_id: str,
    depth_m: float,
    method: str,
    stress_tensor: dict[str, Any],
    units: str = "MPa",
    qaqc_flags: list[str] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    record = store.save_dgr_record(
        "in_situ_stress",
        {
            "project_id": project_id,
            "campaign_id": campaign_id,
            "borehole_id": borehole_id,
            "depth_m": depth_m,
            "measurement_type": "in_situ_stress",
            "method": method,
            "values": {"stress_tensor": stress_tensor},
            "units": {"stress": units},
            "qaqc_flags": qaqc_flags or ["requires_method_report", "requires_orientation_reference"],
        },
    )
    return tool_response(
        tool="ingest_dgr_in_situ_stress",
        query={"project_id": project_id, "campaign_id": campaign_id, "borehole_id": borehole_id, "depth_m": depth_m, "method": method},
        mode="mock",
        results=[record],
        provenance=provenance("DGR in-situ stress ingestion", mode="mock", units={"stress": units}),
        warnings=_acquisition_warnings(),
    )


def validate_dgr_thmc_dataset(
    project_id: str,
    campaign_id: str | None = None,
    dataset_ids: list[str] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    records = store.list_dgr_records(project_id=project_id, campaign_id=campaign_id)
    if dataset_ids:
        wanted = set(dataset_ids)
        records = [item for item in records if item["record_id"] in wanted]
    present_types = {item["record_type"] for item in records}
    coverage = {}
    gaps = []
    for process, required_types in PROCESS_RECORD_TYPES.items():
        matched = sorted(present_types.intersection(required_types))
        coverage[process] = {
            "covered": bool(matched),
            "matched_record_types": matched,
            "candidate_required_record_types": sorted(required_types),
        }
        if not matched:
            gaps.append({"process": process, "missing_record_types": sorted(required_types)})
    validation = {
        "project_id": project_id,
        "campaign_id": campaign_id,
        "record_count": len(records),
        "record_types": sorted(present_types),
        "coverage": coverage,
        "data_gaps": gaps,
        "ready_for_calibration": len(gaps) == 0 and len(records) > 0,
    }
    return tool_response(
        tool="validate_dgr_thmc_dataset",
        query={"project_id": project_id, "campaign_id": campaign_id, "dataset_ids": dataset_ids},
        mode="mock",
        results=[validation],
        provenance=provenance("DGR THMC dataset validation", mode="mock"),
        warnings=_acquisition_warnings(["Validation checks coverage only; it does not certify scientific adequacy or regulatory acceptability."]),
    )


def build_dgr_calibration_dataset(
    project_id: str,
    campaign_id: str | None = None,
    target_processes: list[str] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    records = store.list_dgr_records(project_id=project_id, campaign_id=campaign_id)
    processes = target_processes or ["T", "H", "M", "C"]
    selected_types = set().union(*(PROCESS_RECORD_TYPES.get(process, set()) for process in processes))
    selected = [item for item in records if item["record_type"] in selected_types or item["record_type"] == "borehole"]
    asset = {
        "asset_id": f"dgr-calibration-dataset-{project_id}-{campaign_id or 'all'}",
        "asset_type": "dgr_calibration_dataset",
        "format": "json",
        "storage": "inline",
        "record_count": len(selected),
        "record_ids": [item["record_id"] for item in selected],
        "target_processes": processes,
    }
    return tool_response(
        tool="build_dgr_calibration_dataset",
        query={"project_id": project_id, "campaign_id": campaign_id, "target_processes": target_processes},
        mode="mock",
        results=[{"record_count": len(selected), "target_processes": processes}],
        assets=[asset],
        provenance=provenance("DGR calibration dataset builder", mode="mock"),
        warnings=_acquisition_warnings(["Calibration dataset is a structured package of records, not a calibrated THMC model."]),
    )


def save_dgr_data_package(
    project_id: str,
    package_label: str,
    campaign_id: str | None = None,
    dataset_ids: list[str] | None = None,
    package_spec: dict[str, Any] | None = None,
    notes: str = "",
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    package = store.save_dgr_data_package(
        {
            "project_id": project_id,
            "campaign_id": campaign_id,
            "package_label": package_label,
            "dataset_ids": dataset_ids or [],
            "package_spec": package_spec or {},
            "notes": notes,
        }
    )
    return tool_response(
        tool="save_dgr_data_package",
        query={"project_id": project_id, "campaign_id": campaign_id, "package_label": package_label},
        mode="mock",
        results=[package],
        provenance=provenance("DGR data package registry", mode="mock"),
        warnings=_acquisition_warnings(["Package saved to local/mock registry; not synced to a field-data repository."]),
    )


def get_dgr_data_package(package_id: str, storage: THMCStorage | None = None) -> dict[str, Any]:
    store = _store(storage)
    package = store.get_dgr_data_package(package_id)
    query = {"package_id": package_id}
    if not package:
        return tool_response(
            tool="get_dgr_data_package",
            query=query,
            mode="error",
            ok=False,
            provenance=provenance("DGR data package registry", mode="mock"),
            errors=[
                {
                    "code": "DGR_DATA_PACKAGE_NOT_FOUND",
                    "message": "DGR data package was not found in the local/mock registry.",
                    "retryable": False,
                    "suggested_action": "Use list_dgr_data_packages or save a data package first.",
                }
            ],
        )
    return tool_response(
        tool="get_dgr_data_package",
        query=query,
        mode="mock",
        results=[package],
        provenance=provenance("DGR data package registry", mode="mock"),
        warnings=_acquisition_warnings(),
    )


def list_dgr_data_packages(
    project_id: str | None = None,
    campaign_id: str | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = _store(storage)
    return tool_response(
        tool="list_dgr_data_packages",
        query={"project_id": project_id, "campaign_id": campaign_id},
        mode="mock",
        results=store.list_dgr_data_packages(project_id=project_id, campaign_id=campaign_id),
        provenance=provenance("DGR data package registry", mode="mock"),
        warnings=_acquisition_warnings(),
    )
