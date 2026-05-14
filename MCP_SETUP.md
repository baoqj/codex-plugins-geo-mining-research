# GeoMine MCP Setup

GeoMine Research includes local MCP server implementations named `geomine`, `geomine_thmc`, `geomine_thmc_data`, and `geomine_pflotran`, but they are not auto-registered by the plugin manifest by default.

This is intentional. Keeping MCP disabled prevents Codex startup errors in environments where `uv`, `mcp[cli]`, `httpx`, or local skill installation paths are not ready.

## Files

```text
.codex-plugin/plugin.json
references/geomine.mcp.example.json
scripts/geomine_mcp_server.py
scripts/geomine/tools.py
mcp/geomine-thmc-server/
references/geomine-thmc.mcp.example.json
references/geomine-thmc-data.mcp.example.json
references/geomine-pflotran.mcp.example.json
```

## Validate JSON

```bash
python3 -m json.tool references/geomine.mcp.example.json
python3 -m json.tool references/geomine-thmc.mcp.example.json
python3 -m json.tool references/geomine-thmc-data.mcp.example.json
python3 -m json.tool references/geomine-pflotran.mcp.example.json
python3 scripts/validate_plugin.py
python3 tests/validate_thmc_mcp_config.py
```

## Run The Server Command

The deferred MCP template uses:

```bash
PYTHONPATH=./scripts uv --directory . run --no-project --with "mcp[cli]" --with httpx python scripts/geomine_mcp_server.py
```

This is a stdio MCP server, so it waits for an MCP client and may appear idle in a plain terminal.

The THMC server command is:

```bash
GEOMINE_THMC_MODE=mock uv --directory ./mcp/geomine-thmc-server run geomine-thmc-mcp
```

The DGR field-data acquisition server command is:

```bash
GEOMINE_THMC_MODE=mock uv --directory ./mcp/geomine-thmc-server run geomine-thmc-data-mcp
```

The PFLOTRAN planning server command is:

```bash
GEOMINE_THMC_MODE=mock uv --directory ./mcp/geomine-thmc-server run geomine-pflotran-mcp
```

## Development Smoke Test

Run the automated smoke tests:

```bash
PYTHONPATH=scripts uv run --no-project --with pytest --with "mcp[cli]" --with httpx python -m pytest
python3 scripts/test_thmc_mcp_tools.py
python3 scripts/test_thmc_data_mcp_tools.py
python3 scripts/test_pflotran_mcp_tools.py
uv --directory mcp/geomine-thmc-server run --with pytest python -m pytest
```

The test suite verifies:

- plugin manifest does not auto-register skills or MCP servers by default;
- no plugin-root `.mcp.json` exists by default;
- the deferred MCP example exposes exactly the expected GeoMine tools and is disabled by default;
- pure tool functions return stable JSON contracts;
- the MCP server imports without stdout leakage risk.
- `geomine_thmc` exposes a disabled example config, stable mock responses, PHREEQC draft/mock tools, OGS/PFLOTRAN job lifecycle tools, and run-record/model-version tools.
- `geomine_thmc_data` exposes a disabled example config, DGR campaign/borehole/field-measurement ingestion, data-gap validation, calibration dataset, and data-package tools.
- `geomine_pflotran` exposes a disabled example config for PFLOTRAN planning only: input deck skeleton generation, deck validation, run manifest generation, observation-output parsing, result summaries, and draft model-package records. It does not execute PFLOTRAN in v0.1.

## Direct Codex MCP Registration

For direct local debugging before plugin installation:

```bash
codex mcp add geomine \
  --env PYTHONPATH=/Users/aibao/Documents/Project/MiningReg/openminer/plugins/Code/geo-mining-research/scripts \
  -- \
  uv \
  --directory /Users/aibao/Documents/Project/MiningReg/openminer/plugins/Code/geo-mining-research \
  run \
  --no-project \
  --with \
  "mcp[cli]" \
  --with \
  httpx \
  python \
  scripts/geomine_mcp_server.py
```

Then run `/mcp` in Codex and confirm the `geomine` server and tools are visible.

For THMC-only local debugging:

```bash
scripts/install_thmc_mcp_dev.sh
```

For DGR field-data acquisition debugging:

```bash
scripts/install_thmc_data_mcp_dev.sh
```

Then run `/mcp` in Codex and confirm the `geomine_thmc`, `geomine_thmc_data`, or `geomine_pflotran` server and tools are visible.

## Plugin Install / Cache Notes

If Codex has already installed the plugin, reinstall after changing the manifest or MCP template:

```bash
codex plugin uninstall geo-mining-research
codex plugin install geo-mining-research
```

Codex may load a cached plugin copy, so a restart or reinstall may be required.

## Safety Defaults

- The plugin manifest has no `skills` entry and no `mcpServers` entry by default.
- The root `.mcp.json` file is intentionally absent by default.
- The example MCP config keeps `enabled` as `false` and `required` as `false`.
- The THMC MCP example config also keeps `enabled` as `false` and `required` as `false`.
- The DGR THMC data MCP example config also keeps `enabled` as `false` and `required` as `false`.
- The PFLOTRAN MCP planning example config also keeps `enabled` as `false` and `required` as `false`.
- `GEOMINE_ALLOW_NETWORK_DEFAULT` is `false`.
- Live network retrieval must be explicit and remains unsupported unless a specific adapter implements it.
- Tool outputs must include provenance and warnings.
- THMC mock outputs demonstrate workflow shape only; they are not validated solver results.
