# GeoMine MCP Setup

GeoMine Research now declares one local MCP server named `geomine`.

## Files

```text
.codex-plugin/plugin.json
.mcp.json
scripts/geomine_mcp_server.py
scripts/geomine/tools.py
```

## Validate JSON

```bash
python3 -m json.tool .mcp.json
python3 scripts/validate_plugin.py
```

## Run The Server Command

The bundled `.mcp.json` uses:

```bash
PYTHONPATH=./scripts uv --directory . run --no-project --with "mcp[cli]" --with httpx python scripts/geomine_mcp_server.py
```

This is a stdio MCP server, so it waits for an MCP client and may appear idle in a plain terminal.

## Development Smoke Test

Run the automated smoke tests:

```bash
PYTHONPATH=scripts uv run --no-project --with pytest --with "mcp[cli]" --with httpx python -m pytest
```

The test suite verifies:

- plugin manifest points to `.mcp.json`;
- `.mcp.json` exposes exactly the expected GeoMine tools;
- pure tool functions return stable JSON contracts;
- the MCP server imports without stdout leakage risk.

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

## Plugin Install / Cache Notes

If Codex has already installed the plugin, reinstall after changing `.mcp.json`:

```bash
codex plugin uninstall geo-mining-research
codex plugin install geo-mining-research
```

Codex may load a cached plugin copy, so a restart or reinstall may be required.

## Safety Defaults

- `required` is `false` so a failed MCP server does not disable the whole plugin.
- `GEOMINE_ALLOW_NETWORK_DEFAULT` is `false`.
- Live network retrieval must be explicit and remains unsupported unless a specific adapter implements it.
- Tool outputs must include provenance and warnings.
