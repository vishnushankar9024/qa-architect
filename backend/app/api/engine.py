from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.services import pipeline
from app.store import store

router = APIRouter(prefix="/engine", tags=["engine"])


def _project_context(project_id: str) -> tuple[str, list[str]]:
    project = store.projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    source_descriptors = []
    for source in store.sources[project_id]:
        metadata = source["metadata"]
        source_descriptors.append(
            metadata.get("url", metadata.get("fileName", source["sourceType"]))
        )
    return project["name"], source_descriptors


@router.get("/discovery/{project_id}")
def discovery(project_id: str) -> dict[str, list[str]]:
    project_name, source_descriptors = _project_context(project_id)
    return {"discovery": pipeline.discovery(project_name, source_descriptors)}


@router.get("/features/{project_id}")
def features(project_id: str) -> dict[str, list[dict[str, str]]]:
    project_name, source_descriptors = _project_context(project_id)
    discovered = pipeline.discovery(project_name, source_descriptors)
    return {"features": [item.model_dump() for item in pipeline.features(discovered)]}


@router.get("/domains/{project_id}")
def domains(project_id: str) -> dict[str, list[dict[str, str]]]:
    project_name, source_descriptors = _project_context(project_id)
    discovered = pipeline.discovery(project_name, source_descriptors)
    feature_items = pipeline.features(discovered)
    return {"domains": [item.model_dump() for item in pipeline.domains(feature_items)]}


@router.get("/traceability/{project_id}")
def traceability(project_id: str) -> dict[str, list[dict[str, str]]]:
    project_name, source_descriptors = _project_context(project_id)
    discovered = pipeline.discovery(project_name, source_descriptors)
    feature_items = pipeline.features(discovered)
    domain_items = pipeline.domains(feature_items)
    trace_items = pipeline.traceability(feature_items, domain_items)
    return {"traceability": [item.model_dump() for item in trace_items]}


@router.get("/business-rules/{project_id}")
def business_rules(project_id: str) -> dict[str, list[dict[str, str]]]:
    project_name, source_descriptors = _project_context(project_id)
    discovered = pipeline.discovery(project_name, source_descriptors)
    feature_items = pipeline.features(discovered)
    return {
        "business_rules": [
            item.model_dump() for item in pipeline.business_rules(feature_items)
        ]
    }


@router.get("/flow-discovery/{project_id}")
def flow_discovery(project_id: str) -> dict[str, list[dict[str, str]]]:
    project_name, source_descriptors = _project_context(project_id)
    discovered = pipeline.discovery(project_name, source_descriptors)
    feature_items = pipeline.features(discovered)
    domain_items = pipeline.domains(feature_items)
    rule_items = pipeline.business_rules(feature_items)
    flow_items = pipeline.flow_discovery(domain_items, rule_items)
    return {"flows": [item.model_dump() for item in flow_items]}


@router.get("/pipeline/{project_id}")
def run_pipeline(project_id: str) -> dict[str, list[dict[str, str]]]:
    project_name, source_descriptors = _project_context(project_id)
    output = pipeline.run_pipeline(project_name, source_descriptors)
    return {
        "features": [item.model_dump() for item in output.features],
        "domains": [item.model_dump() for item in output.domains],
        "traceability": [item.model_dump() for item in output.traceability],
        "business_rules": [item.model_dump() for item in output.business_rules],
        "flows": [item.model_dump() for item in output.flows],
    }
