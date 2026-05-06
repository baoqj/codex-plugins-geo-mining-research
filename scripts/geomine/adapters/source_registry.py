"""Candidate live-data adapter registry for GeoMine Research."""

from __future__ import annotations

from typing import Any


ADAPTER_SOURCE_REGISTRY: tuple[dict[str, Any], ...] = (
    {
        "key": "open-canada-ckan",
        "source": "Open Canada / Geo.ca",
        "jurisdiction": "Canada",
        "access_pattern": "CKAN package_search and downstream resource links",
        "endpoint": "https://open.canada.ca/data/api/3/action/package_search",
        "auth": "none for public catalogue search",
        "status": "url-builder-and-parser",
    },
    {
        "key": "bc-data-catalogue-ckan",
        "source": "BC Data Catalogue / MINFILE",
        "jurisdiction": "British Columbia",
        "access_pattern": "CKAN package_search, resource download links, WMS/KML/CSV/SHP/XLS resources",
        "endpoint": "https://catalogue.data.gov.bc.ca/api/3/action/package_search",
        "auth": "none for public catalogue search",
        "status": "url-builder-and-parser",
    },
    {
        "key": "usgs-mrdata-arcgis",
        "source": "USGS MRData ArcGIS REST",
        "jurisdiction": "United States and global extension",
        "access_pattern": "ArcGIS REST MapServer/FeatureServer query",
        "endpoint": "https://energy.usgs.gov/arcgis/rest/services/MRData/Mineral_Resource_Data_System/MapServer",
        "auth": "none for public service query",
        "status": "url-builder-and-parser",
    },
    {
        "key": "nrcan-cdogs",
        "source": "NRCan CDoGS",
        "jurisdiction": "Canada",
        "access_pattern": "metadata pages, spreadsheet links, KML links, WMS index layer",
        "endpoint": "https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm",
        "auth": "none for public metadata and downloads",
        "status": "roadmap-only",
    },
    {
        "key": "ontario-ogsearth",
        "source": "Ontario OGSEarth / OMI",
        "jurisdiction": "Ontario",
        "access_pattern": "KML bookmarks and GeologyOntario record pages",
        "endpoint": "https://www.geologyontario.mndm.gov.on.ca/ogsearth.html",
        "auth": "none for public KML records",
        "status": "roadmap-only",
    },
    {
        "key": "earthchem-library",
        "source": "EarthChem Library",
        "jurisdiction": "Global extension",
        "access_pattern": "public search/export workflow; API surface to be confirmed",
        "endpoint": "https://ecl.earthchem.org/search.php",
        "auth": "none identified for public search; workflows may vary",
        "status": "roadmap-only",
    },
)


def get_source_registry(status: str | None = None) -> list[dict[str, Any]]:
    if status is None:
        return [dict(item) for item in ADAPTER_SOURCE_REGISTRY]
    return [dict(item) for item in ADAPTER_SOURCE_REGISTRY if item["status"] == status]
