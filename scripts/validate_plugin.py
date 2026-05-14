#!/usr/bin/env python3
"""Validate the GeoMine Research Codex plugin package."""

from __future__ import annotations

import json
import sys
from pathlib import Path
import tomllib


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_SKILLS = [
    ("skills/geomine-research-router-skill", "geomine-research-router-skill"),
    ("skills/geomine-visualization-studio-skill", "geomine-visualization-studio-skill"),
    ("skills/geomine-paper-pdf-export-skill", "geomine-paper-pdf-export-skill"),
    ("skills/academic-paper-research-writer", "academic-paper-research-writer"),
    ("skills/academic-geochemistry-paper-architect", "academic-geochemistry-paper-architect"),
    ("skills/figure-generation/academic-figure-package-skill", "academic-figure-package-skill"),
    ("skills/phreeqc-modeling-skill", "phreeqc-modeling-skill"),
    ("skills/pflotran-modeling/pflotran-router-skill", "pflotran-router-skill"),
    ("skills/pflotran-modeling/pflotran-conceptual-model-skill", "pflotran-conceptual-model-skill"),
    ("skills/pflotran-modeling/pflotran-input-deck-skill", "pflotran-input-deck-skill"),
    ("skills/pflotran-modeling/pflotran-grid-material-skill", "pflotran-grid-material-skill"),
    ("skills/pflotran-modeling/pflotran-flow-transport-skill", "pflotran-flow-transport-skill"),
    ("skills/pflotran-modeling/pflotran-chemistry-skill", "pflotran-chemistry-skill"),
    ("skills/pflotran-modeling/pflotran-thc-skill", "pflotran-thc-skill"),
    ("skills/pflotran-modeling/pflotran-geomechanics-skill", "pflotran-geomechanics-skill"),
    ("skills/pflotran-modeling/pflotran-run-management-skill", "pflotran-run-management-skill"),
    ("skills/pflotran-modeling/pflotran-output-analysis-skill", "pflotran-output-analysis-skill"),
    ("skills/pflotran-modeling/pflotran-calibration-validation-skill", "pflotran-calibration-validation-skill"),
    ("skills/pflotran-modeling/pflotran-paper-synthesis-skill", "pflotran-paper-synthesis-skill"),
    ("skills/thmc-modeling/thmc-groundwater-router-skill", "thmc-groundwater-router-skill"),
    ("skills/thmc-modeling/conceptual-thmc-model-skill", "conceptual-thmc-model-skill"),
    ("skills/thmc-modeling/governing-equations-skill", "governing-equations-skill"),
    ("skills/thmc-modeling/hydro-transport-skill", "hydro-transport-skill"),
    ("skills/thmc-modeling/geochemical-reaction-network-skill", "geochemical-reaction-network-skill"),
    ("skills/thmc-modeling/thermal-gradient-heat-transport-skill", "thermal-gradient-heat-transport-skill"),
    ("skills/thmc-modeling/mechanical-damage-permeability-skill", "mechanical-damage-permeability-skill"),
    ("skills/thmc-modeling/solver-selection-skill", "solver-selection-skill"),
    ("skills/thmc-modeling/dgr-field-data-acquisition-skill", "dgr-field-data-acquisition-skill"),
    ("skills/thmc-modeling/phreeqc-coupling-skill", "phreeqc-coupling-skill"),
    ("skills/thmc-modeling/ogs-pflotran-remote-run-skill", "ogs-pflotran-remote-run-skill"),
    ("skills/thmc-modeling/reactive-transport-implementation-skill", "reactive-transport-implementation-skill"),
    ("skills/thmc-modeling/calibration-validation-skill", "calibration-validation-skill"),
    ("skills/thmc-modeling/uncertainty-sensitivity-skill", "uncertainty-sensitivity-skill"),
    ("skills/thmc-modeling/thmc-paper-figure-skill", "thmc-paper-figure-skill"),
    ("skills/thmc-modeling/thmc-report-synthesis-skill", "thmc-report-synthesis-skill"),
    ("skills/research-router-skill", "research-router-skill"),
    ("skills/aoi-crs-normalizer-skill", "aoi-crs-normalizer-skill"),
    ("skills/geodata-discovery-skill", "geodata-discovery-skill"),
    ("skills/geochemical-survey-skill", "geochemical-survey-skill"),
    ("skills/mineral-occurrence-skill", "mineral-occurrence-skill"),
    ("skills/deposit-model-skill", "deposit-model-skill"),
    ("skills/ni43-101-disclosure-check-skill", "ni43-101-disclosure-check-skill"),
    ("skills/report-synthesis-skill", "report-synthesis-skill"),
]
REQUIRED_FILES = [
    ".codex-plugin/plugin.json",
    "MCP_SETUP.md",
    "references/data-sources-canada.md",
    "references/evidence-grading.md",
    "references/entity-schema.md",
    "references/evidence-matrix-template.md",
    "references/deposit-model-cheatsheet.md",
    "references/ni43-101-cim-boundary.md",
    "references/output-contracts.md",
    "references/mcp-roadmap.md",
    "references/adapter-mcp-design.md",
    "references/runnable-mcp-server-build-guide.md",
    "references/geomine.mcp.example.json",
    "references/geomine-thmc.mcp.example.json",
    "references/geomine-thmc-data.mcp.example.json",
    "references/geomine-pflotran.mcp.example.json",
    "references/visualization-studio-design.md",
    "examples/visualization-uranium-basin-scene.json",
    "skills/academic-paper-research-writer/SKILL.md",
    "skills/academic-paper-research-writer/prompts/system.md",
    "skills/academic-paper-research-writer/prompts/research_framing.md",
    "skills/academic-paper-research-writer/prompts/literature_review.md",
    "skills/academic-paper-research-writer/prompts/mechanistic_reasoning.md",
    "skills/academic-paper-research-writer/prompts/equation_derivation.md",
    "skills/academic-paper-research-writer/prompts/evidence_synthesis.md",
    "skills/academic-paper-research-writer/prompts/academic_writing.md",
    "skills/academic-paper-research-writer/prompts/citation_style.md",
    "skills/academic-paper-research-writer/prompts/peer_review_check.md",
    "skills/academic-paper-research-writer/schemas/input.schema.json",
    "skills/academic-paper-research-writer/schemas/output.schema.json",
    "skills/academic-paper-research-writer/schemas/paper_plan.schema.json",
    "skills/academic-paper-research-writer/schemas/evidence_matrix.schema.json",
    "skills/academic-paper-research-writer/schemas/equation_registry.schema.json",
    "skills/academic-paper-research-writer/examples/porous_media_radiolysis_paper.md",
    "skills/academic-paper-research-writer/examples/uranium_groundwater_migration_paper.md",
    "skills/academic-paper-research-writer/examples/geochem_anomaly_paper.md",
    "skills/academic-paper-research-writer/examples/gis_mineral_targeting_paper.md",
    "skills/academic-paper-research-writer/tests/test_skill_manifest.py",
    "skills/academic-paper-research-writer/tests/test_output_schema.py",
    "skills/academic-paper-research-writer/tests/test_required_sections.py",
    "skills/academic-paper-research-writer/tests/test_citation_rules.py",
    "skills/academic-paper-research-writer/tests/test_equation_registry.py",
    "skills/academic-geochemistry-paper-architect/SKILL.md",
    "skills/academic-geochemistry-paper-architect/prompts/paper_architect.md",
    "skills/academic-geochemistry-paper-architect/references/paper-type-taxonomy.md",
    "skills/academic-geochemistry-paper-architect/references/section-writing-rules.md",
    "skills/academic-geochemistry-paper-architect/references/data-method-qaqc-rules.md",
    "skills/academic-geochemistry-paper-architect/references/figure-table-architecture.md",
    "skills/academic-geochemistry-paper-architect/references/citation-uncertainty-guardrails.md",
    "skills/academic-geochemistry-paper-architect/templates/geochemistry-paper-architecture-template.md",
    "skills/academic-geochemistry-paper-architect/templates/quality-checklist-template.md",
    "skills/academic-geochemistry-paper-architect/schemas/input.schema.json",
    "skills/academic-geochemistry-paper-architect/schemas/output.schema.json",
    "skills/academic-geochemistry-paper-architect/scripts/generate_paper_architecture.py",
    "skills/academic-geochemistry-paper-architect/examples/hydrogeochemistry-uranium-groundwater.md",
    "skills/academic-geochemistry-paper-architect/examples/mineral-exploration-saskatchewan-uranium.md",
    "skills/academic-geochemistry-paper-architect/examples/radiolysis-nuclear-geochemistry.md",
    "skills/academic-geochemistry-paper-architect/examples/geochemical-database-paper.md",
    "skills/academic-geochemistry-paper-architect/examples/petrogenesis-isotope-paper.md",
    "skills/figure-generation/academic-figure-package-skill/SKILL.md",
    "skills/figure-generation/academic-figure-package-skill/README.md",
    "skills/figure-generation/academic-figure-package-skill/references/figure-types.md",
    "skills/figure-generation/academic-figure-package-skill/references/visual-grammar.md",
    "skills/figure-generation/academic-figure-package-skill/references/vector-vs-raster.md",
    "skills/figure-generation/academic-figure-package-skill/references/color-accessibility.md",
    "skills/figure-generation/academic-figure-package-skill/references/publication-checklist.md",
    "skills/figure-generation/academic-figure-package-skill/references/caption-writing-rules.md",
    "skills/figure-generation/academic-figure-package-skill/references/data-visualization-rules.md",
    "skills/figure-generation/academic-figure-package-skill/references/gis-map-figure-rules.md",
    "skills/figure-generation/academic-figure-package-skill/references/geochemistry-figure-rules.md",
    "skills/figure-generation/academic-figure-package-skill/references/mining-exploration-figure-rules.md",
    "skills/figure-generation/academic-figure-package-skill/references/radionuclide-migration-figure-rules.md",
    "skills/figure-generation/academic-figure-package-skill/references/ni43-101-technical-figure-caveats.md",
    "skills/figure-generation/academic-figure-package-skill/templates/figure-package-template.md",
    "skills/figure-generation/academic-figure-package-skill/templates/figure-inventory-template.md",
    "skills/figure-generation/academic-figure-package-skill/templates/figure-spec-template.md",
    "skills/figure-generation/academic-figure-package-skill/templates/multi-panel-layout-template.md",
    "skills/figure-generation/academic-figure-package-skill/templates/drawing-prompt-template.md",
    "skills/figure-generation/academic-figure-package-skill/templates/caption-template.md",
    "skills/figure-generation/academic-figure-package-skill/templates/figure-manifest-template.json",
    "skills/figure-generation/academic-figure-package-skill/templates/publication-checklist-template.md",
    "skills/figure-generation/academic-figure-package-skill/templates/geomine-figure-package-template.md",
    "skills/figure-generation/academic-figure-package-skill/scripts/validate_figure_package.py",
    "skills/figure-generation/academic-figure-package-skill/scripts/build_figure_manifest.py",
    "skills/figure-generation/academic-figure-package-skill/scripts/generate_mermaid_from_spec.py",
    "skills/figure-generation/academic-figure-package-skill/scripts/check_color_accessibility.py",
    "skills/figure-generation/academic-figure-package-skill/scripts/check_image_resolution.py",
    "skills/figure-generation/academic-figure-package-skill/scripts/scaffold_matplotlib_figure.py",
    "skills/figure-generation/academic-figure-package-skill/scripts/scaffold_qgis_layout_plan.py",
    "skills/figure-generation/academic-figure-package-skill/examples/uranium-groundwater-figure-package.md",
    "skills/figure-generation/academic-figure-package-skill/examples/geochemical-anomaly-map-figure-package.md",
    "skills/figure-generation/academic-figure-package-skill/examples/mining-project-study-area-map-package.md",
    "skills/figure-generation/academic-figure-package-skill/examples/geomine-ai-workflow-figure-package.md",
    "skills/phreeqc-modeling-skill/SKILL.md",
    "skills/phreeqc-modeling-skill/references/phreeqc-keywords.md",
    "skills/phreeqc-modeling-skill/references/phreeqc-database-selection.md",
    "skills/phreeqc-modeling-skill/references/groundwater-chemistry-data-schema.md",
    "skills/phreeqc-modeling-skill/references/uranium-radionuclide-reaction-patterns.md",
    "skills/phreeqc-modeling-skill/references/acid-mine-drainage-reaction-patterns.md",
    "skills/phreeqc-modeling-skill/references/tailings-seepage-reaction-patterns.md",
    "skills/phreeqc-modeling-skill/references/phreeqc-paper-methods-writing.md",
    "skills/phreeqc-modeling-skill/templates/phreeqc-modeling-package-template.md",
    "skills/phreeqc-modeling-skill/templates/solution-template.phr",
    "skills/phreeqc-modeling-skill/templates/equilibrium-phases-template.phr",
    "skills/phreeqc-modeling-skill/templates/kinetics-template.phr",
    "skills/phreeqc-modeling-skill/templates/surface-complexation-template.phr",
    "skills/phreeqc-modeling-skill/templates/exchange-template.phr",
    "skills/phreeqc-modeling-skill/templates/transport-1d-template.phr",
    "skills/phreeqc-modeling-skill/templates/selected-output-template.phr",
    "skills/phreeqc-modeling-skill/templates/paper-methods-template.md",
    "skills/phreeqc-modeling-skill/scripts/validate_water_chemistry_table.py",
    "skills/phreeqc-modeling-skill/scripts/build_solution_block.py",
    "skills/phreeqc-modeling-skill/scripts/generate_selected_output.py",
    "skills/phreeqc-modeling-skill/scripts/parse_selected_output.py",
    "skills/phreeqc-modeling-skill/scripts/make_phreeqc_run_manifest.py",
    "skills/phreeqc-modeling-skill/examples/phreeqc-uranium-groundwater.md",
    "skills/phreeqc-modeling-skill/examples/phreeqc-acid-mine-drainage.md",
    "skills/phreeqc-modeling-skill/examples/phreeqc-tailings-seepage.md",
    "skills/pflotran-modeling/README.md",
    "skills/pflotran-modeling/pflotran-router-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-conceptual-model-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-input-deck-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-input-deck-skill/templates/pflotran-input-deck-skeleton.in",
    "skills/pflotran-modeling/pflotran-input-deck-skill/templates/subsurface-flow-template.in",
    "skills/pflotran-modeling/pflotran-input-deck-skill/templates/reactive-transport-template.in",
    "skills/pflotran-modeling/pflotran-input-deck-skill/templates/thermal-hydrologic-template.in",
    "skills/pflotran-modeling/pflotran-input-deck-skill/templates/chemistry-template.in",
    "skills/pflotran-modeling/pflotran-input-deck-skill/templates/output-template.in",
    "skills/pflotran-modeling/pflotran-grid-material-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-grid-material-skill/templates/structured-grid-template.md",
    "skills/pflotran-modeling/pflotran-grid-material-skill/templates/material-property-table-template.csv",
    "skills/pflotran-modeling/pflotran-grid-material-skill/templates/region-definition-template.md",
    "skills/pflotran-modeling/pflotran-flow-transport-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-flow-transport-skill/references/flow-transport-mode-selection.md",
    "skills/pflotran-modeling/pflotran-flow-transport-skill/references/boundary-condition-patterns.md",
    "skills/pflotran-modeling/pflotran-flow-transport-skill/references/transport-configuration-rules.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/references/chemistry-block-rules.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/references/thermodynamic-database-rules.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/references/mineral-reaction-patterns.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/references/sorption-ion-exchange-patterns.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/references/uranium-reactive-transport-pattern.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/references/acid-mine-drainage-pattern.md",
    "skills/pflotran-modeling/pflotran-chemistry-skill/references/tailings-seepage-pattern.md",
    "skills/pflotran-modeling/pflotran-thc-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-thc-skill/references/thermal-hydrologic-chemical-coupling.md",
    "skills/pflotran-modeling/pflotran-thc-skill/references/temperature-dependent-chemistry.md",
    "skills/pflotran-modeling/pflotran-thc-skill/references/heat-source-boundary-patterns.md",
    "skills/pflotran-modeling/pflotran-geomechanics-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-geomechanics-skill/references/geomechanics-scope-and-limits.md",
    "skills/pflotran-modeling/pflotran-geomechanics-skill/references/porosity-permeability-feedback.md",
    "skills/pflotran-modeling/pflotran-geomechanics-skill/references/biot-coupling-notes.md",
    "skills/pflotran-modeling/pflotran-run-management-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-run-management-skill/scripts/build_run_manifest.py",
    "skills/pflotran-modeling/pflotran-run-management-skill/scripts/validate_input_deck.py",
    "skills/pflotran-modeling/pflotran-run-management-skill/scripts/make_run_command.py",
    "skills/pflotran-modeling/pflotran-output-analysis-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-output-analysis-skill/scripts/parse_observation_output.py",
    "skills/pflotran-modeling/pflotran-output-analysis-skill/scripts/build_result_summary.py",
    "skills/pflotran-modeling/pflotran-output-analysis-skill/scripts/generate_output_manifest.py",
    "skills/pflotran-modeling/pflotran-calibration-validation-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-paper-synthesis-skill/SKILL.md",
    "skills/pflotran-modeling/pflotran-paper-synthesis-skill/templates/pflotran-modeling-package-template.md",
    "skills/pflotran-modeling/pflotran-paper-synthesis-skill/templates/methods-section-template.md",
    "skills/pflotran-modeling/pflotran-paper-synthesis-skill/templates/results-section-template.md",
    "skills/pflotran-modeling/pflotran-paper-synthesis-skill/templates/model-limitations-template.md",
    "skills/pflotran-modeling/pflotran-paper-synthesis-skill/templates/machine-readable-model-manifest-schema.json",
    "skills/pflotran-modeling/examples/pflotran-tailings-seepage.md",
    "skills/pflotran-modeling/examples/pflotran-uranium-reactive-transport.md",
    "skills/pflotran-modeling/examples/pflotran-thc-geothermal-groundwater.md",
    "skills/thmc-modeling/README.md",
    "skills/thmc-modeling/thmc-groundwater-router-skill/SKILL.md",
    "skills/thmc-modeling/conceptual-thmc-model-skill/SKILL.md",
    "skills/thmc-modeling/conceptual-thmc-model-skill/templates/conceptual-model-template.md",
    "skills/thmc-modeling/conceptual-thmc-model-skill/templates/coupling-matrix-template.md",
    "skills/thmc-modeling/governing-equations-skill/SKILL.md",
    "skills/thmc-modeling/governing-equations-skill/references/thmc-equation-library.md",
    "skills/thmc-modeling/governing-equations-skill/references/variable-parameter-glossary.md",
    "skills/thmc-modeling/hydro-transport-skill/SKILL.md",
    "skills/thmc-modeling/hydro-transport-skill/references/groundwater-flow-transport.md",
    "skills/thmc-modeling/hydro-transport-skill/references/fracture-flow-matrix-diffusion.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/SKILL.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/references/uranium-series-reaction-network.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/references/acid-mine-drainage-reaction-network.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/references/tailings-seepage-reaction-network.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/references/bentonite-buffer-reaction-network.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/references/geothermal-water-rock-reaction-network.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/templates/phreeqc-reaction-network-draft.md",
    "skills/thmc-modeling/geochemical-reaction-network-skill/templates/reaction-network-table-template.md",
    "skills/thmc-modeling/thermal-gradient-heat-transport-skill/SKILL.md",
    "skills/thmc-modeling/thermal-gradient-heat-transport-skill/references/thermal-transport-and-temperature-effects.md",
    "skills/thmc-modeling/mechanical-damage-permeability-skill/SKILL.md",
    "skills/thmc-modeling/mechanical-damage-permeability-skill/references/stress-permeability-porosity-laws.md",
    "skills/thmc-modeling/mechanical-damage-permeability-skill/references/fracture-aperture-evolution.md",
    "skills/thmc-modeling/solver-selection-skill/SKILL.md",
    "skills/thmc-modeling/solver-selection-skill/references/solver-route-comparison.md",
    "skills/thmc-modeling/solver-selection-skill/references/comsol-phreeqc-route.md",
    "skills/thmc-modeling/solver-selection-skill/references/ogs-phreeqc-route.md",
    "skills/thmc-modeling/solver-selection-skill/references/pflotran-route.md",
    "skills/thmc-modeling/solver-selection-skill/references/python-phreeqc-route.md",
    "skills/thmc-modeling/solver-selection-skill/references/pinn-surrogate-route.md",
    "skills/thmc-modeling/dgr-field-data-acquisition-skill/SKILL.md",
    "skills/thmc-modeling/phreeqc-coupling-skill/SKILL.md",
    "skills/thmc-modeling/ogs-pflotran-remote-run-skill/SKILL.md",
    "skills/thmc-modeling/reactive-transport-implementation-skill/SKILL.md",
    "skills/thmc-modeling/reactive-transport-implementation-skill/templates/implementation-plan-template.md",
    "skills/thmc-modeling/reactive-transport-implementation-skill/templates/model-input-manifest-template.md",
    "skills/thmc-modeling/calibration-validation-skill/SKILL.md",
    "skills/thmc-modeling/calibration-validation-skill/templates/calibration-validation-plan-template.md",
    "skills/thmc-modeling/calibration-validation-skill/templates/benchmark-selection-template.md",
    "skills/thmc-modeling/uncertainty-sensitivity-skill/SKILL.md",
    "skills/thmc-modeling/uncertainty-sensitivity-skill/templates/sensitivity-analysis-plan-template.md",
    "skills/thmc-modeling/uncertainty-sensitivity-skill/templates/uncertainty-analysis-plan-template.md",
    "skills/thmc-modeling/thmc-paper-figure-skill/SKILL.md",
    "skills/thmc-modeling/thmc-paper-figure-skill/templates/thmc-figure-plan-template.md",
    "skills/thmc-modeling/thmc-report-synthesis-skill/SKILL.md",
    "skills/thmc-modeling/thmc-report-synthesis-skill/templates/thmc-modeling-package-template.md",
    "skills/thmc-modeling/thmc-report-synthesis-skill/templates/thmc-model-spec-schema.json",
    "skills/thmc-modeling/templates/thmc-modeling-package-2.0-template.md",
    "skills/thmc-modeling/templates/thmc-model-spec.schema.json",
    "skills/thmc-modeling/templates/thmc-run-record.schema.json",
    "skills/thmc-modeling/templates/thmc-parameter-table-template.csv",
    "skills/thmc-modeling/templates/thmc-reaction-network-template.md",
    "references/thmc-modeling/thmc-scenario-taxonomy.md",
    "references/thmc-modeling/thmc-coupling-map.md",
    "references/thmc-modeling/thmc-evidence-and-data-requirements.md",
    "references/thmc-modeling/thmc-modeling-limitations.md",
    "references/thmc-modeling/thmc-publication-caveats.md",
    "tests/validate_thmc_skill_family.py",
    "tests/test_thmc_skill_family.py",
    "scripts/geomine/evidence_schema.py",
    "scripts/geomine/data_sources.py",
    "scripts/geomine/aoi.py",
    "scripts/geomine/geochem.py",
    "scripts/geomine/occurrences.py",
    "scripts/geomine/reports.py",
    "scripts/geomine/tools.py",
    "scripts/geomine_mcp_server.py",
    "scripts/run_mcp_sample_cases.py",
    "scripts/install_thmc_mcp_dev.sh",
    "scripts/install_thmc_data_mcp_dev.sh",
    "scripts/check_thmc_mcp.sh",
    "scripts/test_thmc_mcp_tools.py",
    "scripts/test_thmc_data_mcp_tools.py",
    "scripts/test_pflotran_mcp_tools.py",
    "scripts/generate_thmc_mock_data.py",
    "scripts/geomine/adapters/__init__.py",
    "scripts/geomine/adapters/base.py",
    "scripts/geomine/adapters/ckan.py",
    "scripts/geomine/adapters/arcgis.py",
    "scripts/geomine/adapters/source_registry.py",
    "skills/geomine-visualization-studio-skill/scripts/create_geomine_visualization.py",
    "skills/geomine-paper-pdf-export-skill/scripts/build_pdf_with_math.py",
    "tests/test_mcp_tools.py",
    "tests/test_mcp_server_import.py",
    "tests/validate_thmc_mcp_config.py",
    "tests/test_thmc_mcp_config.py",
    "mcp/geomine-thmc-server/pyproject.toml",
    "mcp/geomine-thmc-server/README.md",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/__init__.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/server.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/data_server.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/pflotran_server.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/config.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/auth.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/schemas.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/storage.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/provenance.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/project_database.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/water_chemistry.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/lithology_mineralogy.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/r2_postgis.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/phreeqc_service.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/remote_compute.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/pflotran_modeling.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/model_registry.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/run_records.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tools/dgr_data_collection.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/clients/openmine_api_client.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/clients/postgis_client.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/clients/r2_client.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/clients/phreeqc_client.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/clients/compute_client.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/adapters/phreeqc_input_builder.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/adapters/ogs_project_builder.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/adapters/pflotran_input_builder.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tests/test_tools_schema.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tests/test_mock_project_database.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tests/test_mock_phreeqc.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tests/test_run_records.py",
    "mcp/geomine-thmc-server/src/geomine_thmc_mcp/tests/test_dgr_data_collection.py",
    "README.md",
    "AGENTS.md",
    "CHANGELOG.md",
    "THMC_MODELING_GUIDE.md",
    "THMC_MCP_INTEGRATION_GUIDE.md",
    "MCP_TROUBLESHOOTING.md",
    "pyproject.toml",
]
EXPECTED_MCP_TOOLS = [
    "normalize_aoi",
    "search_canada_geodata",
    "search_cdogs_surveys",
    "search_bc_minfile",
    "search_ontario_omi",
    "search_saskatchewan_mineral_data",
    "fetch_dataset_metadata",
    "summarize_dataset_provenance",
    "query_claim_neighbors",
    "calculate_infrastructure_distance",
]
EXPECTED_THMC_MCP_TOOLS = [
    "list_openmine_projects",
    "get_openmine_project",
    "get_project_aoi",
    "query_water_chemistry_samples",
    "query_lithology_units",
    "query_mineral_assemblages",
    "get_thmc_mesh_catalog",
    "fetch_mesh_or_parameter_field",
    "build_phreeqc_input",
    "run_phreeqc_job",
    "submit_ogs_job",
    "submit_pflotran_job",
    "get_compute_job_status",
    "fetch_compute_job_results",
    "save_thmc_model_version",
    "get_thmc_model_version",
    "list_thmc_model_versions",
    "save_thmc_run_record",
    "get_thmc_run_record",
    "list_thmc_run_records",
]
EXPECTED_THMC_DATA_MCP_TOOLS = [
    "list_dgr_data_campaigns",
    "get_dgr_data_campaign",
    "register_dgr_borehole",
    "ingest_dgr_sensor_timeseries",
    "ingest_dgr_water_sample",
    "ingest_dgr_rock_core_measurement",
    "ingest_dgr_packer_test",
    "ingest_dgr_in_situ_stress",
    "validate_dgr_thmc_dataset",
    "build_dgr_calibration_dataset",
    "save_dgr_data_package",
    "get_dgr_data_package",
    "list_dgr_data_packages",
]
EXPECTED_PFLOTRAN_MCP_TOOLS = [
    "validate_input_deck",
    "build_input_deck",
    "build_run_manifest",
    "parse_observation_output",
    "generate_result_summary",
    "save_model_package",
    "get_model_package",
    "list_model_packages",
]


