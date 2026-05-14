#!/usr/bin/env python3
"""Run direct GeoMine PFLOTRAN MCP planning-tool smoke checks."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
THMC_SRC = ROOT / "mcp" / "geomine-thmc-server" / "src"
sys.path.insert(0, str(THMC_SRC))

from geomine_thmc_mcp.storage import THMCStorage  # noqa: E402
from geomine_thmc_mcp.tools import (  # noqa: E402
    build_pflotran_input_deck,
    build_pflotran_result_summary,
    build_pflotran_run_manifest,
    get_pflotran_model_package,
    list_pflotran_model_packages,
    parse_pflotran_observation_output,
    save_pflotran_model_package,
    validate_pflotran_input_deck,
)


PROJECT_ID = "om-prj-uranium-001"
REQUIRED = {"ok", "mode", "tool", "query", "results", "assets", "provenance", "warnings", "errors"}


def assert_response(payload: dict, expected_tool: str) -> None:
    missing = REQUIRED.difference(payload)
    if missing:
        raise AssertionError(f"{expected_tool} missing keys: {sorted(missing)}")
    if payload["tool"] != expected_tool:
        raise AssertionError(f"{expected_tool} reported tool={payload['tool']}")
    if payload["mode"] != "mock":
        raise AssertionError(f"{expected_tool} should run in mock mode")
    if not payload["ok"]:
        raise AssertionError(f"{expected_tool} failed unexpectedly: {payload['errors']}")


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="geomine-pflotran-") as tmp:
        storage = THMCStorage(cache_dir=Path(tmp), mode="mock")
        responses: list[dict] = []
        deck = build_pflotran_input_deck(PROJECT_ID, "pflotran-model-001")
        input_deck = deck["results"][0]["input_deck"]
        responses.append(deck)
        responses.append(validate_pflotran_input_deck(input_deck))
        responses.append(build_pflotran_run_manifest("pflotran-model-001", input_file="pflotran-model-001.in", mpi_processes=4))
        parsed = parse_pflotran_observation_output("time,pH,U\n0,7.2,0.01\n1,7.1,0.02\n")
        responses.append(parsed)
        responses.append(build_pflotran_result_summary(parsed["results"][0]["rows"]))
        saved = save_pflotran_model_package(
            PROJECT_ID,
            "v0.1-smoke",
            {"scenario": "uranium_reactive_transport", "input_deck_status": "draft"},
            storage=storage,
        )
        package_id = saved["results"][0]["package_id"]
        responses.append(saved)
        responses.append(get_pflotran_model_package(package_id, storage=storage))
        responses.append(list_pflotran_model_packages(PROJECT_ID, storage=storage))

        for response in responses:
            assert_response(response, response["tool"])

        print(json.dumps({"ok": True, "tool_count": len({item["tool"] for item in responses}), "responses": len(responses)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
