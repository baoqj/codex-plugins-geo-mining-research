"""Base types for GeoMine data adapters."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Protocol


@dataclass(frozen=True)
class DataResource:
    """A downloadable or queryable resource attached to a source record."""

    name: str | None = None
    url: str | None = None
    format: str | None = None
    resource_id: str | None = None
    description: str | None = None

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True)
class AdapterResult:
    """A normalized adapter result with provenance and limitations."""

    source: str
    title: str
    record_id: str | None = None
    url: str | None = None
    jurisdiction: str | None = None
    data_types: tuple[str, ...] = ()
    formats: tuple[str, ...] = ()
    license: str | None = None
    provider: str | None = None
    retrieval_status: str = "parsed"
    query: dict[str, Any] = field(default_factory=dict)
    resources: tuple[DataResource, ...] = ()
    warnings: tuple[str, ...] = ()

    def as_dict(self) -> dict[str, Any]:
        data = asdict(self)
        data["resources"] = [resource.as_dict() for resource in self.resources]
        return data


class SourceAdapter(Protocol):
    """Protocol for source-specific adapters."""

    name: str
    version: str

    def source_note(self) -> str:
        """Return a human-readable source limitation note."""
