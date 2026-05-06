---
name: mineral-occurrence-skill
description: Normalize mineral occurrence records and review occurrence evidence, confidence, commodities, deposit models, and historic-resource cautions.
---

# Mineral Occurrence Skill

## Purpose

Convert government or report-based mineral occurrence records into a common evidence format and interpret them cautiously in relation to an AOI or deposit model.

## Inputs To Identify

- Source database, such as BC MINFILE, Ontario Mineral Inventory, USMIN, MRDS, or a provincial survey inventory.
- Occurrence id, name, source URL, and release or update date.
- Coordinates, CRS, location confidence, and geometry type.
- Commodity, deposit model, host rocks, alteration, mineralogy, status, and history.
- Production, resource, or reserve language and whether it is current, historic, or unsupported.
- Distance or relationship to AOI only when geometry and CRS are confirmed.

## Procedure

1. Preserve the source id and original record fields.
2. Normalize name, source, jurisdiction, coordinates, commodities, deposit model, status, and confidence notes.
3. Use `scripts/geomine/occurrences.py` when working with structured occurrence dictionaries.
4. Check whether the record is a government inventory, assessment report, company report, or secondary source.
5. Compare the occurrence to the requested commodity and deposit model.
6. Flag historic production or resource statements that need QP and current-report verification.
7. Do not calculate proximity unless AOI and occurrence CRS are confirmed.

## Output Contract

Return:

- Normalized occurrence table.
- Source id and provenance.
- Commodity and deposit model relevance.
- Location confidence.
- Status and history.
- Evidence grade.
- Cautions around historic production, resources, reserves, or economic language.
- Next verification steps.

## Evidence And Provenance Rules

- Prefer official government inventory records for occurrence existence and metadata.
- Preserve source id, update date, location accuracy, and original terminology.
- Treat secondary descriptions as lower-grade evidence unless tied to primary records.
- Separate occurrence presence from target potential.

## Guardrails And Limitations

- Do not imply a nearby occurrence extends into the AOI without evidence.
- Do not use historic resource statements as current mineral resources.
- Do not treat occurrence coordinates as precise unless the source says so.
- Do not infer tenure ownership or permitting status from occurrence records.
