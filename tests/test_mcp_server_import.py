import geomine_mcp_server


def test_mcp_server_imports():
    assert geomine_mcp_server.mcp is not None
    assert callable(geomine_mcp_server.main)
