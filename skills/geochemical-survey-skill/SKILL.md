---
name: geochemical-survey-skill
description: Structure geochemical survey evidence, QA/QC context, pathfinder elements, and cautious anomaly language for mining research.
---

# Geochemical Survey Skill

## Purpose

Review geochemical survey evidence and convert raw or described values into cautious, provenance-aware interpretation. This skill can suggest anomaly classes but must not turn anomalies into discovery claims.

## Inputs To Identify

- Sample medium: soil, till, stream sediment, lake sediment, lake water, rock, vegetation, drill core, or unknown.
- Elements and units.
- Analytical method, lab, detection limits, and censored values.
- QA/QC records: duplicates, blanks, CRMs, field standards, batch information.
- Coordinates and CRS.
- Survey id, source, release date, and license.
- Commodity and deposit model.

## Procedure

1. Summarize dataset scope, sample medium, element list, units, and spatial coverage.
2. Check whether CRS, analytical method, detection limits, and QA/QC are supplied.
3. Avoid comparing surveys directly unless methods and media are compatible.
4. Use deposit-model pathfinders from `references/deposit-model-cheatsheet.md`.
5. Use robust language: background, weak anomaly, moderate anomaly, strong anomaly, or unclassified.
6. If numeric arrays are supplied, use `scripts/geomine/geochem.py` for percentile rank, robust z-score, and simple anomaly class.
7. Explain data gaps and follow-up work before interpreting target potential.
8. If the user asks for geochemical maps, anomaly figures, pathfinder heatmaps, target-ranking visuals, captions, or manuscript figure planning, route to `academic-figure-package-skill` after the geochemical evidence and QA/QC limits are clarified.

## Output Contract

Return:

- Dataset summary.
- QA/QC and comparability review.
- Background and threshold notes.
- Pathfinder element associations.
- Anomaly table with element, value or zone, percentile or score if calculated, class, and caveats.
- Deposit-model relevance.
- Recommended follow-up.
- Limitations.
- Recommended figures when the user is preparing a paper or technical report.

## Evidence And Provenance Rules

- Preserve sample medium, lab, analytical method, detection limits, units, CRS, survey date, and source id.
- Mark values below detection limits and explain how they were handled.
- Separate analytical anomalies from geological interpretation.
- Use evidence grades from `references/evidence-grading.md`.

## Guardrails And Limitations

- Do not claim mineralization, ore, resource, reserve, or economic value from geochemistry alone.
- Do not rank drill targets without spatial control and geological context.
- Do not hide missing QA/QC or method metadata.
- Do not compare incompatible sample media as if they are equivalent.
