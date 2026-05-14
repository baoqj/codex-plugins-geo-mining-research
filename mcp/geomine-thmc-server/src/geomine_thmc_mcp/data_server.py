"""GeoMine THMC DGR field-data acquisition MCP server entrypoint."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from .tools import (
    build_dgr_calibration_dataset as build_dgr_calibration_dataset_tool,
    get_dgr_data_campaign as get_dgr_data_campaign_tool,
    get_dgr_data_package as get_dgr_data_package_tool,
    ingest_dgr_in_situ_stress as ingest_dgr_in_situ_stress_tool,
    ingest_dgr_packer_test as ingest_dgr_packer_test_tool,
    ingest_dgr_rock_core_measurement as ingest_dgr_rock_core_measurement_tool,
    ingest_dgr_sensor_timeseries as ingest_dgr_sensor_timeseries_tool,
    ingest_dgr_water_sample as ingest_dgr_water_sample_tool,
    list_dgr_data_campaigns as list_dgr_data_campaigns_tool,
    list_dgr_data_packages as list_dgr_data_packages_tool,
    register_dgr_borehole as register_dgr_borehole_tool,
    save_dgr_data_package as save_dgr_data_package_tool,
    validate_dgr_thmc_dataset as validate_dgr_thmc_dataset_tool,
)


mcp = FastMCP("geomine_thmc_data")


@mcp.tool()
def list_dgr_data_campaigns(
    project_id: str | None = None,
    site_type: str | None = "deep_geological_repository",
    status: str | None = None,
    limit: int = 20,
) -> dict[str, Any]:
    """List DGR THMC field-data acquisition campaigns."""
    return list_dgr_data_campaigns_tool(project_id=project_id, site_type=site_type, status=status, limit=limit)


@mcp.tool()
def get_dgr_data_campaign(campaign_id: str) -> dict[str, Any]:
    """Get one DGR THMC field-data acquisition campaign."""
    return get_dgr_data_campaign_tool(campaign_id=campaign_id)


@mcp.tool()
def register_dgr_borehole(
    project_id: str,
    borehole_id: str,
    collar: dict[str, Any],
    depth_m: float,
    campaign_id: str | None = None,
    crs: str = "EPSG:4326",
    metadata: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Register borehole collar/depth metadata for DGR THMC field data."""
    return register_dgr_borehole_tool(
        project_id=project_id,
        borehole_id=borehole_id,
        collar=collar,
        depth_m=depth_m,
        campaign_id=campaign_id,
        crs=crs,
        metadata=metadata,
    )


@mcp.tool()
def ingest_dgr_sensor_timeseries(
    project_id: str,
    campaign_id: str,
    sensor_type: str,
    records: list[dict[str, Any]],
    borehole_id: str | None = None,
    depth_m: float | None = None,
    units: dict[str, str] | None = None,
    qaqc_flags: list[str] | None = None,
) -> dict[str, Any]:
    """Ingest DGR sensor time-series records such as temperature, pressure, or deformation."""
    return ingest_dgr_sensor_timeseries_tool(
        project_id=project_id,
        campaign_id=campaign_id,
        sensor_type=sensor_type,
        records=records,
        borehole_id=borehole_id,
        depth_m=depth_m,
        units=units,
        qaqc_flags=qaqc_flags,
    )


@mcp.tool()
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
) -> dict[str, Any]:
    """Ingest DGR groundwater chemistry sample data with field parameters and analytes."""
    return ingest_dgr_water_sample_tool(
        project_id=project_id,
        campaign_id=campaign_id,
        sample_id=sample_id,
        borehole_id=borehole_id,
        depth_m=depth_m,
        sample_date=sample_date,
        field_parameters=field_parameters,
        analytes=analytes,
        units=units,
        qaqc_flags=qaqc_flags,
    )


