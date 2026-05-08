"""GeoMine Research MCP server entrypoint."""

from __future__ import annotations

from typing import Any

from mcp.server.fastmcp import FastMCP

from geomine.tools import (
    calculate_infrastructure_distance_tool,
    fetch_dataset_metadata_mcp_tool,
    normalize_aoi_tool,
    query_claim_neighbors_tool,
    search_bc_minfile_tool,
    search_canada_geodata_tool,
    search_cdogs_surveys_tool,
    search_ontario_omi_tool,
    search_saskatchewan_mineral_data_tool,
    summarize_dataset_provenance_tool,
)


mcp = FastMCP("geomine")


@mcp.tool()
def normalize_aoi(aoi: str | dict[str, Any], default_crs: str = "EPSG:4326") -> dict[str, Any]:
    """Normalize a user-provided AOI into a provenance-preserving GeoMine object."""
    return normalize_aoi_tool(aoi=aoi, default_crs=default_crs)


@mcp.tool()
def search_canada_geodata(
    query: str,
    province: str | None = None,
    commodity: str | None = None,
    rows: int = 10,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan or perform bounded Canadian public geodata source discovery."""
    return search_canada_geodata_tool(
        query=query,
        province=province,
        commodity=commodity,
        rows=rows,
        allow_network=allow_network,
    )


@mcp.tool()
def search_cdogs_surveys(
    aoi: str | None = None,
    commodity: str | None = None,
    province: str | None = None,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan CDoGS geochemical survey discovery with provenance and caveats."""
    return search_cdogs_surveys_tool(aoi=aoi, commodity=commodity, province=province, allow_network=allow_network)


@mcp.tool()
def search_bc_minfile(
    aoi: str | None = None,
    commodity: str | None = None,
    rows: int = 10,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan BC MINFILE mineral occurrence discovery."""
    return search_bc_minfile_tool(aoi=aoi, commodity=commodity, rows=rows, allow_network=allow_network)


@mcp.tool()
def search_ontario_omi(
    aoi: str | None = None,
    commodity: str | None = None,
    rows: int = 10,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan Ontario Mineral Inventory / OGSEarth occurrence discovery."""
    return search_ontario_omi_tool(aoi=aoi, commodity=commodity, rows=rows, allow_network=allow_network)


@mcp.tool()
def search_saskatchewan_mineral_data(
    aoi: str | None = None,
    commodity: str | None = None,
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan Saskatchewan public mineral data discovery."""
    return search_saskatchewan_mineral_data_tool(aoi=aoi, commodity=commodity, allow_network=allow_network)


@mcp.tool()
def fetch_dataset_metadata(dataset_id: str) -> dict[str, Any]:
    """Fetch local-registry dataset metadata and identify missing provenance fields."""
    return fetch_dataset_metadata_mcp_tool(dataset_id=dataset_id)


@mcp.tool()
def summarize_dataset_provenance(dataset: dict[str, Any]) -> dict[str, Any]:
    """Normalize a dataset provenance block without verifying the source."""
    return summarize_dataset_provenance_tool(dataset=dataset)


@mcp.tool()
def query_claim_neighbors(claim_id: str, buffer_km: float = 10.0, allow_network: bool = False) -> dict[str, Any]:
    """Plan a claim-neighbor scan without fabricating tenure results."""
    return query_claim_neighbors_tool(claim_id=claim_id, buffer_km=buffer_km, allow_network=allow_network)


@mcp.tool()
def calculate_infrastructure_distance(
    aoi: str,
    infrastructure_type: str = "road",
    allow_network: bool = False,
) -> dict[str, Any]:
    """Plan infrastructure-distance calculation and report required missing inputs."""
    return calculate_infrastructure_distance_tool(
        aoi=aoi,
        infrastructure_type=infrastructure_type,
        allow_network=allow_network,
    )


def main() -> None:
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