def _failures() -> list[str]:
    errors: list[str] = []
    manifest_path = ROOT / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - validation should report context.
        return [f"Cannot read manifest: {exc}"]

    if manifest.get("name") != "geo-mining-research":
        errors.append("manifest name must be geo-mining-research")
    if manifest.get("version") != "0.2.0":
        errors.append("manifest version must be 0.2.0")
    if "skills" in manifest:
        errors.append("manifest must not auto-register skills by default")
    if "mcpServers" in manifest:
        errors.append("manifest must not auto-register MCP servers by default")
    if manifest.get("interface", {}).get("displayName") != "GeoMine Research":
        errors.append("interface.displayName must be GeoMine Research")

    mcp_path = ROOT / ".mcp.json"
    if mcp_path.exists():
        errors.append(".mcp.json must not exist at the plugin root by default")

    mcp_example_path = ROOT / "references" / "geomine.mcp.example.json"
    if mcp_example_path.exists():
        try:
            mcp_config = json.loads(mcp_example_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation should report context.
            errors.append(f"Cannot read MCP example config: {exc}")
        else:
            geomine = mcp_config.get("geomine")
            if not isinstance(geomine, dict):
                errors.append("MCP example config must define a geomine server")
            else:
                if geomine.get("command") != "uv":
                    errors.append("MCP example geomine.command must be uv")
                if "--no-project" not in geomine.get("args", []):
                    errors.append("MCP example geomine.args must include --no-project")
                if geomine.get("enabled") is not False:
                    errors.append("MCP example geomine.enabled must be false by default")
                if geomine.get("required") is not False:
                    errors.append("MCP example geomine.required must be false")
                enabled_tools = geomine.get("enabled_tools")
                if enabled_tools != EXPECTED_MCP_TOOLS:
                    errors.append("MCP example enabled_tools must match expected GeoMine MCP tools")

    thmc_mcp_example_path = ROOT / "references" / "geomine-thmc.mcp.example.json"
    if thmc_mcp_example_path.exists():
        try:
            thmc_config = json.loads(thmc_mcp_example_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation should report context.
            errors.append(f"Cannot read THMC MCP example config: {exc}")
        else:
            geomine_thmc = thmc_config.get("geomine_thmc")
            if not isinstance(geomine_thmc, dict):
                errors.append("THMC MCP example config must define a geomine_thmc server")
            else:
                if geomine_thmc.get("command") != "uv":
                    errors.append("THMC MCP example geomine_thmc.command must be uv")
                if geomine_thmc.get("args") != ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-thmc-mcp"]:
                    errors.append("THMC MCP example geomine_thmc.args mismatch")
                if geomine_thmc.get("enabled") is not False:
                    errors.append("THMC MCP example geomine_thmc.enabled must be false by default")
                if geomine_thmc.get("required") is not False:
                    errors.append("THMC MCP example geomine_thmc.required must be false")
                enabled_tools = geomine_thmc.get("enabled_tools")
                if enabled_tools != EXPECTED_THMC_MCP_TOOLS:
                    errors.append("THMC MCP example enabled_tools must match expected tools")

    thmc_data_mcp_example_path = ROOT / "references" / "geomine-thmc-data.mcp.example.json"
    if thmc_data_mcp_example_path.exists():
        try:
            thmc_data_config = json.loads(thmc_data_mcp_example_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation should report context.
            errors.append(f"Cannot read THMC data MCP example config: {exc}")
        else:
            geomine_thmc_data = thmc_data_config.get("geomine_thmc_data")
            if not isinstance(geomine_thmc_data, dict):
                errors.append("THMC data MCP example config must define a geomine_thmc_data server")
            else:
                if geomine_thmc_data.get("command") != "uv":
                    errors.append("THMC data MCP example geomine_thmc_data.command must be uv")
                if geomine_thmc_data.get("args") != ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-thmc-data-mcp"]:
                    errors.append("THMC data MCP example geomine_thmc_data.args mismatch")
                if geomine_thmc_data.get("enabled") is not False:
                    errors.append("THMC data MCP example geomine_thmc_data.enabled must be false by default")
                if geomine_thmc_data.get("required") is not False:
                    errors.append("THMC data MCP example geomine_thmc_data.required must be false")
                enabled_tools = geomine_thmc_data.get("enabled_tools")
                if enabled_tools != EXPECTED_THMC_DATA_MCP_TOOLS:
                    errors.append("THMC data MCP example enabled_tools must match expected tools")

    pflotran_mcp_example_path = ROOT / "references" / "geomine-pflotran.mcp.example.json"
    if pflotran_mcp_example_path.exists():
        try:
            pflotran_config = json.loads(pflotran_mcp_example_path.read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001 - validation should report context.
            errors.append(f"Cannot read PFLOTRAN MCP example config: {exc}")
        else:
            geomine_pflotran = pflotran_config.get("geomine_pflotran")
            if not isinstance(geomine_pflotran, dict):
                errors.append("PFLOTRAN MCP example config must define a geomine_pflotran server")
            else:
                if geomine_pflotran.get("command") != "uv":
                    errors.append("PFLOTRAN MCP example geomine_pflotran.command must be uv")
                if geomine_pflotran.get("args") != ["--directory", "./mcp/geomine-thmc-server", "run", "geomine-pflotran-mcp"]:
                    errors.append("PFLOTRAN MCP example geomine_pflotran.args mismatch")
                if geomine_pflotran.get("enabled") is not False:
                    errors.append("PFLOTRAN MCP example geomine_pflotran.enabled must be false by default")
                if geomine_pflotran.get("required") is not False:
                    errors.append("PFLOTRAN MCP example geomine_pflotran.required must be false")
                enabled_tools = geomine_pflotran.get("enabled_tools")
                if enabled_tools != EXPECTED_PFLOTRAN_MCP_TOOLS:
                    errors.append("PFLOTRAN MCP example enabled_tools must match expected tools")

    for rel_path in REQUIRED_FILES:
        if not (ROOT / rel_path).exists():
            errors.append(f"missing required file: {rel_path}")

    pyproject_path = ROOT / "pyproject.toml"
    if pyproject_path.exists():
        try:
            pyproject = tomllib.loads(pyproject_path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid pyproject.toml: {exc}")
        else:
            project = pyproject.get("project", {})
            dependencies = set(project.get("dependencies", []))
            if project.get("version") != "0.2.0":
                errors.append("pyproject version must be 0.2.0")
            if "mcp[cli]>=1.2.0" not in dependencies:
                errors.append("pyproject dependencies must include mcp[cli]>=1.2.0")
            if "httpx>=0.28.0" not in dependencies:
                errors.append("pyproject dependencies must include httpx>=0.28.0")
            scripts = project.get("scripts", {})
            if scripts.get("geomine-mcp") != "geomine_mcp_server:main":
                errors.append("pyproject must expose geomine-mcp = geomine_mcp_server:main")

    thmc_pyproject_path = ROOT / "mcp" / "geomine-thmc-server" / "pyproject.toml"
    if thmc_pyproject_path.exists():
        try:
            thmc_pyproject = tomllib.loads(thmc_pyproject_path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            errors.append(f"invalid THMC MCP pyproject.toml: {exc}")
        else:
            project = thmc_pyproject.get("project", {})
            dependencies = set(project.get("dependencies", []))
            scripts = project.get("scripts", {})
            if project.get("name") != "geomine-thmc-mcp":
                errors.append("THMC MCP pyproject name must be geomine-thmc-mcp")
            if project.get("version") != "0.2.0":
                errors.append("THMC MCP pyproject version must be 0.2.0")
            if "mcp[cli]>=1.2.0" not in dependencies:
                errors.append("THMC MCP dependencies must include mcp[cli]>=1.2.0")
            if "httpx>=0.28.0" not in dependencies:
                errors.append("THMC MCP dependencies must include httpx>=0.28.0")
            if scripts.get("geomine-thmc-mcp") != "geomine_thmc_mcp.server:main":
                errors.append("THMC MCP must expose geomine-thmc-mcp = geomine_thmc_mcp.server:main")
            if scripts.get("geomine-thmc-data-mcp") != "geomine_thmc_mcp.data_server:main":
                errors.append("THMC MCP must expose geomine-thmc-data-mcp = geomine_thmc_mcp.data_server:main")
            if scripts.get("geomine-pflotran-mcp") != "geomine_thmc_mcp.pflotran_server:main":
                errors.append("THMC MCP must expose geomine-pflotran-mcp = geomine_thmc_mcp.pflotran_server:main")

    for skill_dir, skill_name in REQUIRED_SKILLS:
        skill_path = ROOT / skill_dir / "SKILL.md"
        if not skill_path.exists():
            errors.append(f"missing skill: {skill_name}")
            continue
        text = skill_path.read_text(encoding="utf-8")
        frontmatter = _frontmatter(text)
        if frontmatter is None:
            errors.append(f"{skill_name} missing YAML frontmatter")
            continue
        if frontmatter.get("name") != skill_name:
            errors.append(f"{skill_name} frontmatter name mismatch")
        if not frontmatter.get("description"):
            errors.append(f"{skill_name} missing description")
    return errors


def _frontmatter(text: str) -> dict[str, str] | None:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    data: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            return data
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip().strip('"').strip("'")
    return None


def main() -> int:
    errors = _failures()
    if errors:
        print("GeoMine Research plugin validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("GeoMine Research plugin validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
