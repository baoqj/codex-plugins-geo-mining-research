#!/usr/bin/env python3
"""Generate a deterministic first-pass geochemistry paper architecture."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PaperProfile:
    name: str
    keywords: tuple[str, ...]
    questions: tuple[str, ...]
    hypotheses: tuple[str, ...]
    data: tuple[str, ...]
    methods: tuple[str, ...]
    figures: tuple[str, ...]
    tables: tuple[str, ...]
    downstream: tuple[str, ...]


PROFILES: tuple[PaperProfile, ...] = (
    PaperProfile(
        "Data Paper / Database Paper",
        ("database", "compilation", "dataset", "schema", "sql", "csv", "metadata", "fair"),
        ("How can the geochemical dataset be standardized, quality-controlled, and reused?",),
        ("A provenance-tracked schema can reduce cross-source ambiguity and support repeatable geochemical interpretation.",),
        ("sample identifiers, coordinates, sample medium, analytes, units, methods, detection limits, source version, license, quality flags",),
        ("schema design", "unit normalization", "QA/QC flagging", "summary statistics", "data availability plan"),
        ("database schema diagram", "sample distribution map", "element coverage histogram", "QA/QC workflow"),
        ("field dictionary", "source/version table", "QA/QC rule table"),
        ("geodata-discovery-skill", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Regional Geochemical Characterization Paper",
        ("regional", "background", "soil", "sediment", "lake", "whole-rock", "spatial pattern", "lithology"),
        ("Which geochemical patterns characterize the region, and what geological controls explain them?",),
        ("Element distributions vary systematically with lithology, structure, alteration, or hydrological setting.",),
        ("sample locations, medium, lithology, major/trace elements, analytical method, detection limits, GIS context",),
        ("unit standardization", "robust statistics", "correlation/PCA", "spatial interpolation or map classification", "lithology-group comparison"),
        ("sampling map", "element anomaly maps", "correlation matrix", "PCA biplot", "boxplots by lithology"),
        ("summary statistics by lithology", "anomaly threshold table"),
        ("geochemical-survey-skill", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Mineral Exploration Geochemistry Paper",
        ("exploration", "anomaly", "target", "prospectivity", "claim", "pathfinder", "mineral occurrence", "gis", "geophysics"),
        ("Which geochemical signatures are consistent with mineral-system processes, and how should targets be ranked?",),
        ("Multi-element anomalies combined with geological and structural context can prioritize targets, but cannot alone establish economic mineralization.",),
        ("geochemical assays, pathfinder elements, geology, structures, occurrences, geophysics, claim/AOI context, QA/QC status",),
        ("anomaly thresholding", "multi-element association", "spatial overlay", "prospectivity scoring", "disclosure-boundary review"),
        ("study area geology map", "pathfinder anomaly maps", "PCA/factor loading plot", "prospectivity ranking map"),
        ("evidence layer table", "target ranking table with caveats"),
        ("geochemical-survey-skill", "deposit-model-skill", "ni43-101-disclosure-check-skill", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Petrogenesis Paper",
        ("petrogenesis", "magma", "granitoid", "basalt", "harker", "tas", "ree", "spider", "tectonic setting"),
        ("What source, fractionation, assimilation, or tectonic processes explain the rock suite?",),
        ("Major, trace, REE, and isotope patterns can distinguish source inheritance from differentiation or alteration effects.",),
        ("petrography, major oxides, trace elements, REE, isotopes, ages, alteration indicators, analytical methods",),
        ("rock classification", "Harker trends", "REE normalization", "trace-element discrimination", "isotope comparison"),
        ("TAS/QAPF diagram", "Harker diagrams", "REE patterns", "primitive mantle spider diagram", "isotope evolution plot"),
        ("sample metadata", "analytical method table", "derived geochemical index table"),
        ("academic-figure-package-skill",),
    ),
    PaperProfile(
        "Isotope Geochemistry Paper",
        ("isotope", "zircon", "hf", "nd", "sr", "pb", "oxygen", "sulfur", "crustal growth", "provenance"),
        ("What isotopic evidence constrains source, age, mixing, provenance, or crustal evolution?",),
        ("Isotopic compositions preserve source and evolution signals that can be tested against age and geochemical constraints.",),
        ("isotope ratios, analytical uncertainty, standards, ages, petrography, whole-rock chemistry, reference reservoirs",),
        ("isotope correction", "age filtering", "mixing model planning", "source comparison", "uncertainty propagation"),
        ("epsilon-time diagram", "isotope ratio plot", "concordia or age distribution", "mixing model schematic"),
        ("isotope metadata table", "reference reservoir comparison table"),
        ("academic-figure-package-skill",),
    ),
    PaperProfile(
        "Hydrogeochemistry Paper",
        ("groundwater", "phreeqc", "speciation", "saturation", "piper", "gibbs", "eh", "ph", "alkalinity", "hco3"),
        ("Which water-rock, redox, mixing, or complexation processes control groundwater chemistry and solute mobility?",),
        ("Major-ion chemistry, redox indicators, and speciation/saturation calculations can distinguish controlling processes.",),
        ("water chemistry, charge balance inputs, pH, Eh, alkalinity, temperature, major ions, trace elements, sampling metadata",),
        ("charge-balance check", "Piper/Gibbs classification", "PHREEQC speciation", "saturation-index analysis", "sensitivity analysis"),
        ("Piper diagram", "Eh-pH diagram", "saturation-index plot", "speciation fraction plot", "reaction path diagram"),
        ("water chemistry QA/QC table", "PHREEQC database/keyword table"),
        ("phreeqc-modeling-skill", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Environmental Geochemistry Paper",
        ("environmental", "contamination", "acid mine drainage", "tailings", "seepage", "baseline", "risk", "metal mobility"),
        ("Which processes control contaminant release, transport, attenuation, or baseline variability?",),
        ("Metal mobility is controlled by coupled pH, redox, adsorption, precipitation, and hydrological pathways.",),
        ("sample chemistry, pH/Eh, sulfate/alkalinity, mineralogy, hydrology, background/baseline data, regulatory context if relevant",),
        ("baseline comparison", "redox-pH interpretation", "mineral saturation", "attenuation mechanism analysis", "uncertainty review"),
        ("concentration maps", "pH/Eh plot", "metal-sulfate trends", "attenuation conceptual model"),
        ("baseline/exceedance table", "uncertainty and limitation table"),
        ("phreeqc-modeling-skill", "thmc-groundwater-router-skill", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Reactive Transport Modelling Paper",
        ("reactive transport", "pflotran", "phreeqcrm", "transport", "breakthrough", "boundary condition", "kinetic", "thmc"),
        ("How do flow, transport, and reactions jointly explain observed or predicted geochemical evolution?",),
        ("A coupled transport-reaction model can reproduce key concentration or mineral trends only within explicit boundary and parameter limits.",),
        ("domain geometry, grid, hydraulic parameters, chemistry, mineralogy, reactions, boundary/initial conditions, observations",),
        ("conceptual model", "governing equations", "reaction network", "solver selection", "calibration/validation plan", "sensitivity analysis"),
        ("conceptual domain", "reaction network", "breakthrough curves", "spatial concentration fields", "sensitivity plots"),
        ("parameter table", "boundary-condition table", "calibration/validation table"),
        ("thmc-groundwater-router-skill", "pflotran-router-skill", "phreeqc-modeling-skill", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Radiolysis / Nuclear Geochemistry Paper",
        ("radiolysis", "g-value", "dose rate", "let", "radical", "h2", "h2o2", "radionuclide", "nuclear waste", "bentonite"),
        ("How does radiation chemistry affect redox evolution, gas generation, or radionuclide mobility in geological media?",),
        ("Radiolysis yields and reactive species are modified by dose rate, pore confinement, mineral surfaces, and groundwater chemistry.",),
        ("radiation field, dose rate, water chemistry, mineral surfaces, porosity, reaction yields, radionuclide species, boundary conditions",),
        ("reaction network design", "G-value comparison", "redox/speciation modeling", "mass balance", "safety-boundary statement"),
        ("radiolysis reaction network", "G-value comparison", "pore-size effect plot", "redox/speciation evolution plot"),
        ("species/reaction table", "assumption and boundary-condition table"),
        ("academic-paper-research-writer", "phreeqc-modeling-skill", "thmc-groundwater-router-skill", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Geochemical Modelling and Machine Learning Paper",
        ("machine learning", "random forest", "classifier", "prediction", "feature importance", "neural", "model", "ai"),
        ("Can a transparent model explain or predict geochemical patterns without overfitting or losing geological meaning?",),
        ("Feature-engineered geochemical and geological predictors can improve prediction, but transferability must be independently tested.",),
        ("labeled samples, predictors, train/test split, spatial grouping, feature definitions, uncertainty labels",),
        ("feature engineering", "cross-validation", "spatial leakage check", "model interpretation", "uncertainty and transferability assessment"),
        ("workflow diagram", "feature importance", "ROC/AUC if labels are valid", "prediction/prospectivity map"),
        ("feature table", "validation metric table", "failure-mode table"),
        ("academic-figure-package-skill", "deposit-model-skill"),
    ),
    PaperProfile(
        "Review / Perspective Paper",
        ("review", "perspective", "future directions", "literature", "progress", "synthesis"),
        ("What is known, what remains uncertain, and what research agenda follows from the evidence?",),
        ("A structured evidence synthesis can identify unresolved mechanisms and practical next tests.",),
        ("literature corpus, inclusion criteria, evidence categories, citation metadata, comparison framework",),
        ("literature search protocol", "evidence matrix", "conceptual synthesis", "research-gap mapping"),
        ("literature workflow", "evidence matrix heatmap", "conceptual framework diagram"),
        ("source corpus table", "gap and future-work table"),
        ("academic-paper-research-writer", "academic-figure-package-skill"),
    ),
    PaperProfile(
        "Technical Note / Methods Paper",
        ("method", "workflow", "protocol", "benchmark", "pipeline", "tool", "validation"),
        ("What method or workflow is introduced, benchmarked, and made reproducible?",),
        ("The proposed workflow improves reproducibility only if inputs, assumptions, validation data, and failure modes are transparent.",),
        ("benchmark data, method inputs, expected outputs, validation cases, failure cases, versioned code",),
        ("workflow specification", "benchmarking", "validation", "failure-mode analysis", "reproducibility package"),
        ("method workflow", "benchmark result plot", "failure-mode schematic"),
        ("benchmark dataset table", "method comparison table"),
        ("academic-figure-package-skill",),
    ),
)


COMMON_OUTLINE = (
    "Abstract",
    "Keywords",
    "1. Introduction",
    "2. Geological / Hydrogeological / Geochemical Setting",
    "3. Materials and Methods",
    "4. Results",
    "5. Discussion",
    "6. Implications",
    "7. Limitations",
    "8. Conclusions",
    "Data and Code Availability",
    "References",
    "Supplementary Materials",
)


def keyword_matches(haystack: str, keyword: str) -> bool:
    normalized = keyword.lower()
    if len(normalized.replace("-", "").replace("_", "")) <= 3:
        return re.search(rf"(?<![a-z0-9]){re.escape(normalized)}(?![a-z0-9])", haystack) is not None
    return normalized in haystack


def classify(text: str) -> list[tuple[int, PaperProfile]]:
    haystack = text.lower()
    scored: list[tuple[int, PaperProfile]] = []
    for profile in PROFILES:
        score = sum(1 for keyword in profile.keywords if keyword_matches(haystack, keyword))
        if score:
            scored.append((score, profile))
    if not scored:
        fallback = next(p for p in PROFILES if p.name == "Regional Geochemical Characterization Paper")
        scored.append((0, fallback))
    return sorted(scored, key=lambda item: (-item[0], item[1].name))[:3]


def bullets(items: tuple[str, ...] | list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render(args: argparse.Namespace) -> str:
    topic_parts = [args.topic, args.region or "", args.paper_goal or "", " ".join(args.available_data or [])]
    classified = classify(" ".join(topic_parts))
    profiles = [profile for _, profile in classified]
    primary = profiles[0]
    secondary = profiles[1].name if len(profiles) > 1 else "None detected"
    tertiary = profiles[2].name if len(profiles) > 2 else "None detected"

    data_items = list(dict.fromkeys(item for profile in profiles for item in profile.data))
    method_items = list(dict.fromkeys(item for profile in profiles for item in profile.methods))
    figure_items = list(dict.fromkeys(item for profile in profiles for item in profile.figures))
    table_items = list(dict.fromkeys(item for profile in profiles for item in profile.tables))
    downstream = list(dict.fromkeys(item for profile in profiles for item in profile.downstream))
    downstream.insert(0, "academic-paper-research-writer")
    downstream.append("geomine-paper-pdf-export-skill")
    downstream = list(dict.fromkeys(downstream))

    summary = {
        "paper_type": {
            "primary": primary.name,
            "secondary": secondary,
            "tertiary": tertiary,
        },
        "research_questions": list(primary.questions),
        "hypotheses": list(primary.hypotheses),
        "required_data": data_items,
        "methods": method_items,
        "figures": figure_items,
        "tables": table_items,
        "downstream_skills": downstream,
    }

    return f"""# Geochemistry Paper Architecture

