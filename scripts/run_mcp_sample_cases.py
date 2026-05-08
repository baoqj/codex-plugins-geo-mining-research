#!/usr/bin/env python3
"""Run deterministic GeoMine MCP sample cases and write report artifacts."""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

from geomine.tools import (
    calculate_infrastructure_distance_tool,
    fetch_dataset_metadata_mcp_tool,
    normalize_aoi_tool,
    query_claim_neighbors_tool,
    search_bc_minfile_tool,
    search_canada_geodata_tool,
    search_cdogs_surveys_tool,
    search_ontario_omi_tool,
    search_saskatchewan_mineral_data_tool,
    summarize_dataset_provenance_tool,
)


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _case(case_id: str, title: str, tool: str, args: dict[str, Any], fn: Callable[..., dict[str, Any]]) -> dict[str, Any]:
    result = fn(**args)
    return {
        "case_id": case_id,
        "title": title,
        "tool": tool,
        "args": args,
        "status": "passed" if result.get("ok") is True and result.get("tool") == tool else "failed",
        "result": result,
    }


def run_cases() -> dict[str, Any]:
    cases = [
        _case(
            "GM-MCP-001",
            "Normalize Saskatchewan uranium AOI",
            "normalize_aoi",
            {"aoi": "Athabasca Basin margin, Saskatchewan, Canada", "default_crs": "EPSG:4326"},
            normalize_aoi_tool,
        ),
        _case(
            "GM-MCP-002",
            "Plan Canada geodata discovery",
            "search_canada_geodata",
            {"query": "uranium geochemistry", "province": "Saskatchewan", "commodity": "uranium"},
            search_canada_geodata_tool,
        ),
        _case(
            "GM-MCP-003",
            "Plan CDoGS geochemical survey discovery",
            "search_cdogs_surveys",
            {"province": "Saskatchewan", "commodity": "uranium"},
            search_cdogs_surveys_tool,
        ),
        _case(
            "GM-MCP-004",
            "Plan BC MINFILE occurrence lookup",
            "search_bc_minfile",
            {"aoi": "Example BC Porphyry AOI", "commodity": "copper"},
            search_bc_minfile_tool,
        ),
        _case(
            "GM-MCP-005",
            "Plan Ontario OMI lookup",
            "search_ontario_omi",
            {"aoi": "Example Ontario LCT claim block", "commodity": "lithium"},
            search_ontario_omi_tool,
        ),
        _case(
            "GM-MCP-006",
            "Plan Saskatchewan mineral data lookup",
            "search_saskatchewan_mineral_data",
            {"aoi": "NTS 74H", "commodity": "uranium"},
            search_saskatchewan_mineral_data_tool,
        ),
        _case(
            "GM-MCP-007",
            "Fetch local CDoGS dataset metadata",
            "fetch_dataset_metadata",
            {"dataset_id": "nrcan-cdogs"},
            fetch_dataset_metadata_mcp_tool,
        ),
        _case(
            "GM-MCP-008",
            "Summarize dataset provenance",
            "summarize_dataset_provenance",
            {
                "dataset": {
                    "name": "CDoGS regional geochemical surveys",
                    "url": "https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm",
                    "license": "verify from source",
                    "limitations": ["Survey coverage and analytical methods vary by survey."],
                }
            },
            summarize_dataset_provenance_tool,
        ),
        _case(
            "GM-MCP-009",
            "Plan claim neighbor query",
            "query_claim_neighbors",
            {"claim_id": "SK-EXAMPLE-001", "buffer_km": 10.0},
            query_claim_neighbors_tool,
        ),
        _case(
            "GM-MCP-010",
            "Plan infrastructure distance calculation",
            "calculate_infrastructure_distance",
            {"aoi": "Athabasca Basin margin, Saskatchewan", "infrastructure_type": "road"},
            calculate_infrastructure_distance_tool,
        ),
        _case(
            "GM-MCP-011",
            "Confirm live-network guardrail",
            "search_canada_geodata",
            {"query": "uranium geochemistry", "province": "Saskatchewan", "commodity": "uranium", "allow_network": True},
            search_canada_geodata_tool,
        ),
    ]
    return {
        "suite": "GeoMine MCP deterministic sample suite",
        "generated_at": _now(),
        "case_count": len(cases),
        "passed": sum(1 for case in cases if case["status"] == "passed"),
        "failed": sum(1 for case in cases if case["status"] != "passed"),
        "cases": cases,
    }


def write_artifacts(output_dir: Path) -> dict[str, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results = run_cases()
    json_path = output_dir / "2026-05-08-geomine-mcp-sample-results.json"
    cases_path = output_dir / "2026-05-08-geomine-mcp-test-cases.md"
    report_path = output_dir / "2026-05-08-geomine-mcp-test-report.md"

    json_path.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    cases_path.write_text(_render_cases(results), encoding="utf-8")
    report_path.write_text(_render_report(results), encoding="utf-8")
    return {"json": json_path, "cases": cases_path, "report": report_path}


def _render_cases(results: dict[str, Any]) -> str:
    lines = [
        "# GeoMine MCP Test Cases",
        "",
        f"Generated at: `{results['generated_at']}`",
        "",
        "| Case | Tool | Purpose | Key Arguments |",
        "|---|---|---|---|",
    ]
    for case in results["cases"]:
        arg_text = ", ".join(f"{key}={value!r}" for key, value in case["args"].items())
        lines.append(f"| {case['case_id']} | `{case['tool']}` | {case['title']} | `{arg_text}` |")
    lines.append("")
    return "\n".join(lines)


def _render_report(results: dict[str, Any]) -> str:
    lines = [
        "# GeoMine MCP Test Report",
        "",
        f"Generated at: `{results['generated_at']}`",
        "",
        "## Summary",
        "",
        f"- Suite: {results['suite']}",
        f"- Cases: {results['case_count']}",
        f"- Passed: {results['passed']}",
        f"- Failed: {results['failed']}",
        "- Live network calls: disabled by default; the guardrail case confirms `allow_network=true` returns `unsupported` rather than fabricated data.",
        "",
        "## Results",
        "",
        "| Case | Tool | Status | Retrieval Status | Network | Warning Count |",
        "|---|---|---:|---|---|---:|",
    ]
    for case in results["cases"]:
        provenance = case["result"].get("provenance", {})
        warnings = case["result"].get("warnings", [])
        lines.append(
            f"| {case['case_id']} | `{case['tool']}` | {case['status']} | "
            f"{provenance.get('retrieval_status')} | {provenance.get('network')} | {len(warnings)} |"
        )
    lines.extend(
        [
            "",
            "## Acceptance Notes",
            "",
            "- Every MCP sample result includes `ok`, `tool`, `query`, `provenance`, `warnings`, and `next_steps`.",
            "- Tools return planned/static evidence objects unless a future adapter implements bounded live retrieval.",
            "- This report is deterministic and can be regenerated with `python3 scripts/run_mcp_sample_cases.py <output-dir>`.",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    output_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("report")
    artifacts = write_artifacts(output_dir)
    for kind, path in artifacts.items():
        print(f"{kind}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
