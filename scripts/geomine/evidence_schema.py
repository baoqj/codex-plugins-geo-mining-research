"""Shared records for GeoMine Research evidence handling."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


ALLOWED_GRADES = {"A", "B", "C", "D"}


@dataclass(frozen=True)
class EvidenceRecord:
    """A single provenance-preserving evidence item."""

    source: str
    title: str
    evidence_type: str
    summary: str
    grade: str = "C"
    jurisdiction: str | None = None
    date: str | None = None
    crs: str | None = None
    scale_or_resolution: str | None = None
    license: str | None = None
    uncertainty: str | None = None
    url: str | None = None

    def __post_init__(self) -> None:
        grade = self.grade.upper()
        if grade not in ALLOWED_GRADES:
            raise ValueError(f"grade must be one of {sorted(ALLOWED_GRADES)}")
        object.__setattr__(self, "grade", grade)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)

    def to_markdown(self) -> str:
        parts = [
            f"- **{self.title}** ({self.source}, grade {self.grade})",
            f"  - Type: {self.evidence_type}",
            f"  - Summary: {self.summary}",
        ]
        if self.jurisdiction:
            parts.append(f"  - Jurisdiction: {self.jurisdiction}")
        if self.date:
            parts.append(f"  - Date/version: {self.date}")
        if self.crs:
            parts.append(f"  - CRS: {self.crs}")
        if self.scale_or_resolution:
            parts.append(f"  - Scale/resolution: {self.scale_or_resolution}")
        if self.license:
            parts.append(f"  - License: {self.license}")
        if self.uncertainty:
            parts.append(f"  - Uncertainty: {self.uncertainty}")
        if self.url:
            parts.append(f"  - URL: {self.url}")
        return "\n".join(parts)


@dataclass(frozen=True)
class NormalizedAOI:
    """A structured AOI without external geocoding."""

    name: str | None = None
    province_or_territory: str | None = None
    country: str = "Canada"
    coordinates: Any | None = None
    crs: str | None = None
    nts_sheet: str | None = None
    assumptions: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class DataSourceRecord:
    """A public data source catalog entry."""

    name: str
    jurisdiction: str
    data_types: tuple[str, ...]
    likely_formats: tuple[str, ...]
    use_cases: tuple[str, ...]
    provenance_notes: str
    limitations: str
    url: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class Finding:
    """A finding with confidence and limits."""

    title: str
    body: str
    confidence: str = "medium"
    evidence_grade: str = "C"
    limitations: str | None = None

    def __post_init__(self) -> None:
        grade = self.evidence_grade.upper()
        if grade not in ALLOWED_GRADES:
            raise ValueError(f"evidence_grade must be one of {sorted(ALLOWED_GRADES)}")
        object.__setattr__(self, "evidence_grade", grade)

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class Recommendation:
    """A recommended next step."""

    action: str
    rationale: str
    priority: str = "medium"
    evidence_needed: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)
