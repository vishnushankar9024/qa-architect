from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.schemas import ArtifactType, ReviewRequest, ReviewResponse, ReviewStatus, utc_now
from app.store import store

router = APIRouter(tags=["review"])


def _find_item(items: list[dict], item_id: str) -> dict | None:
    for item in items:
        if item["id"] == item_id:
            return item
    return None


@router.post("/review", response_model=ReviewResponse)
def review_item(request: ReviewRequest) -> ReviewResponse:
    if not store.project_exists(request.projectId):
        raise HTTPException(status_code=404, detail="Project not found")
    knowledge = store.get_knowledge_base(request.projectId)
    if not knowledge:
        raise HTTPException(status_code=404, detail="Knowledge base not found")

    artifact_key = request.artifactType.value
    if artifact_key not in knowledge:
        raise HTTPException(status_code=400, detail="Invalid artifact type")
    item = _find_item(knowledge[artifact_key], request.itemId)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if request.action == "approve":
        item["status"] = ReviewStatus.approved.value
        item["approvedBy"] = request.reviewer
        item["approvedDate"] = utc_now().isoformat()
    elif request.action == "reject":
        item["status"] = ReviewStatus.rejected.value
        item["approvedBy"] = None
        item["approvedDate"] = None
    elif request.action == "edit":
        if request.name:
            item["name"] = request.name
        if request.description:
            item["description"] = request.description
    else:
        raise HTTPException(status_code=400, detail="Invalid action")

    if request.action == "approve":
        review_status = ReviewStatus.approved
    elif request.action == "reject":
        review_status = ReviewStatus.rejected
    else:
        review_status = ReviewStatus(item["status"])
    store.append_review_log(
        {
            "projectId": request.projectId,
            "artifactType": request.artifactType.value,
            "itemId": request.itemId,
            "action": request.action,
            "reviewer": request.reviewer,
            "timestamp": utc_now().isoformat(),
        }
    )

    all_items: list[dict] = []
    for key in (
        ArtifactType.features.value,
        ArtifactType.domains.value,
        ArtifactType.business_rules.value,
        ArtifactType.flows.value,
    ):
        all_items.extend(knowledge.get(key, []))
    if all_items and all(item["status"] == ReviewStatus.approved.value for item in all_items):
        store.set_project_status(request.projectId, "Approved")
    else:
        store.set_project_status(request.projectId, "Review")
    store.set_knowledge_base(request.projectId, knowledge)
    store.log_event(
        action="review.updated",
        details={
            "projectId": request.projectId,
            "artifactType": request.artifactType.value,
            "itemId": request.itemId,
            "action": request.action,
        },
    )

    return ReviewResponse(
        projectId=request.projectId,
        artifactType=request.artifactType,
        itemId=request.itemId,
        status=review_status,
        approvedBy=item.get("approvedBy"),
        approvedDate=item.get("approvedDate"),
    )
