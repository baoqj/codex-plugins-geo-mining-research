"""PHREEQC draft and mock execution THMC MCP tools."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from ..adapters.phreeqc_input_builder import build_phreeqc_input_draft
from ..provenance import provenance
from ..schemas import now_iso, tool_response
from ..storage import THMCStorage, get_default_storage


def build_phreeqc_input(
    project_id: str,
    model_id: str,
    scenario: str = "uranium_mine_groundwater",
    sample_ids: list[str] | None = None,
    database: str = "phreeqc.dat",
    reaction_network: dict[str, Any] | None = None,
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    samples, sample_warnings = store.query_water_samples(project_id=project_id, analytes=["U", "Ra226", "Rn222"])
    if sample_ids:
        selected = set(sample_ids)
        samples = [sample for sample in samples if sample.get("sample_id") in selected]
    minerals = store.query_minerals(project_id=project_id)
    input_text, builder_warnings = build_phreeqc_input_draft(
        project_id=project_id,
        model_id=model_id,
        scenario=scenario,
        water_samples=samples,
        mineral_assemblages=minerals,
        database=database,
        reaction_network=reaction_network,
    )
    asset = {
        "asset_id": f"phreeqc-input-{uuid4().hex[:10]}",
        "asset_type": "phreeqc_input",
        "name": f"{model_id}.phrq",
        "format": "text/phreeqc",
        "storage": "inline",
        "content": input_text,
        "checksum": f"length:{len(input_text)}",
        "created_at": now_iso(),
    }
    return tool_response(
        tool="build_phreeqc_input",
        query={
            "project_id": project_id,
            "model_id": model_id,
            "scenario": scenario,
            "sample_ids": sample_ids,
            "database": database,
        },
        mode="mock",
        results=[{"database": database, "sample_count": len(samples), "mineral_assemblage_count": len(minerals)}],
        assets=[asset],
        provenance=provenance("PHREEQC input builder", mode="mock", data_version="mock-2026-05-12"),
        warnings=sample_warnings + builder_warnings,
    )


def run_phreeqc_job(
    project_id: str,
    model_id: str,
    phreeqc_input: str | None = None,
    database: str = "phreeqc.dat",
    run_mode: str = "mock",
    storage: THMCStorage | None = None,
) -> dict[str, Any]:
    store = storage or get_default_storage()
    warnings = [
        "Mock PHREEQC execution; no external PHREEQC binary or thermodynamic database was run.",
        "Use results only to validate MCP workflow shape, not scientific interpretation.",
    ]
    if phreeqc_input is None:
        built = build_phreeqc_input(
            project_id=project_id,
            model_id=model_id,
            database=database,
            storage=store,
        )
        phreeqc_input = built["assets"][0]["content"] if built["assets"] else ""
        warnings.extend(built.get("warnings", []))
    job_id = f"phreeqc-job-{uuid4().hex[:10]}"
    selected_output = {
        "pH_range": [6.9, 7.2],
        "alkalinity_status": "mock_from_hco3",
        "saturation_indices": [
            {"phase": "Calcite", "range": [-0.2, 0.1], "interpretation": "near equilibrium; mock"},
            {"phase": "Goethite", "range": [0.4, 1.2], "interpretation": "potential sorption surface proxy; mock"},
            {"phase": "Barite", "range": [-1.0, -0.3], "interpretation": "not saturated in mock output"},
        ],
        "radionuclide_species": "not calculated; database/speciation mapping required",
    }
    output_asset = {
        "asset_id": f"phreeqc-output-{uuid4().hex[:10]}",
        "asset_type": "phreeqc_selected_output",
        "name": f"{job_id}-selected-output.json",
        "format": "json",
        "storage": "inline",
        "content": selected_output,
        "created_at": now_iso(),
    }
    return tool_response(
        tool="run_phreeqc_job",
        query={
            "project_id": project_id,
            "model_id": model_id,
            "database": database,
            "run_mode": run_mode,
        },
        mode="mock",
        results=[
            {
                "job_id": job_id,
                "status": "completed",
                "run_mode": "mock",
                "database": database,
                "input_length": len(phreeqc_input),
                "outputs": selected_output,
            }
        ],
        assets=[output_asset],
        provenance=provenance("PHREEQC mock service", mode="mock", solver="PHREEQC", solver_version="mock"),
        warnings=warnings,
    )
