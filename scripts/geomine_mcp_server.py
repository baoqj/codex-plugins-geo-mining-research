"""GeoMine Research MCP server entrypoint."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from geomine.tools import (
    fetch_geochem_metadata_tool,
    resolve_aoi_tool,
    retrieve_assessment_reports_tool,
    search_geodata_sources_tool,
    search_mineral_occurrences_tool,
)


mcp = FastMCP("GeoMine Research")


@mcp.tool()
def resolve_aoi(input_data: dict[str, Any]) -> dict[str, Any]:
    """Normalize an AOI and report CRS, jurisdiction, assumptions, and warnings."""
    return resolve_aoi_tool(input_data)


@mcp.tool()
def search_geodata_sources(
    query: str,
    jurisdiction: str | None = None,
    data_type: str | None = None,
    rows: int = 10,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan or perform bounded public geodata source search."""
    return search_geodata_sources_tool(
        query=query,
        jurisdiction=jurisdiction,
        data_type=data_type,
        rows=rows,
        allow_network=allow_network,
    )


@mcp.tool()
def search_mineral_occurrences(
    jurisdiction: str,
    commodity: str | None = None,
    deposit_model: str | None = None,
    bbox: dict[str, float] | None = None,
    rows: int = 10,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan or perform bounded public mineral occurrence search."""
    return search_mineral_occurrences_tool(
        jurisdiction=jurisdiction,
        commodity=commodity,
        deposit_model=deposit_model,
        bbox=bbox,
        rows=rows,
        allow_network=allow_network,
    )


@mcp.tool()
def fetch_geochem_metadata(
    source: str | None = None,
    survey_id: str | None = None,
    source_url: str | None = None,
    jurisdiction: str | None = None,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan or fetch geochemical survey metadata."""
    return fetch_geochem_metadata_tool(
        source=source,
        survey_id=survey_id,
        source_url=source_url,
        jurisdiction=jurisdiction,
        allow_network=allow_network,
    )


@mcp.tool()
def retrieve_assessment_reports(
    jurisdiction: str,
    project_name: str | None = None,
    report_id: str | None = None,
    nts_sheet: str | None = None,
    commodity: str | None = None,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan or retrieve public assessment report metadata."""
    return retrieve_assessment_reports_tool(
        jurisdiction=jurisdiction,
        project_name=project_name,
        report_id=report_id,
        nts_sheet=nts_sheet,
        commodity=commodity,
        allow_network=allow_network,
    )


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()