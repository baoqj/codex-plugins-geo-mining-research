#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "GeoMine THMC DGR data acquisition MCP dev command:"
echo "codex mcp add geomine_thmc_data --env GEOMINE_THMC_MODE=mock -- uv --directory ${ROOT}/mcp/geomine-thmc-server run geomine-thmc-data-mcp"

if command -v codex >/dev/null 2>&1; then
  codex mcp add geomine_thmc_data \
    --env GEOMINE_THMC_MODE=mock \
    -- \
    uv \
    --directory "${ROOT}/mcp/geomine-thmc-server" \
    run \
    geomine-thmc-data-mcp
else
  echo "codex CLI not found; run the printed command manually."
fi
