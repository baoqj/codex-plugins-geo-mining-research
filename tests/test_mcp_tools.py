from geomine.tools import (
    fetch_geochem_metadata_tool,
    resolve_aoi_tool,
    retrieve_assessment_reports_tool,
    search_geodata_sources_tool,
    search_mineral_occurrences_tool,
)


EXPECTED_CONTRACT = {"data", "provenance", "warnings", "next_steps"}


def assert_contract(result: dict):
    assert set(result) == EXPECTED_CONTRACT
    assert isinstance(result["data"], dict)
    assert isinstance(result["provenance"], dict)
    assert isinstance(result["warnings"], list)
    assert isinstance(result["next_steps"], list)
    assert result["provenance"]["tool_layer"] == "scripts/geomine/tools.py"
    assert result["provenance"]["retrieved_at"]


def test_resolve_aoi_tool_returns_contract():
    result = resolve_aoi_tool({"name": "Example", "province": "Ontario"})

    assert_contract(result)
    assert result["data"]["province_or_territory"] == "Ontario"
    assert result["provenance"]["retrieval_status"] == "parsed"
    assert result["provenance"]["network"] == "not-used"
    assert result["warnings"]


def test_search_geodata_sources_planned_mode():
    result = search_geodata_sources_tool(
        query="geochemistry",
        jurisdiction="BC",
        rows=5,
        allow_network=False,
    )

    assert_contract(result)
    assert result["provenance"]["retrieval_status"] == "planned"
    assert result["provenance"]["network"] == "disabled"
    assert result["data"]["planned_requests"]
    assert result["data"]["results"] == []
    assert all(request["retrieval_status"] == "planned" for request in result["data"]["planned_requests"])
    assert "Network disabled" in " ".join(result["warnings"])


def test_search_geodata_sources_network_mode_is_unsupported_not_fabricated():
    result = search_geodata_sources_tool(
        query="geochemistry",
        jurisdiction="BC",
        rows=5,
        allow_network=True,
    )

    assert_contract(result)
    assert result["provenance"]["retrieval_status"] == "unsupported"
    assert result["provenance"]["network"] == "requested-but-not-implemented"
    assert result["data"]["results"] == []


def test_search_mineral_occurrences_planned_mode():
    result = search_mineral_occurrences_tool(
        jurisdiction="BC",
        commodity="Cu",
        deposit_model="porphyry Cu-Mo",
        allow_network=False,
    )

    assert_contract(result)
    assert result["data"]["planned_requests"]
    assert result["data"]["occurrences"] == []
    assert result["provenance"]["network"] == "disabled"
    assert result["provenance"]["retrieval_status"] == "planned"


def test_search_mineral_occurrences_bbox_adds_arcgis_plan():
    result = search_mineral_occurrences_tool(
        jurisdiction="BC",
        bbox={"xmin": -124.0, "ymin": 49.0, "xmax": -123.0, "ymax": 50.0},
        rows=10,
    )

    assert_contract(result)
    urls = [request["url"] for request in result["data"]["planned_requests"]]
    assert any("arcgis/rest/services/MRData" in url for url in urls)
    assert result["data"]["occurrences"] == []


def test_search_mineral_occurrences_incomplete_bbox_warns():
    result = search_mineral_occurrences_tool(
        jurisdiction="BC",
        bbox={"xmin": -124.0, "ymin": 49.0},
    )

    assert_contract(result)
    assert "bbox is missing required keys" in " ".join(result["warnings"])
    assert result["data"]["occurrences"] == []


def test_fetch_geochem_metadata_planned_mode():
    result = fetch_geochem_metadata_tool(
        source="CDoGS",
        jurisdiction="Canada",
        allow_network=False,
    )

    assert_contract(result)
    assert result["provenance"]["retrieval_status"] == "planned"
    assert result["provenance"]["network"] == "disabled"
    assert result["data"]["metadata"] == []
    assert result["data"]["candidate_sources"]


def test_retrieve_assessment_reports_planned_mode():
    result = retrieve_assessment_reports_tool(
        jurisdiction="Ontario",
        project_name="Example Project",
        commodity="Au",
        allow_network=False,
    )

    assert_contract(result)
    assert result["provenance"]["network"] == "disabled"
    assert result["provenance"]["retrieval_status"] == "planned"
    assert result["data"]["reports"] == []
    assert result["data"]["planned_sources"]
