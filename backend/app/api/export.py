from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import PlainTextResponse

from app.services.exporter import approved_knowledge_pack, to_csv, to_json, to_markdown
from app.store import store

router = APIRouter(tags=["export"])


@router.get("/export/{project_id}")
def export_knowledge(
    project_id: str, format: str = Query(default="json", pattern="^(json|markdown|csv)$")
) -> PlainTextResponse:
    if not store.project_exists(project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    knowledge = store.get_knowledge_base(project_id)
    if not knowledge:
        raise HTTPException(status_code=404, detail="Knowledge base not found")

    knowledge_pack = approved_knowledge_pack(knowledge)
    if format == "json":
        body = to_json(knowledge_pack)
        media_type = "application/json"
        extension = "json"
    elif format == "markdown":
        body = to_markdown(knowledge_pack)
        media_type = "text/markdown"
        extension = "md"
    else:
        body = to_csv(knowledge_pack)
        media_type = "text/csv"
        extension = "csv"
    store.log_event(
        action="knowledge.exported",
        details={"projectId": project_id, "format": format},
    )

    headers = {
        "Content-Disposition": f'attachment; filename="knowledge-pack-{project_id}.{extension}"'
    }
    return PlainTextResponse(content=body, media_type=media_type, headers=headers)
