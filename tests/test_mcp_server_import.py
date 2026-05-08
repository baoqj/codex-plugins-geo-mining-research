import geomine_mcp_server


def test_mcp_server_imports():
    assert geomine_mcp_server.mcp is not None
    assert callable(geomine_mcp_server.main)


def test_mcp_server_exposes_expected_wrappers():
    for name in [
        "normalize_aoi",
        "search_canada_geodata",
        "search_cdogs_surveys",
        "search_bc_minfile",
        "search_ontario_omi",
        "search_saskatchewan_mineral_data",
        "fetch_dataset_metadata",
        "summarize_dataset_provenance",
        "query_claim_neighbors",
        "calculate_infrastructure_distance",
    ]:
        assert hasattr(geomine_mcp_server, name)
