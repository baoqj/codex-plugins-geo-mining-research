# GeoMine MCP Troubleshooting

## `geomine_thmc` or `geomine_thmc_data` does not appear in Codex

- Confirm the plugin was reinstalled or Codex was restarted after copying the plugin.
- Confirm the example config was installed or converted into the local MCP config used by Codex.
- Run `python3 tests/validate_thmc_mcp_config.py`.
- Run `python3 scripts/test_thmc_mcp_tools.py` to verify pure tool functions.
- Run `python3 scripts/test_thmc_data_mcp_tools.py` to verify DGR data-acquisition tool functions.

## Server exits on startup

Run:

```bash
uv --directory mcp/geomine-thmc-server run python -m geomine_thmc_mcp.server
```

The process is a stdio MCP server and may appear idle when no MCP client is attached. Startup failures usually mean missing `uv`, an invalid Python version, or missing `mcp[cli]`.

## Tools return `mode: "mock"`

This is expected by default. Mock mode validates contracts and workflow shape. It is not live OpenMine data and not a numerical simulation.

For `geomine_thmc_data`, mock mode also means records are local/schema examples or user-supplied local ingestions, not verified DGR field measurements.

## PHREEQC output looks incomplete

The MCP server currently produces a conservative PHREEQC draft and mock selected output. It does not invent radionuclide species mappings, thermodynamic constants, kinetic rates, or sorption parameters.

## OGS/PFLOTRAN jobs complete too quickly

Mock jobs are stored in a local JSON registry and advanced through a deterministic lifecycle for testing. They do not run real solvers.

## Do not leak secrets

The server only reports boolean environment readiness. Do not paste tokens, DSNs, signed URLs, or secret access keys into reports.
