"""Configuration for the GeoMine THMC MCP server."""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path


@dataclass(frozen=True)
class THMCConfig:
    mode: str
    cache_dir: Path
    openmine_api_base_url: str | None
    openmine_project_db_url: str | None
    openmine_postgis_dsn: str | None
    openmine_r2_endpoint: str | None
    phreeqc_service_url: str | None
    compute_api_url: str | None


def load_config() -> THMCConfig:
    cache_dir = Path(
        os.environ.get("GEOMINE_THMC_CACHE_DIR", "~/.cache/geomine-thmc-mcp")
    ).expanduser()
    return THMCConfig(
        mode=os.environ.get("GEOMINE_THMC_MODE", "mock").lower(),
        cache_dir=cache_dir,
        openmine_api_base_url=os.environ.get("OPENMINE_API_BASE_URL"),
        openmine_project_db_url=os.environ.get("OPENMINE_PROJECT_DB_URL"),
        openmine_postgis_dsn=os.environ.get("OPENMINE_POSTGIS_DSN"),
        openmine_r2_endpoint=os.environ.get("OPENMINE_R2_ENDPOINT"),
        phreeqc_service_url=os.environ.get("PHREEQC_SERVICE_URL"),
        compute_api_url=os.environ.get("THMC_COMPUTE_API_URL"),
    )


def masked_env_status() -> dict[str, bool]:
    keys = [
        "OPENMINE_API_BASE_URL",
        "OPENMINE_API_TOKEN",
        "OPENMINE_PROJECT_DB_URL",
        "OPENMINE_POSTGIS_DSN",
        "OPENMINE_R2_ENDPOINT",
        "OPENMINE_R2_ACCESS_KEY_ID",
        "OPENMINE_R2_SECRET_ACCESS_KEY",
        "OPENMINE_R2_BUCKET",
        "PHREEQC_SERVICE_URL",
        "PHREEQC_SERVICE_TOKEN",
        "THMC_COMPUTE_API_URL",
        "THMC_COMPUTE_API_TOKEN",
        "GEOMINE_THMC_CACHE_DIR",
        "GEOMINE_THMC_MODE",
    ]
    return {key: bool(os.environ.get(key)) for key in keys}

