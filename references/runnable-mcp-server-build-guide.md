# Runnable MCP Server Build Guide

This guide documents the current v0.2 GeoMine Research MCP implementation and the repeatable steps for developing, configuring, running, and testing the local server. Plugin-level activation is deferred by default to avoid Codex startup errors in environments without a complete local MCP/skill setup.

## 1. Target Outcome

GeoMine Research implements one local stdio MCP server:

```text
Codex / MCP client
  -> reads .codex-plugin/plugin.json
  -> does not auto-register skills or MCP servers by default
  -> starts the geomine stdio server only after explicit local MCP registration
  -> discovers deterministic GeoMine tools
  -> receives structured results with provenance, warnings, and next_steps
```

Server name:

```text
geomine
```

Enabled tools:

- `normalize_aoi`
- `search_canada_geodata`
- `search_cdogs_surveys`
- `search_bc_minfile`
- `search_ontario_omi`
- `search_saskatchewan_mineral_data`
- `fetch_dataset_metadata`
- `summarize_dataset_provenance`
- `query_claim_neighbors`
- `calculate_infrastructure_distance`

The current server does not perform default live retrieval. When a tool receives `allow_network=true` for an unsupported live path, it returns an explicit `unsupported` retrieval status instead of fabricated records.

## 2. Files

```text
.codex-plugin/plugin.json
MCP_SETUP.md
references/geomine.mcp.example.json
scripts/geomine/tools.py
scripts/geomine_mcp_server.py
scripts/run_mcp_sample_cases.py
tests/test_mcp_tools.py
tests/test_mcp_server_import.py
tests/test_manifest.py
```

Key rules:

- Keep root `.mcp.json` absent until the server is intentionally enabled.
- Keep the default plugin manifest free of `skills` and `mcpServers`.
- Keep only `plugin.json` inside `.codex-plugin/`.
- Keep MCP transport code thin; business logic belongs in `scripts/geomine/tools.py`.
- Keep pure tool tests independent from MCP transport.

## 3. MCP Configuration

`plugin.json` does not point to local skills or MCP servers by default:

```json
{
  "name": "geo-mining-research",
  "version": "0.2.0"
}
```

`references/geomine.mcp.example.json` defines a disabled future-install server map:

```json
{
  "geomine": {
    "command": "uv",
    "args": [
      "--directory",
      ".",
      "run",
      "--no-project",
      "--with",
      "mcp[cli]",
      "--with",
      "httpx",
      "python",
      "scripts/geomine_mcp_server.py"
    ],
    "env": {
      "PYTHONPATH": "./scripts",
      "GEOMINE_ALLOW_NETWORK_DEFAULT": "false"
    },
    "enabled": false,
    "required": false
  }
}
```

`enabled` and `required` remain `false` so an incomplete local MCP setup does not affect startup.

## 4. Tool Implementation Pattern

Each pure tool function returns a dictionary with this contract:

```python
{
    "ok": True,
    "tool": "tool_name",
    "query": {...},
    "provenance": {
        "retrieval_status": "planned",
        "network": "disabled",
    },
    "warnings": [],
    "next_steps": [],
}
```

Rules:

- Never write to stdout from tool functions.
- Never call the network unless the user or caller explicitly enables it.
- Preserve source names, URLs, assumptions, and limitations in structured fields.
- Use warnings for source gaps or unsupported live retrieval.
- Throw only for programmer errors, not for normal source limitations.

## 5. Run Locally

Validate plugin metadata and MCP JSON:

```bash
python3 scripts/validate_plugin.py
python3 -m json.tool references/geomine.mcp.example.json
```

Run pytest:

```bash
PYTHONPATH=scripts uv run --no-project --with pytest --with "mcp[cli]" --with httpx python -m pytest
```

Run the stdio server command directly:

```bash
PYTHONPATH=./scripts uv --directory . run --no-project --with "mcp[cli]" --with httpx python scripts/geomine_mcp_server.py
```

The direct server process waits for an MCP client, so a plain terminal run may appear idle.

## 6. Codex Direct MCP Registration

For local debugging outside plugin install flow:

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

Then run `/mcp` in Codex and verify the `geomine` server and ten tools are visible.

## 7. Automated Sample Suite

Generate deterministic test cases, JSON results, and a Markdown report:

```bash
PYTHONPATH=scripts python3 scripts/run_mcp_sample_cases.py ../../report
```

Expected output files:

```text
openminer/plugins/report/2026-05-08-geomine-mcp-test-cases.md
openminer/plugins/report/2026-05-08-geomine-mcp-sample-results.json
openminer/plugins/report/2026-05-08-geomine-mcp-test-report.md
```

The sample suite covers all ten MCP tools plus one live-network guardrail case.

## 8. Stdio Smoke Test Method

Use the Python MCP client to verify the server starts and exposes exactly the expected tools:

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

params = StdioServerParameters(
    command="uv",
    args=[
        "--directory",
        ".",
        "run",
        "--no-project",
        "--with",
        "mcp[cli]",
        "--with",
        "httpx",
        "python",
        "scripts/geomine_mcp_server.py",
    ],
    env={"PYTHONPATH": "./scripts", "GEOMINE_ALLOW_NETWORK_DEFAULT": "false"},
)
```

The smoke test should confirm:

- `tools_count == 10`
- tool names match `references/geomine.mcp.example.json`
- `normalize_aoi` can be called
- `search_canada_geodata` can be called
- a direct empty-stdin launch writes zero bytes to stdout

## 9. Future Live Adapter Gates

Before turning on real retrieval for any source:

1. Add fixture-backed parsers for the source.
2. Add bounded live tests behind `GEOMINE_RUN_LIVE_TESTS=1`.
3. Require explicit `allow_network=True`.
4. Set timeouts, user agent, row limits, and cache strategy.
5. Preserve source URL, retrieval timestamp, license, and limitations.
6. Keep unsupported or unstable public APIs as `unsupported`, not inferred live results.