@mcp.tool()
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
) -> dict[str, Any]:
    """Ingest DGR rock-core thermal, mechanical, petrophysical, or geochemical measurements."""
    return ingest_dgr_rock_core_measurement_tool(
        project_id=project_id,
        campaign_id=campaign_id,
        core_id=core_id,
        borehole_id=borehole_id,
        depth_interval=depth_interval,
        measurement_type=measurement_type,
        values=values,
        units=units,
        lab_method=lab_method,
        qaqc_flags=qaqc_flags,
    )


@mcp.tool()
def ingest_dgr_packer_test(
    project_id: str,
    campaign_id: str,
    borehole_id: str,
    interval_m: dict[str, float],
    hydraulic_conductivity_m_s: float | None = None,
    transmissivity_m2_s: float | None = None,
    pressure_observations: list[dict[str, Any]] | None = None,
    qaqc_flags: list[str] | None = None,
) -> dict[str, Any]:
    """Ingest DGR packer-test hydraulic measurements for calibration datasets."""
    return ingest_dgr_packer_test_tool(
        project_id=project_id,
        campaign_id=campaign_id,
        borehole_id=borehole_id,
        interval_m=interval_m,
        hydraulic_conductivity_m_s=hydraulic_conductivity_m_s,
        transmissivity_m2_s=transmissivity_m2_s,
        pressure_observations=pressure_observations,
        qaqc_flags=qaqc_flags,
    )


@mcp.tool()
def ingest_dgr_in_situ_stress(
    project_id: str,
    campaign_id: str,
    borehole_id: str,
    depth_m: float,
    method: str,
    stress_tensor: dict[str, Any],
    units: str = "MPa",
    qaqc_flags: list[str] | None = None,
) -> dict[str, Any]:
    """Ingest DGR in-situ stress measurements for mechanical THMC coupling."""
    return ingest_dgr_in_situ_stress_tool(
        project_id=project_id,
        campaign_id=campaign_id,
        borehole_id=borehole_id,
        depth_m=depth_m,
        method=method,
        stress_tensor=stress_tensor,
        units=units,
        qaqc_flags=qaqc_flags,
    )


@mcp.tool()
def validate_dgr_thmc_dataset(
    project_id: str,
    campaign_id: str | None = None,
    dataset_ids: list[str] | None = None,
) -> dict[str, Any]:
    """Validate DGR field-data coverage across T/H/M/C process groups."""
    return validate_dgr_thmc_dataset_tool(project_id=project_id, campaign_id=campaign_id, dataset_ids=dataset_ids)


@mcp.tool()
def build_dgr_calibration_dataset(
    project_id: str,
    campaign_id: str | None = None,
    target_processes: list[str] | None = None,
) -> dict[str, Any]:
    """Build a DGR THMC calibration dataset asset from ingested field records."""
    return build_dgr_calibration_dataset_tool(project_id=project_id, campaign_id=campaign_id, target_processes=target_processes)


@mcp.tool()
def save_dgr_data_package(
    project_id: str,
    package_label: str,
    campaign_id: str | None = None,
    dataset_ids: list[str] | None = None,
    package_spec: dict[str, Any] | None = None,
    notes: str = "",
) -> dict[str, Any]:
    """Save a DGR field-data package record for reproducible THMC modeling."""
    return save_dgr_data_package_tool(
        project_id=project_id,
        package_label=package_label,
        campaign_id=campaign_id,
        dataset_ids=dataset_ids,
        package_spec=package_spec,
        notes=notes,
    )


@mcp.tool()
def get_dgr_data_package(package_id: str) -> dict[str, Any]:
    """Get one saved DGR data package record."""
    return get_dgr_data_package_tool(package_id=package_id)


@mcp.tool()
def list_dgr_data_packages(project_id: str | None = None, campaign_id: str | None = None) -> dict[str, Any]:
    """List saved DGR data packages."""
    return list_dgr_data_packages_tool(project_id=project_id, campaign_id=campaign_id)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