## 1. Topic and Paper Type Classification

- Research topic: {args.topic}
- Region: {args.region or "[not specified]"}
- Paper goal: {args.paper_goal or "[not specified]"}
- Paper stage: {args.paper_stage}
- Preferred journal style: {args.journal_style}
- Output language: {args.language}
- Primary type: {primary.name}
- Secondary type: {secondary}
- Tertiary type: {tertiary}

Rationale: classification is based on topic keywords, available-data hints, and intended method signals. Treat this as a first-pass architecture until the source corpus and dataset audit are complete.

## 2. Scientific Framing

Scientific problem: [state the unresolved geochemical process or knowledge gap].

Knowledge gap: [state what previous studies or available datasets do not yet constrain].

Research questions:
{bullets(primary.questions)}

Testable hypotheses:
{bullets(primary.hypotheses)}

## 3. Data Audit and Missing-Data Control

Required data:
{bullets(data_items)}

Missing-data rule: use explicit placeholders for unavailable sample counts, concentrations, coordinates, analytical methods, detection limits, model parameters, boundary conditions, and calibration results. Explain how each missing item affects interpretation.

## 4. Methods and Reproducibility Plan

Methods:
{bullets(method_items)}

Reproducibility requirements:
- Record data source, release date or version, license, and processing script.
- Record units, normalization constants, analytical methods, detection limits, and QA/QC flags.
- Record software, version, thermodynamic database, model settings, and code path.

