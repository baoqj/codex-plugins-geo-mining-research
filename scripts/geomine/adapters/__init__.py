"""Adapter contracts and source-specific helpers for future live data access."""

from .arcgis import ArcGisFeatureServiceAdapter
from .base import AdapterResult, DataResource, SourceAdapter
from .ckan import BcDataCatalogueAdapter, CkanPackageSearchAdapter, OpenCanadaCkanAdapter
from .source_registry import ADAPTER_SOURCE_REGISTRY, get_source_registry

__all__ = [
    "ADAPTER_SOURCE_REGISTRY",
    "AdapterResult",
    "ArcGisFeatureServiceAdapter",
    "BcDataCatalogueAdapter",
    "CkanPackageSearchAdapter",
    "DataResource",
    "OpenCanadaCkanAdapter",
    "SourceAdapter",
    "get_source_registry",
]
