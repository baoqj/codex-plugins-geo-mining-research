# GeoMine Entity Schema

Use this schema when routing research tasks and interpreting MCP results.

## Core Entities

- AOI: name, geometry, geometry type, CRS, country, province/territory, NTS sheet, precision, assumptions, warnings.
- Commodity: primary commodity, secondary commodities, critical mineral status, pathfinder elements.
- Deposit model: normalized model name, expected evidence, pathfinders, common false positives.
- Jurisdiction: country, province/territory, federal context, local or Indigenous context when relevant.
- Claim / tenure: claim id, status, owner/operator, expiry, geometry source, update date.
- Company / project: company name, project name, adjacent assets, technical reports, disclosure documents.
- Dataset: source name, source URL, dataset id, license, CRS, scale/resolution, update date, retrieval status.
- Technical report: report type, title, author, date, QP status, issuer, project stage, evidence gaps.

## Required Provenance Fields

- source_name
- source_url or catalog identifier
- retrieved_at
- retrieval_status
- CRS when spatial
- scale_or_resolution when spatial
- license
- limitations
- evidence_origin: MCP, user file, static reference, or model inference
