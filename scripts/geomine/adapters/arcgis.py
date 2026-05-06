"""ArcGIS REST query helpers for MRData and future government map services."""

from __future__ import annotations

import json
from typing import Any
from urllib.parse import urlencode

from .base import AdapterResult


class ArcGisFeatureServiceAdapter:
    """Build ArcGIS REST query URLs and parse FeatureSet payloads."""

    name = "arcgis-feature-service"
    version = "0.2.0"

    def __init__(
        self,
        service_url: str,
        source_name: str,
        jurisdiction: str | None = None,
        default_layer: int = 0,
    ) -> None:
        self.service_url = service_url.rstrip("/")
        self.source_name = source_name
        self.jurisdiction = jurisdiction
        self.default_layer = default_layer

    def build_query_url(
        self,
        layer: int | None = None,
        where: str = "1=1",
        out_fields: str = "*",
        geometry: dict[str, Any] | None = None,
        result_record_count: int = 100,
        out_sr: int = 4326,
    ) -> str:
        if result_record_count < 1 or result_record_count > 2000:
            raise ValueError("result_record_count must be between 1 and 2000")
        params: dict[str, Any] = {
            "f": "json",
            "where": where,
            "outFields": out_fields,
            "returnGeometry": "true",
            "outSR": out_sr,
            "resultRecordCount": result_record_count,
        }
        if geometry:
            params["geometry"] = _compact_geometry(geometry)
            params["geometryType"] = "esriGeometryEnvelope"
            params["spatialRel"] = "esriSpatialRelIntersects"
        layer_id = self.default_layer if layer is None else layer
        return f"{self.service_url}/{layer_id}/query?{urlencode(params)}"

    def parse_feature_set(
        self,
        payload: dict[str, Any],
        title_field: str | None = None,
        id_field: str | None = None,
        query: dict[str, Any] | None = None,
    ) -> list[AdapterResult]:
        features = payload.get("features", [])
        if not isinstance(features, list):
            raise ValueError("ArcGIS FeatureSet payload features must be a list")

        parsed: list[AdapterResult] = []
        fields = _field_names(payload.get("fields"))
        for index, feature in enumerate(features):
            if not isinstance(feature, dict):
                continue
            attributes = feature.get("attributes") if isinstance(feature.get("attributes"), dict) else {}
            title = _select_field(attributes, title_field, ("name", "site_name", "dep_name", "mrds_name")) or f"Feature {index + 1}"
            record_id = _select_field(attributes, id_field, ("id", "objectid", "OBJECTID", "site_id", "mrds_id"))
            warnings: list[str] = []
            if not feature.get("geometry"):
                warnings.append("Feature has no geometry.")
            if fields:
                warnings.append(f"Fields available: {', '.join(fields[:12])}")
            parsed.append(
                AdapterResult(
                    source=self.source_name,
                    title=str(title),
                    record_id=str(record_id) if record_id is not None else None,
                    jurisdiction=self.jurisdiction,
                    data_types=("arcgis-feature",),
                    formats=("JSON",),
                    retrieval_status="parsed",
                    query=query or {},
                    warnings=tuple(warnings),
                )
            )
        return parsed

    def source_note(self) -> str:
        return "ArcGIS FeatureSet parsing preserves attributes only through source/cache references in later live adapters."


def _compact_geometry(geometry: dict[str, Any]) -> str:
    keys = ("xmin", "ymin", "xmax", "ymax", "spatialReference")
    compact = {key: geometry[key] for key in keys if key in geometry}
    if not {"xmin", "ymin", "xmax", "ymax"}.issubset(compact):
        raise ValueError("geometry envelope must include xmin, ymin, xmax, and ymax")
    return json.dumps(compact, separators=(",", ":"))


def _field_names(fields: Any) -> list[str]:
    if not isinstance(fields, list):
        return []
    return [str(field["name"]) for field in fields if isinstance(field, dict) and field.get("name")]


def _select_field(attributes: dict[str, Any], preferred: str | None, fallbacks: tuple[str, ...]) -> Any | None:
    if preferred and preferred in attributes:
        return attributes[preferred]
    lower_index = {key.lower(): key for key in attributes}
    for field in fallbacks:
        key = lower_index.get(field.lower())
        if key:
            return attributes[key]
    return None
