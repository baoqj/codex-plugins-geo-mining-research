# GeoMine THMC MCP Server

`geomine_thmc` is an optional MCP server for THMC Skill Family 2.0. It provides mock-backed tools for OpenMine project metadata, water chemistry, lithology/mineralogy, R2/PostGIS-like model assets, PHREEQC input/job drafts, OGS/PFLOTRAN job lifecycle, model versions, and run records.

`geomine_thmc_data` is the companion DGR field-data acquisition server. It provides mock/local tools for DGR campaigns, boreholes, sensor time series, groundwater chemistry, rock-core measurements, packer tests, in-situ stress, data-gap validation, calibration datasets, and data packages.

This server is an enhancement layer. THMC skills must keep working in Core Mode when it is unavailable.

Run local checks:

```bash
uv --directory mcp/geomine-thmc-server run pytest
python3 scripts/test_thmc_mcp_tools.py
python3 scripts/test_thmc_data_mcp_tools.py
```

All tools return the unified `ok/mode/tool/query/results/assets/provenance/warnings/errors` contract. Mock mode is the default and must not be interpreted as live OpenMine data, verified DGR field data, or real numerical solver output.
