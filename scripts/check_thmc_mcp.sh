#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

python3 -m json.tool references/geomine-thmc.mcp.example.json >/dev/null
python3 -m json.tool references/geomine-thmc-data.mcp.example.json >/dev/null
python3 -m json.tool references/geomine-pflotran.mcp.example.json >/dev/null
python3 tests/validate_thmc_mcp_config.py
python3 scripts/test_thmc_mcp_tools.py
python3 scripts/test_thmc_data_mcp_tools.py
python3 scripts/test_pflotran_mcp_tools.py
uv --directory mcp/geomine-thmc-server run --with pytest python -m pytest
