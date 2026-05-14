"""GeoMine THMC MCP server entrypoint."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from .tools import (
    build_phreeqc_input as build_phreeqc_input_tool,
    fetch_compute_job_results as fetch_compute_job_results_tool,
    fetch_mesh_or_parameter_field as fetch_mesh_or_parameter_field_tool,
    get_compute_job_status as get_compute_job_status_tool,
    get_openmine_project as get_openmine_project_tool,
    get_project_aoi as get_project_aoi_tool,
    get_thmc_mesh_catalog as get_thmc_mesh_catalog_tool,
    get_thmc_model_version as get_thmc_model_version_tool,
    get_thmc_run_record as get_thmc_run_record_tool,
    list_openmine_projects as list_openmine_projects_tool,
    list_thmc_model_versions as list_thmc_model_versions_tool,
    list_thmc_run_records as list_thmc_run_records_tool,
    query_lithology_units as query_lithology_units_tool,
    query_mineral_assemblages as query_mineral_assemblages_tool,
    query_water_chemistry_samples as query_water_chemistry_samples_tool,
    run_phreeqc_job as run_phreeqc_job_tool,
    save_thmc_model_version as save_thmc_model_version_tool,
    save_thmc_run_record as save_thmc_run_record_tool,
    submit_ogs_job as submit_ogs_job_tool,
    submit_pflotran_job as submit_pflotran_job_tool,
)


mcp = FastMCP("geomine_thmc")


@mcp.tool()
def list_openmine_projects(
    status: str | None = "active",
    jurisdiction: str | None = None,
    commodity: str | None = None,
    limit: int = 20,
) -> dict[str, Any]:
    """List OpenMine projects available to THMC modeling workflows."""
    return list_openmine_projects_tool(status=status, jurisdiction=jurisdiction, commodity=commodity, limit=limit)


@mcp.tool()
def get_openmine_project(project_id: str) -> dict[str, Any]:
    """Get one OpenMine project metadata record by project_id."""
    return get_openmine_project_tool(project_id=project_id)


@mcp.tool()
def get_project_aoi(project_id: str, aoi_id: str | None = None) -> dict[str, Any]:
    """Get the modeling AOI for a THMC project."""
    return get_project_aoi_tool(project_id=project_id, aoi_id=aoi_id)


@mcp.tool()
def query_water_chemistry_samples(
    project_id: str,
    aoi_id: str | None = None,
    sample_types: list[str] | None = None,
    analytes: list[str] | None = None,
    date_range: dict[str, str] | None = None,
    include_qaqc: bool = True,
    limit: int = 5000,
) -> dict[str, Any]:
    """Query THMC-ready groundwater or water-chemistry samples."""
    return query_water_chemistry_samples_tool(
        project_id=project_id,
        aoi_id=aoi_id,
        sample_types=sample_types,
        analytes=analytes,
        date_range=date_range,
        include_qaqc=include_qaqc,
        limit=limit,
    )


@mcp.tool()
def query_lithology_units(
    project_id: str,
    aoi_id: str | None = None,
    include_geometry: bool = True,
    target_crs: str = "EPSG:4326",
) -> dict[str, Any]:
    """Query lithology units and THMC parameter hints for a project."""
    return query_lithology_units_tool(
        project_id=project_id,
        aoi_id=aoi_id,
        include_geometry=include_geometry,
        target_crs=target_crs,
    )


@mcp.tool()
def query_mineral_assemblages(project_id: str, unit_id: str | None = None) -> dict[str, Any]:
    """Query mineral assemblages for reaction-network design."""
    return query_mineral_assemblages_tool(project_id=project_id, unit_id=unit_id)


@mcp.tool()
def get_thmc_mesh_catalog(project_id: str) -> dict[str, Any]:
    """List mesh and parameter-field assets for a THMC project."""
    return get_thmc_mesh_catalog_tool(project_id=project_id)


@mcp.tool()
def fetch_mesh_or_parameter_field(
    project_id: str,
    asset_type: str,
    field_name: str | None = None,
    format: str | None = None,
    target_crs: str | None = None,
) -> dict[str, Any]:
    """Fetch metadata for a THMC mesh or parameter field asset."""
    return fetch_mesh_or_parameter_field_tool(
        project_id=project_id,
        asset_type=asset_type,
        field_name=field_name,
        format=format,
        target_crs=target_crs,
    )


@mcp.tool()
def build_phreeqc_input(
    project_id: str,
    model_id: str,
    scenario: str = "uranium_mine_groundwater",
    sample_ids: list[str] | None = None,
    database: str = "phreeqc.dat",
    reaction_network: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a PHREEQC draft input file from project chemistry and reaction-network hints."""
    return build_phreeqc_input_tool(
        project_id=project_id,
        model_id=model_id,
        scenario=scenario,
        sample_ids=sample_ids,
        database=database,
        reaction_network=reaction_network,
    )


