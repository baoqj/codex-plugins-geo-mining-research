"""Static Canada-first geoscience and mining data catalog."""

from __future__ import annotations

from .evidence_schema import DataSourceRecord


CATALOG: tuple[DataSourceRecord, ...] = (
    DataSourceRecord(
        name="NRCan CDoGS",
        jurisdiction="Canada",
        data_types=("geochemistry", "sample-location", "survey-metadata"),
        likely_formats=("CSV", "GIS", "database export"),
        use_cases=("regional geochemical screening", "sample media review"),
        provenance_notes="Federal geochemical survey database; preserve survey id, medium, analytical method, and release date.",
        limitations="Coverage varies by region and survey generation; detection limits and methods must be checked before comparing surveys.",
        url="https://natural-resources.canada.ca/",
    ),
    DataSourceRecord(
        name="Geo.ca",
        jurisdiction="Canada",
        data_types=("geodata-catalog", "metadata", "gis"),
        likely_formats=("catalog record", "WMS", "WFS", "KML", "CSV", "Shapefile"),
        use_cases=("public data discovery", "license and metadata lookup"),
        provenance_notes="Use as a catalog entry point for Canadian federal and open-government geoscience datasets.",
        limitations="Catalog discovery is not the same as data retrieval; each linked dataset needs separate verification.",
        url="https://geo.ca/",
    ),
    DataSourceRecord(
        name="BC MINFILE",
        jurisdiction="British Columbia",
        data_types=("mineral-occurrence", "deposit-model", "commodity"),
        likely_formats=("database record", "CSV", "GIS"),
        use_cases=("nearby mineral occurrence review", "deposit model context"),
        provenance_notes="Government mineral occurrence inventory; preserve MINFILE id, status, commodities, and location confidence.",
        limitations="Historic records can include uncertain locations or legacy resource language that requires caution.",
        url="https://minfile.gov.bc.ca/",
    ),
    DataSourceRecord(
        name="BC Geological Survey data portals",
        jurisdiction="British Columbia",
        data_types=("geology", "geochemistry", "geophysics", "geochronology"),
        likely_formats=("ArcGIS REST", "CSV", "Shapefile", "GeoPackage", "PDF"),
        use_cases=("bedrock geology", "regional geochemistry", "geophysical context"),
        provenance_notes="Use dataset release name, scale, publication year, and map/product id.",
        limitations="Map scale and compilation vintage can materially affect target-scale interpretation.",
        url="https://www2.gov.bc.ca/gov/content/industry/mineral-exploration-mining/british-columbia-geological-survey",
    ),
    DataSourceRecord(
        name="Ontario OGSEarth and Ontario Mineral Inventory",
        jurisdiction="Ontario",
        data_types=("gis", "geology", "geochemistry", "geophysics", "drillhole", "mineral-occurrence"),
        likely_formats=("KML", "KMZ", "Shapefile", "ArcGIS REST", "CSV"),
        use_cases=("Ontario claim screening", "OMI occurrence review", "LCT pegmatite context"),
        provenance_notes="Preserve OGS layer name, OMI identifier, update date, and layer metadata.",
        limitations="KML layers may need conversion before spatial analysis; occurrence records can mix historic and current interpretations.",
        url="https://www.geologyontario.mndm.gov.on.ca/",
    ),
    DataSourceRecord(
        name="Provincial and territorial geological surveys",
        jurisdiction="Canada provinces and territories",
        data_types=("geology", "assessment-report", "geochemistry", "geophysics", "mineral-tenure"),
        likely_formats=("catalog record", "PDF", "GIS", "CSV", "ArcGIS REST"),
        use_cases=("jurisdiction-specific source discovery", "assessment report retrieval planning"),
        provenance_notes="Record the province or territory, survey branch, publication id, and map scale.",
        limitations="Access patterns, licensing, and metadata quality vary by jurisdiction.",
    ),
    DataSourceRecord(
        name="USGS mineral and geochemical data",
        jurisdiction="United States and global extension",
        data_types=("geology", "geochemistry", "mineral-occurrence", "geophysics"),
        likely_formats=("REST", "CSV", "GIS", "database export"),
        use_cases=("cross-border comparison", "USMIN and regional geochemical context"),
        provenance_notes="Use as an extension source outside the Canada-first MVP scope.",
        limitations="Not a substitute for Canadian provincial datasets when evaluating Canadian AOIs.",
        url="https://mrdata.usgs.gov/",
    ),
    DataSourceRecord(
        name="EarthChem",
        jurisdiction="Global extension",
        data_types=("geochemistry", "rock-geochemistry", "petrology"),
        likely_formats=("portal export", "CSV", "database record"),
        use_cases=("regional geochemical background", "igneous and metamorphic comparison"),
        provenance_notes="Preserve sample id, method, repository, citation, and download date.",
        limitations="Coverage and analytical comparability vary by contributing database.",
        url="https://www.earthchem.org/",
    ),
)


def list_sources() -> list[DataSourceRecord]:
    return list(CATALOG)


def find_sources(
    jurisdiction: str | None = None,
    data_type: str | None = None,
) -> list[DataSourceRecord]:
    """Find catalog entries by broad jurisdiction and data type."""

    jurisdiction_l = jurisdiction.lower() if jurisdiction else None
    data_type_l = data_type.lower() if data_type else None
    results: list[DataSourceRecord] = []
    for record in CATALOG:
        if jurisdiction_l and jurisdiction_l not in record.jurisdiction.lower():
            if not (jurisdiction_l in {"bc", "b.c."} and "british columbia" in record.jurisdiction.lower()):
                continue
        if data_type_l and not any(data_type_l in item.lower() for item in record.data_types):
            continue
        results.append(record)
    return results
