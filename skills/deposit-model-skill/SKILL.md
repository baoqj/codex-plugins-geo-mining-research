---
name: deposit-model-skill
description: Apply concise evidence checklists for major deposit models and pathfinder associations without overclaiming prospectivity.
---

# Deposit Model Skill

## Purpose

Map observed geology, geochemistry, geophysics, alteration, structure, and occurrence evidence to a deposit-model checklist. The output is a fit assessment and gap list, not a discovery or economic conclusion.

## Inputs To Identify

- Requested or inferred deposit model.
- Commodity and pathfinder elements.
- Host rocks, intrusive units, stratigraphy, structure, alteration, mineralization, geophysics, geochemistry, and known occurrences.
- Evidence quality, source provenance, scale, and uncertainty.

## Procedure

1. Select the relevant model or state that the model is unresolved.
2. Use `references/deposit-model-cheatsheet.md` for model checklists.
3. Score evidence qualitatively as supportive, mixed, absent, unknown, or not applicable.
4. Separate direct evidence from indirect pathfinders and regional analogies.
5. Identify missing evidence that would most improve model confidence.
6. Avoid binary yes/no conclusions unless the evidence is strong and well sourced.

## Output Contract

Return:

- Deposit model assessed.
- Expected evidence checklist.
- Observed evidence by lane.
- Pathfinder elements.
- Fit assessment: strong, moderate, weak, speculative, or insufficient data.
- Confidence and limitations.
- Data gaps.
- Recommended next work.

## Evidence And Provenance Rules

- Link each model-fit statement to an evidence source or mark it as unverified.
- Preserve scale because regional evidence may not support target-scale decisions.
- Mark remote sensing, geophysical, and statistical anomalies as hypothesis-level until ground checked.
- Note conflicts between geology, geochemistry, occurrences, and geophysics.

## Guardrails And Limitations

- Do not equate model fit with economic viability.
- Do not claim resource, reserve, or drill-ready status from model fit alone.
- Do not ignore negative or absent evidence.
- Do not force an AOI into a popular model when evidence is insufficient.

## MVP Model Coverage

- Porphyry Cu-Mo-Au.
- Orogenic gold.
- Volcanogenic massive sulphide.
- LCT pegmatite.
- Magmatic Ni-Cu-PGE.
- Iron oxide copper-gold.
- Mississippi Valley-type.
- Skarn.
