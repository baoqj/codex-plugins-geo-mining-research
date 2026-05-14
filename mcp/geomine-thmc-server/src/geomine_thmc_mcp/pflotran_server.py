"""GeoMine PFLOTRAN MCP server entrypoint.

This server exposes planning and packaging tools only. It does not execute
PFLOTRAN locally or remotely in v0.1.
"""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from .tools import (
    build_pflotran_input_deck as build_pflotran_input_deck_tool,
    build_pflotran_result_summary as build_pflotran_result_summary_tool,
    build_pflotran_run_manifest as build_pflotran_run_manifest_tool,
    get_pflotran_model_package as get_pflotran_model_package_tool,
    list_pflotran_model_packages as list_pflotran_model_packages_tool,
    parse_pflotran_observation_output as parse_pflotran_observation_output_tool,
    save_pflotran_model_package as save_pflotran_model_package_tool,
    validate_pflotran_input_deck as validate_pflotran_input_deck_tool,
)


mcp = FastMCP("geomine_pflotran")


@mcp.tool()
def validate_input_deck(input_deck: str) -> dict[str, Any]:
    """Validate PFLOTRAN input deck structure without executing PFLOTRAN."""
    return validate_pflotran_input_deck_tool(input_deck=input_deck)


@mcp.tool()
def build_input_deck(
    project_id: str,
    model_id: str,
    scenario: str = "tailings_seepage",
    dimension: str = "2D",
    chemistry_mode: str = "reactive_transport",
    grid: dict[str, Any] | None = None,
    materials: list[dict[str, Any]] | None = None,
    chemistry: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a draft PFLOTRAN input deck skeleton and model manifest."""
    return build_pflotran_input_deck_tool(
        project_id=project_id,
        model_id=model_id,
        scenario=scenario,
        dimension=dimension,
        chemistry_mode=chemistry_mode,
        grid=grid,
        materials=materials,
        chemistry=chemistry,
    )


@mcp.tool()
def build_run_manifest(
    model_name: str,
    input_file: str = "model.in",
    database_file: str = "",
    mpi_processes: int | None = None,
    expected_outputs: list[str] | None = None,
) -> dict[str, Any]:
    """Build a PFLOTRAN run manifest without executing PFLOTRAN."""
    return build_pflotran_run_manifest_tool(
        model_name=model_name,
        input_file=input_file,
        database_file=database_file,
        mpi_processes=mpi_processes,
        expected_outputs=expected_outputs,
    )


@mcp.tool()
def parse_observation_output(observation_text: str, delimiter: str = "auto") -> dict[str, Any]:
    """Parse simple PFLOTRAN observation CSV/TSV text."""
    return parse_pflotran_observation_output_tool(observation_text=observation_text, delimiter=delimiter)


@mcp.tool()
def generate_result_summary(observation_rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Build numeric summaries from parsed PFLOTRAN observation rows."""
    return build_pflotran_result_summary_tool(observation_rows=observation_rows)


@mcp.tool()
def save_model_package(
    project_id: str,
    package_label: str,
    package_spec: dict[str, Any],
    source_asset_ids: list[str] | None = None,
    notes: str = "",
) -> dict[str, Any]:
    """Save a draft PFLOTRAN Modeling Package record."""
    return save_pflotran_model_package_tool(
        project_id=project_id,
        package_label=package_label,
        package_spec=package_spec,
        source_asset_ids=source_asset_ids,
        notes=notes,
    )


@mcp.tool()
def get_model_package(package_id: str) -> dict[str, Any]:
    """Fetch a draft PFLOTRAN Modeling Package record."""
    return get_pflotran_model_package_tool(package_id=package_id)


@mcp.tool()
def list_model_packages(project_id: str | None = None) -> dict[str, Any]:
    """List draft PFLOTRAN Modeling Package records."""
    return list_pflotran_model_packages_tool(project_id=project_id)


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