@mcp.tool()
def run_phreeqc_job(
    project_id: str,
    model_id: str,
    phreeqc_input: str | None = None,
    database: str = "phreeqc.dat",
    run_mode: str = "mock",
) -> dict[str, Any]:
    """Run or mock-run a PHREEQC job and return selected outputs."""
    return run_phreeqc_job_tool(
        project_id=project_id,
        model_id=model_id,
        phreeqc_input=phreeqc_input,
        database=database,
        run_mode=run_mode,
    )


@mcp.tool()
def submit_ogs_job(
    project_id: str,
    model_version_id: str,
    mesh_asset_id: str,
    process_type: str = "ComponentTransport",
    parameters: dict[str, Any] | None = None,
    compute_profile: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Submit an OGS job to the THMC compute service or mock job registry."""
    return submit_ogs_job_tool(
        project_id=project_id,
        model_version_id=model_version_id,
        mesh_asset_id=mesh_asset_id,
        process_type=process_type,
        parameters=parameters,
        compute_profile=compute_profile,
    )


@mcp.tool()
def submit_pflotran_job(
    project_id: str,
    model_version_id: str,
    mesh_asset_id: str,
    chemistry_mode: str = "reactive_transport",
    parameters: dict[str, Any] | None = None,
    compute_profile: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Submit a PFLOTRAN job to the THMC compute service or mock job registry."""
    return submit_pflotran_job_tool(
        project_id=project_id,
        model_version_id=model_version_id,
        mesh_asset_id=mesh_asset_id,
        chemistry_mode=chemistry_mode,
        parameters=parameters,
        compute_profile=compute_profile,
    )


@mcp.tool()
def get_compute_job_status(job_id: str) -> dict[str, Any]:
    """Check OGS/PFLOTRAN compute job status."""
    return get_compute_job_status_tool(job_id=job_id)


@mcp.tool()
def fetch_compute_job_results(job_id: str) -> dict[str, Any]:
    """Fetch OGS/PFLOTRAN compute job result assets."""
    return fetch_compute_job_results_tool(job_id=job_id)


@mcp.tool()
def save_thmc_model_version(
    project_id: str,
    model_id: str,
    version_label: str,
    model_spec: dict[str, Any],
    source_asset_ids: list[str] | None = None,
    notes: str = "",
) -> dict[str, Any]:
    """Save a THMC model version record."""
    return save_thmc_model_version_tool(
        project_id=project_id,
        model_id=model_id,
        version_label=version_label,
        model_spec=model_spec,
        source_asset_ids=source_asset_ids,
        notes=notes,
    )


@mcp.tool()
def get_thmc_model_version(model_version_id: str) -> dict[str, Any]:
    """Get a THMC model version record."""
    return get_thmc_model_version_tool(model_version_id=model_version_id)


@mcp.tool()
def list_thmc_model_versions(project_id: str | None = None, model_id: str | None = None) -> dict[str, Any]:
    """List THMC model version records."""
    return list_thmc_model_versions_tool(project_id=project_id, model_id=model_id)


@mcp.tool()
def save_thmc_run_record(
    project_id: str,
    model_id: str,
    model_version_id: str,
    solver: str,
    input_asset_ids: list[str] | None = None,
    output_asset_ids: list[str] | None = None,
    solver_version: str = "mock",
    parameters_hash: str | None = None,
    data_hash: str | None = None,
    status: str = "completed",
    warnings: list[str] | None = None,
    created_by: str = "geomine-thmc-mcp",
) -> dict[str, Any]:
    """Save a THMC run record with provenance fields."""
    return save_thmc_run_record_tool(
        project_id=project_id,
        model_id=model_id,
        model_version_id=model_version_id,
        solver=solver,
        input_asset_ids=input_asset_ids,
        output_asset_ids=output_asset_ids,
        solver_version=solver_version,
        parameters_hash=parameters_hash,
        data_hash=data_hash,
        status=status,
        warnings=warnings,
        created_by=created_by,
    )


@mcp.tool()
def get_thmc_run_record(run_id: str) -> dict[str, Any]:
    """Get a THMC run record by run_id."""
    return get_thmc_run_record_tool(run_id=run_id)


@mcp.tool()
def list_thmc_run_records(project_id: str | None = None, model_id: str | None = None) -> dict[str, Any]:
    """List THMC run records."""
    return list_thmc_run_records_tool(project_id=project_id, model_id=model_id)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