## 5. Figure Architecture

{bullets(figure_items)}

Each figure must state the claim supported, variables, axes, units, legend, source/provenance, uncertainty encoding, and caveat.

## 6. Table Plan

{bullets(table_items)}

## 7. Paper Outline

{bullets(COMMON_OUTLINE)}

## 8. Section-Level Writing Controls

- Abstract: background -> knowledge gap -> data/methods -> key results -> interpretation -> implication.
- Introduction: build problem tension, prior work, limitation, hypothesis, and contribution.
- Setting: include only geological or hydrogeochemical context needed for interpretation.
- Methods: document data provenance, QA/QC, transformations, software, versions, and uncertainty.
- Results: report observations only; do not explain mechanisms prematurely.
- Discussion: observation -> mechanism -> evidence -> alternative explanation -> boundary condition -> implication.
- Conclusions: 4-6 evidence-traceable points with no new data or over-extrapolation.

## 9. Citation Requirements

- Cite datasets, analytical methods, formulas, classification diagrams, software, thermodynamic databases, and regional geology.
- Preserve citation placeholders instead of inventing references or DOI values.
- Match the selected journal style: {args.journal_style}.

## 10. Uncertainty and Academic Restraint

- Discuss sampling bias, analytical error, detection limits, lithology bias, alteration/weathering, model parameter uncertainty, thermodynamic database limits, and validation gaps.
- Do not treat correlation as causation without independent mechanism evidence.
- Do not infer mineral resources, reserves, feasibility, or economic value from geochemical evidence alone.

## 11. Downstream GeoMine Skill Routing

{bullets(downstream)}

## 12. Machine-Readable Summary

```json
{json.dumps(summary, ensure_ascii=False, indent=2)}
```
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True, help="Research topic or proposed paper title")
    parser.add_argument("--region", default="", help="Region or study area")
    parser.add_argument("--paper-goal", default="", help="Intended contribution or target outcome")
    parser.add_argument("--available-data", action="append", default=[], help="Available data class; repeatable")
    parser.add_argument("--journal-style", default="Elsevier", help="Citation / journal style")
    parser.add_argument("--language", default="Chinese", choices=("English", "Chinese", "bilingual"))
    parser.add_argument("--paper-stage", default="outline", choices=("outline", "proposal", "draft", "revision", "final"))
    parser.add_argument("--output", "-o", type=Path, help="Write Markdown architecture to a file")
    args = parser.parse_args()

    markdown = render(args)
    if args.output:
        args.output.write_text(markdown, encoding="utf-8")
    else:
        print(markdown)
    return 0


if __name__ == "__main__":
    sys.exit(main())
