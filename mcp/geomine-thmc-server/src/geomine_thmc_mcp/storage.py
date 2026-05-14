"""Mock and local-file storage for GeoMine THMC MCP tools."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any
from uuid import uuid4

from .config import load_config
from .schemas import now_iso


MOCK_PROJECTS = [
    {
        "project_id": "om-prj-uranium-001",
        "name": "Athabasca Margin Uranium Groundwater Study",
        "jurisdiction": "Saskatchewan, Canada",
        "commodity": ["uranium"],
        "stage": "research_modeling",
        "status": "active",
        "updated_at": "2026-05-12T00:00:00Z",
        "research_objective": "Mock project for U-Ra-Rn-Po-Pb radionuclide migration in fractured groundwater.",
        "data_assets": ["mesh-2d-cross-section-001", "field-k-001", "field-porosity-001", "field-temperature-001"],
    },
    {
        "project_id": "om-prj-dgr-001",
        "name": "DGR THMC Field Data Acquisition Mock Project",
        "jurisdiction": "Canada",
        "commodity": [],
        "stage": "research_modeling",
        "status": "active",
        "updated_at": "2026-05-12T00:00:00Z",
        "research_objective": "Mock DGR project for field-measured THMC data acquisition, QA/QC, and calibration dataset packaging.",
        "data_assets": ["dgr-campaign-revell-mock-001"],
    }
]

MOCK_AOIS = {
    "om-prj-uranium-001": {
        "aoi_id": "aoi-main",
        "name": "Athabasca margin mock AOI",
        "crs": "EPSG:4326",
        "bbox": {"xmin": -106.8, "ymin": 57.0, "xmax": -105.9, "ymax": 57.6},
        "geometry_status": "mock_bbox_only",
        "limitations": ["Mock AOI for MCP testing; not authoritative geometry."],
    }
}

MOCK_WATER_SAMPLES = [
    {
        "project_id": "om-prj-uranium-001",
        "aoi_id": "aoi-main",
        "sample_id": "GW-001",
        "sample_types": ["groundwater", "well"],
        "location": {"x": -106.42, "y": 57.21},
        "crs": "EPSG:4326",
        "sample_date": "2025-08-10",
        "depth_interval": {"from_m": 42.0, "to_m": 55.0},
        "field_parameters": {"pH": 7.2, "Eh_mV": 165, "EC_uS_cm": 540, "T_C": 8.4},
        "lab_analytes": {
            "U": {"value": 8.1, "unit": "ug/L"},
            "Ra226": {"value": 0.08, "unit": "Bq/L"},
            "Rn222": {"value": 19.0, "unit": "Bq/L"},
            "Pb210": {"value": 0.012, "unit": "Bq/L"},
            "Po210": {"value": 0.006, "unit": "Bq/L"},
            "Ca": {"value": 42.0, "unit": "mg/L"},
            "Mg": {"value": 11.0, "unit": "mg/L"},
            "HCO3": {"value": 155.0, "unit": "mg/L"},
            "SO4": {"value": 31.0, "unit": "mg/L"},
        },
        "units": {"metals": "ug/L", "radionuclides": "Bq/L", "major_ions": "mg/L"},
        "detection_limits": {"U": "0.05 ug/L", "Ra226": "0.005 Bq/L", "Rn222": "1 Bq/L"},
        "qaqc_flags": ["mock", "charge_balance_not_checked"],
        "source_file_id": "mock-water-chemistry-2026",
        "provenance": {"source": "GeoMine THMC mock water chemistry", "mode": "mock"},
    },
    {
        "project_id": "om-prj-uranium-001",
        "aoi_id": "aoi-main",
        "sample_id": "GW-002",
        "sample_types": ["groundwater", "well"],
        "location": {"x": -106.31, "y": 57.28},
        "crs": "EPSG:4326",
        "sample_date": "2025-08-11",
        "depth_interval": {"from_m": 60.0, "to_m": 75.0},
        "field_parameters": {"pH": 6.9, "Eh_mV": 210, "EC_uS_cm": 610, "T_C": 9.1},
        "lab_analytes": {
            "U": {"value": 13.4, "unit": "ug/L"},
            "Ra226": {"value": 0.11, "unit": "Bq/L"},
            "Rn222": {"value": 24.0, "unit": "Bq/L"},
            "Pb210": {"value": 0.015, "unit": "Bq/L"},
            "Po210": {"value": 0.007, "unit": "Bq/L"},
            "Ca": {"value": 49.0, "unit": "mg/L"},
            "Mg": {"value": 13.0, "unit": "mg/L"},
            "HCO3": {"value": 172.0, "unit": "mg/L"},
            "SO4": {"value": 44.0, "unit": "mg/L"},
        },
        "units": {"metals": "ug/L", "radionuclides": "Bq/L", "major_ions": "mg/L"},
        "detection_limits": {"U": "0.05 ug/L", "Ra226": "0.005 Bq/L", "Rn222": "1 Bq/L"},
        "qaqc_flags": ["mock", "duplicate_required"],
        "source_file_id": "mock-water-chemistry-2026",
        "provenance": {"source": "GeoMine THMC mock water chemistry", "mode": "mock"},
    },
]

MOCK_LITHOLOGY = [
    {
        "project_id": "om-prj-uranium-001",
        "aoi_id": "aoi-main",
        "unit_id": "granite-fractured-001",
        "lithology": "fractured granite basement",
        "geometry_status": "mock_2d_cross_section_unit",
        "porosity": 0.015,
        "permeability_m2": 1.0e-15,
        "fracture_density": "moderate; mock",
        "source": "GeoMine THMC mock lithology",
        "confidence": "low",
        "limitations": ["Mock lithology; not from core logs."],
    },
    {
        "project_id": "om-prj-uranium-001",
        "aoi_id": "aoi-main",
        "unit_id": "sandstone-cover-001",
        "lithology": "Athabasca-like sandstone cover",
        "geometry_status": "mock_2d_cross_section_unit",
        "porosity": 0.12,
        "permeability_m2": 5.0e-14,
        "fracture_density": "low; mock",
        "source": "GeoMine THMC mock lithology",
        "confidence": "low",
        "limitations": ["Mock lithology; not a regional geological model."],
    },
]

MOCK_MINERALS = [
    {
        "project_id": "om-prj-uranium-001",
        "unit_id": "granite-fractured-001",
        "minerals": [
            {"name": "quartz", "volume_fraction": 0.35},
            {"name": "calcite", "volume_fraction": 0.02},
            {"name": "goethite", "volume_fraction": 0.01},
            {"name": "clay", "volume_fraction": 0.04},
            {"name": "barite", "volume_fraction": 0.002},
        ],
        "reactive_surface_area": "required measurement",
        "source": "GeoMine THMC mock mineral assemblage",
        "confidence": "low",
        "limitations": ["Mock mineral fractions; XRD/QEMSCAN required before modeling."],
    }
]

MOCK_ASSETS = [
    {
        "project_id": "om-prj-uranium-001",
        "asset_id": "mesh-2d-cross-section-001",
        "name": "mock_2d_fractured_cross_section.vtu",
        "asset_type": "mesh",
        "field_name": "mesh",
        "format": "VTU",
        "storage": "r2",
        "crs": "EPSG:32613",
        "data_version": "mock-2026-05-12",
        "checksum": "sha256:mockmesh001",
    },
    {
        "project_id": "om-prj-uranium-001",
        "asset_id": "field-k-001",
        "name": "hydraulic_conductivity_field.gpkg",
        "asset_type": "parameter_field",
        "field_name": "hydraulic_conductivity",
        "format": "geopackage",
        "storage": "r2",
        "crs": "EPSG:32613",
        "data_version": "mock-2026-05-12",
        "checksum": "sha256:mockkfield001",
    },
    {
        "project_id": "om-prj-uranium-001",
        "asset_id": "field-porosity-001",
        "name": "porosity_field.gpkg",
        "asset_type": "parameter_field",
        "field_name": "porosity",
        "format": "geopackage",
        "storage": "r2",
        "crs": "EPSG:32613",
        "data_version": "mock-2026-05-12",
        "checksum": "sha256:mockporosity001",
    },
    {
        "project_id": "om-prj-uranium-001",
        "asset_id": "field-temperature-001",
        "name": "temperature_field.gpkg",
        "asset_type": "parameter_field",
        "field_name": "temperature",
        "format": "geopackage",
        "storage": "r2",
        "crs": "EPSG:32613",
        "data_version": "mock-2026-05-12",
        "checksum": "sha256:mocktemp001",
    },
]

MOCK_DGR_CAMPAIGNS = [
    {
        "campaign_id": "dgr-campaign-revell-mock-001",
        "project_id": "om-prj-dgr-001",
        "name": "Revell-style DGR THMC field data mock campaign",
        "site_type": "deep_geological_repository",
        "status": "planned",
        "coordinate_reference_system": "EPSG:4326",
        "depth_reference": "ground_surface",
        "target_processes": ["T", "H", "M", "C"],
        "planned_measurement_groups": [
            "borehole collar and deviation",
            "hydraulic packer tests",
            "groundwater chemistry and isotopes",
            "thermal conductivity and temperature logging",
            "rock mechanics and in-situ stress",
            "microseismic / deformation monitoring",
        ],
        "qaqc_policy": "Mock campaign only; real campaigns require chain-of-custody, calibration certificates, and signed lab reports.",
        "created_at": "2026-05-12T00:00:00Z",
    }
]


class THMCStorage:
    def __init__(self, cache_dir: Path | None = None, mode: str = "mock") -> None:
        self.cache_dir = cache_dir or load_config().cache_dir
        self.mode = mode
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def _json_path(self, name: str) -> Path:
        return self.cache_dir / f"{name}.json"

    def _read_list(self, name: str) -> list[dict[str, Any]]:
        path = self._json_path(name)
        if not path.exists():
            return []
        return json.loads(path.read_text(encoding="utf-8"))

    def _write_list(self, name: str, values: list[dict[str, Any]]) -> None:
        self._json_path(name).write_text(json.dumps(values, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def list_projects(self, status: str | None = None, jurisdiction: str | None = None, commodity: str | None = None, limit: int = 20) -> list[dict[str, Any]]:
        projects = MOCK_PROJECTS
        if status:
            projects = [item for item in projects if item.get("status") == status]
        if jurisdiction:
            projects = [item for item in projects if jurisdiction.lower() in item["jurisdiction"].lower()]
        if commodity:
            projects = [item for item in projects if commodity.lower() in [str(c).lower() for c in item.get("commodity", [])]]
        return projects[: max(1, min(limit, 100))]

    def get_project(self, project_id: str) -> dict[str, Any] | None:
        return next((item for item in MOCK_PROJECTS if item["project_id"] == project_id), None)

    def list_dgr_campaigns(
        self,
        project_id: str | None = None,
        site_type: str | None = None,
        status: str | None = None,
        limit: int = 20,
    ) -> list[dict[str, Any]]:
        values = self._read_list("dgr_campaigns") or MOCK_DGR_CAMPAIGNS
        if project_id:
            values = [item for item in values if item["project_id"] == project_id]
        if site_type:
            values = [item for item in values if item.get("site_type") == site_type]
        if status:
            values = [item for item in values if item.get("status") == status]
        return values[: max(1, min(limit, 100))]

    def get_dgr_campaign(self, campaign_id: str) -> dict[str, Any] | None:
        return next((item for item in self.list_dgr_campaigns(limit=100) if item["campaign_id"] == campaign_id), None)

    def get_aoi(self, project_id: str, aoi_id: str | None = None) -> dict[str, Any] | None:
        aoi = MOCK_AOIS.get(project_id)
        if aoi_id and aoi and aoi.get("aoi_id") != aoi_id:
            return None
        return aoi

    def query_water_samples(self, project_id: str, aoi_id: str | None = None, analytes: list[str] | None = None, sample_types: list[str] | None = None, limit: int = 5000) -> tuple[list[dict[str, Any]], list[str]]:
        warnings: list[str] = []
        samples = [item for item in MOCK_WATER_SAMPLES if item["project_id"] == project_id]
        if aoi_id:
            samples = [item for item in samples if item["aoi_id"] == aoi_id]
        if sample_types:
            lowered = {item.lower() for item in sample_types}
            samples = [item for item in samples if lowered.intersection({s.lower() for s in item.get("sample_types", [])})]
        if analytes:
            available = {key for sample in samples for key in sample.get("lab_analytes", {})} | {"pH", "Eh", "EC", "T"}
            missing = [item for item in analytes if item not in available and item.replace("-", "") not in available]
            if missing:
                warnings.append(f"Analytes not present in mock data: {', '.join(missing)}")
        return samples[: max(1, min(limit, 10000))], warnings

    def query_lithology(self, project_id: str, aoi_id: str | None = None) -> list[dict[str, Any]]:
        units = [item for item in MOCK_LITHOLOGY if item["project_id"] == project_id]
        if aoi_id:
            units = [item for item in units if item["aoi_id"] == aoi_id]
        return units

    def query_minerals(self, project_id: str, unit_id: str | None = None) -> list[dict[str, Any]]:
        minerals = [item for item in MOCK_MINERALS if item["project_id"] == project_id]
        if unit_id:
            minerals = [item for item in minerals if item["unit_id"] == unit_id]
        return minerals

    def list_assets(self, project_id: str, asset_type: str | None = None, field_name: str | None = None) -> list[dict[str, Any]]:
        assets = [item for item in MOCK_ASSETS if item["project_id"] == project_id]
        if asset_type:
            assets = [item for item in assets if item["asset_type"] == asset_type]
        if field_name:
            assets = [item for item in assets if item["field_name"] == field_name]
        return assets

    def get_asset(self, project_id: str, asset_type: str, field_name: str | None = None) -> dict[str, Any] | None:
        assets = self.list_assets(project_id, asset_type=asset_type, field_name=field_name)
        return assets[0] if assets else None

    def save_model_version(self, payload: dict[str, Any]) -> dict[str, Any]:
        values = self._read_list("model_versions")
        model_version = {
            "model_version_id": payload.get("model_version_id") or f"thmc-model-version-{uuid4().hex[:10]}",
            "project_id": payload["project_id"],
            "model_id": payload["model_id"],
            "version_label": payload["version_label"],
            "model_spec": payload.get("model_spec", {}),
            "source_asset_ids": payload.get("source_asset_ids", []),
            "notes": payload.get("notes", ""),
            "saved_at": now_iso(),
        }
        values.append(model_version)
        self._write_list("model_versions", values)
        return model_version

    def get_model_version(self, model_version_id: str) -> dict[str, Any] | None:
        return next((item for item in self._read_list("model_versions") if item["model_version_id"] == model_version_id), None)

    def list_model_versions(self, project_id: str | None = None, model_id: str | None = None) -> list[dict[str, Any]]:
        values = self._read_list("model_versions")
        if project_id:
            values = [item for item in values if item["project_id"] == project_id]
        if model_id:
            values = [item for item in values if item["model_id"] == model_id]
        return values

    def save_run_record(self, payload: dict[str, Any]) -> dict[str, Any]:
        values = self._read_list("run_records")
        raw_hash = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
        run_record = {
            "run_id": payload.get("run_id") or f"thmc-run-{uuid4().hex[:10]}",
            "project_id": payload["project_id"],
            "model_id": payload["model_id"],
            "model_version_id": payload["model_version_id"],
            "solver": payload["solver"],
            "solver_version": payload.get("solver_version", "mock"),
            "input_asset_ids": payload.get("input_asset_ids", []),
            "output_asset_ids": payload.get("output_asset_ids", []),
            "parameters_hash": payload.get("parameters_hash") or "sha256:" + hashlib.sha256(raw_hash).hexdigest(),
            "data_hash": payload.get("data_hash") or "sha256:mock-data",
            "submitted_at": payload.get("submitted_at") or now_iso(),
            "completed_at": payload.get("completed_at"),
            "status": payload.get("status", "completed"),
            "error_log": payload.get("error_log"),
            "warnings": payload.get("warnings", ["mock run record"]),
            "created_by": payload.get("created_by", "geomine-thmc-mcp"),
        }
        values.append(run_record)
        self._write_list("run_records", values)
        return run_record

    def get_run_record(self, run_id: str) -> dict[str, Any] | None:
        return next((item for item in self._read_list("run_records") if item["run_id"] == run_id), None)

    def list_run_records(self, project_id: str | None = None, model_id: str | None = None) -> list[dict[str, Any]]:
        values = self._read_list("run_records")
        if project_id:
            values = [item for item in values if item["project_id"] == project_id]
        if model_id:
            values = [item for item in values if item["model_id"] == model_id]
        return values

    def save_compute_job(self, payload: dict[str, Any]) -> dict[str, Any]:
        values = self._read_list("compute_jobs")
        job = {
            "job_id": payload.get("job_id") or f"{payload['solver'].lower()}-job-{uuid4().hex[:10]}",
            "solver": payload["solver"],
            "status": payload.get("status", "submitted"),
            "model_version_id": payload["model_version_id"],
            "project_id": payload["project_id"],
            "input_assets": payload.get("input_assets", {}),
            "compute_profile": payload.get("compute_profile", {}),
            "submitted_at": now_iso(),
        }
        values.append(job)
        self._write_list("compute_jobs", values)
        return job

    def get_compute_job(self, job_id: str) -> dict[str, Any] | None:
        return next((item for item in self._read_list("compute_jobs") if item["job_id"] == job_id), None)

    def update_compute_job(self, job_id: str, **updates: Any) -> dict[str, Any] | None:
        values = self._read_list("compute_jobs")
        for index, job in enumerate(values):
            if job["job_id"] == job_id:
                values[index] = {**job, **updates}
                self._write_list("compute_jobs", values)
                return values[index]
        return None

    def save_dgr_record(self, record_type: str, payload: dict[str, Any]) -> dict[str, Any]:
        values = self._read_list("dgr_records")
        raw_hash = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
        record = {
            "record_id": payload.get("record_id") or f"dgr-{record_type}-{uuid4().hex[:10]}",
            "record_type": record_type,
            "project_id": payload["project_id"],
            "campaign_id": payload.get("campaign_id"),
            "borehole_id": payload.get("borehole_id"),
            "depth_m": payload.get("depth_m"),
            "depth_interval": payload.get("depth_interval"),
            "measurement_type": payload.get("measurement_type", record_type),
            "values": payload.get("values", {}),
            "units": payload.get("units", {}),
            "method": payload.get("method"),
            "source": payload.get("source", "geomine_thmc_data MCP local/mock ingestion"),
            "qaqc_flags": payload.get("qaqc_flags", ["mock_or_unverified"]),
            "provenance": payload.get("provenance", {}),
            "created_at": payload.get("created_at") or now_iso(),
            "data_hash": "sha256:" + hashlib.sha256(raw_hash).hexdigest(),
        }
        values.append(record)
        self._write_list("dgr_records", values)
        return record

    def list_dgr_records(
        self,
        project_id: str | None = None,
        campaign_id: str | None = None,
        record_type: str | None = None,
        borehole_id: str | None = None,
    ) -> list[dict[str, Any]]:
        values = self._read_list("dgr_records")
        if project_id:
            values = [item for item in values if item["project_id"] == project_id]
        if campaign_id:
            values = [item for item in values if item.get("campaign_id") == campaign_id]
        if record_type:
            values = [item for item in values if item["record_type"] == record_type]
        if borehole_id:
            values = [item for item in values if item.get("borehole_id") == borehole_id]
        return values

    def save_dgr_data_package(self, payload: dict[str, Any]) -> dict[str, Any]:
        values = self._read_list("dgr_data_packages")
        raw_hash = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
        package = {
            "package_id": payload.get("package_id") or f"dgr-data-package-{uuid4().hex[:10]}",
            "project_id": payload["project_id"],
            "campaign_id": payload.get("campaign_id"),
            "package_label": payload["package_label"],
            "dataset_ids": payload.get("dataset_ids", []),
            "package_spec": payload.get("package_spec", {}),
            "notes": payload.get("notes", ""),
            "created_at": payload.get("created_at") or now_iso(),
            "data_hash": "sha256:" + hashlib.sha256(raw_hash).hexdigest(),
        }
        values.append(package)
        self._write_list("dgr_data_packages", values)
        return package

    def get_dgr_data_package(self, package_id: str) -> dict[str, Any] | None:
        return next((item for item in self._read_list("dgr_data_packages") if item["package_id"] == package_id), None)

    def list_dgr_data_packages(
        self,
        project_id: str | None = None,
        campaign_id: str | None = None,
    ) -> list[dict[str, Any]]:
        values = self._read_list("dgr_data_packages")
        if project_id:
            values = [item for item in values if item["project_id"] == project_id]
        if campaign_id:
            values = [item for item in values if item.get("campaign_id") == campaign_id]
        return values

    def save_pflotran_model_package(self, payload: dict[str, Any]) -> dict[str, Any]:
        values = self._read_list("pflotran_model_packages")
        raw_hash = json.dumps(payload, sort_keys=True, default=str).encode("utf-8")
        package = {
            "package_id": payload.get("package_id") or f"pflotran-package-{uuid4().hex[:10]}",
            "project_id": payload["project_id"],
            "package_label": payload["package_label"],
            "package_spec": payload.get("package_spec", {}),
            "source_asset_ids": payload.get("source_asset_ids", []),
            "notes": payload.get("notes", ""),
            "created_at": payload.get("created_at") or now_iso(),
            "status": payload.get("status", "draft_not_executed"),
            "package_hash": "sha256:" + hashlib.sha256(raw_hash).hexdigest(),
        }
        values.append(package)
        self._write_list("pflotran_model_packages", values)
        return package

    def get_pflotran_model_package(self, package_id: str) -> dict[str, Any] | None:
        return next((item for item in self._read_list("pflotran_model_packages") if item["package_id"] == package_id), None)

    def list_pflotran_model_packages(self, project_id: str | None = None) -> list[dict[str, Any]]:
        values = self._read_list("pflotran_model_packages")
        if project_id:
            values = [item for item in values if item["project_id"] == project_id]
        return values


_DEFAULT_STORAGE: THMCStorage | None = None


def get_default_storage() -> THMCStorage:
    global _DEFAULT_STORAGE
    if _DEFAULT_STORAGE is None:
        config = load_config()
        _DEFAULT_STORAGE = THMCStorage(cache_dir=config.cache_dir, mode=config.mode or "mock")
    return _DEFAULT_STORAGE
