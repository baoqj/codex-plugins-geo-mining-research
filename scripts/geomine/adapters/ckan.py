"""CKAN catalogue adapters for Open Canada and BC Data Catalogue."""

from __future__ import annotations

from typing import Any
from urllib.parse import urlencode

from .base import AdapterResult, DataResource


class CkanPackageSearchAdapter:
    """Build CKAN package-search URLs and normalize package-search payloads."""

    name = "ckan-package-search"
    version = "0.2.0"

    def __init__(self, base_action_url: str, source_name: str, jurisdiction: str):
        self.base_action_url = base_action_url.rstrip("/")
        self.source_name = source_name
        self.jurisdiction = jurisdiction

    def build_package_search_url(self, query: str, rows: int = 10, start: int = 0) -> str:
        if rows < 1 or rows > 100:
            raise ValueError("rows must be between 1 and 100")
        if start < 0:
            raise ValueError("start must be >= 0")
        params = urlencode({"q": query, "rows": rows, "start": start})
        return f"{self.base_action_url}/package_search?{params}"

    def parse_package_search(self, payload: dict[str, Any], query: dict[str, Any] | None = None) -> list[AdapterResult]:
        result = payload.get("result", {})
        records = result.get("results", [])
        if not isinstance(records, list):
            raise ValueError("CKAN payload result.results must be a list")

        parsed: list[AdapterResult] = []
        for record in records:
            if not isinstance(record, dict):
                continue
            resources = tuple(self._parse_resources(record.get("resources", [])))
            formats = tuple(sorted({resource.format for resource in resources if resource.format}))
            warnings: list[str] = []
            if not resources:
                warnings.append("No resources listed in CKAN record.")
            if not record.get("license_title") and not record.get("license_id"):
                warnings.append("No license metadata found in CKAN record.")
            parsed.append(
                AdapterResult(
                    source=self.source_name,
                    title=str(record.get("title") or record.get("name") or "Untitled CKAN package"),
                    record_id=record.get("id") or record.get("name"),
                    url=record.get("url"),
                    jurisdiction=self.jurisdiction,
                    data_types=tuple(_as_tuple(record.get("groups"))),
                    formats=formats,
                    license=record.get("license_title") or record.get("license_id"),
                    provider=_organization_title(record.get("organization")),
                    retrieval_status="parsed",
                    query=query or {},
                    resources=resources,
                    warnings=tuple(warnings),
                )
            )
        return parsed

    def source_note(self) -> str:
        return "CKAN catalogue results identify candidate resources; each resource needs separate retrieval and parsing."

    def _parse_resources(self, resources: Any) -> list[DataResource]:
        if not isinstance(resources, list):
            return []
        parsed: list[DataResource] = []
        for resource in resources:
            if not isinstance(resource, dict):
                continue
            parsed.append(
                DataResource(
                    name=resource.get("name"),
                    url=resource.get("url"),
                    format=_clean_format(resource.get("format")),
                    resource_id=resource.get("id"),
                    description=resource.get("description"),
                )
            )
        return parsed


class OpenCanadaCkanAdapter(CkanPackageSearchAdapter):
    """Open Canada / Open Maps CKAN package-search adapter."""

    name = "open-canada-ckan"

    def __init__(self) -> None:
        super().__init__(
            base_action_url="https://open.canada.ca/data/api/3/action",
            source_name="Open Canada / Geo.ca",
            jurisdiction="Canada",
        )


class BcDataCatalogueAdapter(CkanPackageSearchAdapter):
    """BC Data Catalogue CKAN package-search adapter for MINFILE and BCGS records."""

    name = "bc-data-catalogue-ckan"

    def __init__(self) -> None:
        super().__init__(
            base_action_url="https://catalogue.data.gov.bc.ca/api/3/action",
            source_name="BC Data Catalogue",
            jurisdiction="British Columbia",
        )


def _clean_format(value: Any) -> str | None:
    if value is None:
        return None
    text = str(value).strip()
    return text.upper() if text else None


def _organization_title(value: Any) -> str | None:
    if isinstance(value, dict):
        title = value.get("title") or value.get("name")
        return str(title) if title else None
    return None


def _as_tuple(groups: Any) -> tuple[str, ...]:
    if not isinstance(groups, list):
        return ()
    values: list[str] = []
    for item in groups:
        if isinstance(item, dict):
            value = item.get("display_name") or item.get("title") or item.get("name")
        else:
            value = item
        if value:
            values.append(str(value))
    return tuple(values)
