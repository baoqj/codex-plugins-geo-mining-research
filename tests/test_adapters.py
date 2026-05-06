from geomine.adapters import (
    ArcGisFeatureServiceAdapter,
    BcDataCatalogueAdapter,
    OpenCanadaCkanAdapter,
    get_source_registry,
)


def test_open_canada_ckan_url_builder():
    adapter = OpenCanadaCkanAdapter()
    url = adapter.build_package_search_url("geochemical survey", rows=5)
    assert url.startswith("https://open.canada.ca/data/api/3/action/package_search?")
    assert "geochemical+survey" in url
    assert "rows=5" in url


def test_bc_ckan_parser():
    adapter = BcDataCatalogueAdapter()
    payload = {
        "success": True,
        "result": {
            "results": [
                {
                    "id": "minfile-occurrence",
                    "title": "Mineral Occurrence table",
                    "license_title": "Open Government Licence - British Columbia",
                    "organization": {"title": "BC Geological Survey"},
                    "resources": [
                        {
                            "id": "csv-resource",
                            "name": "CSV",
                            "format": "csv",
                            "url": "https://example.test/minfile.csv",
                        }
                    ],
                }
            ]
        },
    }
    parsed = adapter.parse_package_search(payload, query={"q": "MINFILE"})
    assert len(parsed) == 1
    assert parsed[0].source == "BC Data Catalogue"
    assert parsed[0].formats == ("CSV",)
    assert parsed[0].resources[0].resource_id == "csv-resource"


def test_arcgis_query_builder_and_parser():
    adapter = ArcGisFeatureServiceAdapter(
        service_url="https://energy.usgs.gov/arcgis/rest/services/MRData/Mineral_Resource_Data_System/MapServer",
        source_name="USGS MRData",
        jurisdiction="United States",
    )
    url = adapter.build_query_url(
        where="1=1",
        geometry={"xmin": -125, "ymin": 45, "xmax": -120, "ymax": 50, "spatialReference": {"wkid": 4326}},
        result_record_count=25,
    )
    assert "/0/query?" in url
    assert "resultRecordCount=25" in url
    assert "geometryType=esriGeometryEnvelope" in url

    payload = {
        "fields": [{"name": "OBJECTID"}, {"name": "dep_name"}],
        "features": [
            {
                "attributes": {"OBJECTID": 7, "dep_name": "Example Deposit"},
                "geometry": {"x": -123.1, "y": 49.2},
            }
        ],
    }
    parsed = adapter.parse_feature_set(payload, title_field="dep_name")
    assert parsed[0].title == "Example Deposit"
    assert parsed[0].record_id == "7"


def test_source_registry_filters():
    registry = get_source_registry(status="roadmap-only")
    keys = {item["key"] for item in registry}
    assert "nrcan-cdogs" in keys
    assert "earthchem-library" in keys
