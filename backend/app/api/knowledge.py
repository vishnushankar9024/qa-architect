from __future__ import annotations

import json

from fastapi import APIRouter, HTTPException

from app.schemas import DashboardMetrics, KnowledgeBase, ProjectStatus
from app.services.pipeline import PIPELINE_STAGES, run_pipeline
from app.store import store

router = APIRouter(tags=["knowledge"])


def _get_knowledge_or_404(project_id: str) -> dict:
    knowledge = store.get_knowledge_base(project_id)
    if not knowledge:
        raise HTTPException(status_code=404, detail="Knowledge base not generated")
    return knowledge


@router.post("/knowledge-base/{project_id}", response_model=KnowledgeBase)
def generate_knowledge_base(project_id: str) -> KnowledgeBase:
    project = store.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    store.set_project_status(project_id, ProjectStatus.knowledge_generation.value)
    source_descriptors = []
    for source in store.list_sources(project_id):
        metadata = source["metadata"]
        source_descriptors.append(
            metadata.get("url", metadata.get("fileName", source["sourceType"]))
        )

    output = run_pipeline(project["name"], source_descriptors)
    knowledge = KnowledgeBase(
        project={
            "id": project["id"],
            "name": project["name"],
            "status": ProjectStatus.knowledge_generation.value,
            "stages": list(PIPELINE_STAGES),
        },
        features=output.features,
        domains=output.domains,
        flows=output.flows,
        business_rules=output.business_rules,
        traceability=output.traceability,
    )
    store.set_knowledge_base(project_id, knowledge.model_dump(mode="json"))
    store.set_project_status(project_id, ProjectStatus.review.value)
    store.log_event(
        action="knowledge.generated",
        details={"projectId": project_id, "sourcesCount": len(source_descriptors)},
    )

    project_dir = store.project_path(project_id)
    artifact_path = project_dir / "knowledge-base.json"
    artifact_path.write_text(
        json.dumps(store.get_knowledge_base(project_id), indent=2), encoding="utf-8"
    )
    return KnowledgeBase(**store.get_knowledge_base(project_id))


@router.get("/knowledge-base/{project_id}", response_model=KnowledgeBase)
def get_knowledge_base(project_id: str) -> KnowledgeBase:
    if not store.project_exists(project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    knowledge = _get_knowledge_or_404(project_id)
    return KnowledgeBase(**knowledge)


@router.get("/knowledge-base/{project_id}/dashboard", response_model=DashboardMetrics)
def get_dashboard_metrics(project_id: str) -> DashboardMetrics:
    if not store.project_exists(project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    knowledge = _get_knowledge_or_404(project_id)
    feature_count = len(knowledge["features"])
    domain_count = len(knowledge["domains"])
    rule_count = len(knowledge["business_rules"])
    flow_count = len(knowledge["flows"])
    all_items = (
        knowledge["features"]
        + knowledge["domains"]
        + knowledge["business_rules"]
        + knowledge["flows"]
    )
    approved = [item for item in all_items if item["status"] == "Approved"]
    approval_percentage = (
        round((len(approved) / len(all_items)) * 100, 2) if all_items else 0.0
    )

    coverage_metrics = {
        "traceabilityCoverage": round(
            (len(knowledge["traceability"]) / feature_count) * 100, 2
        )
        if feature_count
        else 0.0,
        "rulesPerFeature": round(rule_count / feature_count, 2) if feature_count else 0.0,
        "flowsPerDomain": round(flow_count / domain_count, 2) if domain_count else 0.0,
    }
    return DashboardMetrics(
        featureCount=feature_count,
        domainCount=domain_count,
        ruleCount=rule_count,
        flowCount=flow_count,
        approvalPercentage=approval_percentage,
        coverageMetrics=coverage_metrics,
    )
