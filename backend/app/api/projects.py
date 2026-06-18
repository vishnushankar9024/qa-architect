from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from app.schemas import (
    DocumentSourceCreateRequest,
    KnowledgeSource,
    Project,
    ProjectCreateRequest,
    ProjectStatus,
    RepositorySourceCreateRequest,
    SourceType,
    SourceStatus,
    generate_id,
    utc_now,
)
from app.store import store

router = APIRouter(tags=["projects"])

DOCUMENT_SOURCE_TYPES = {
    SourceType.pdf,
    SourceType.docx,
    SourceType.xlsx,
    SourceType.pptx,
    SourceType.txt,
    SourceType.markdown,
}
REPOSITORY_SOURCE_TYPES = {SourceType.github, SourceType.gitlab, SourceType.bitbucket}
DOCUMENT_EXTENSION_MAP = {
    ".pdf": SourceType.pdf,
    ".docx": SourceType.docx,
    ".xlsx": SourceType.xlsx,
    ".pptx": SourceType.pptx,
    ".txt": SourceType.txt,
    ".md": SourceType.markdown,
    ".markdown": SourceType.markdown,
}


def _document_source_type(file_name: str) -> SourceType:
    extension = Path(file_name).suffix.lower()
    source_type = DOCUMENT_EXTENSION_MAP.get(extension)
    if not source_type:
        raise HTTPException(
            status_code=400,
            detail=(
                "Unsupported file type. Allowed: PDF, DOCX, XLSX, PPTX, TXT, Markdown"
            ),
        )
    return source_type


@router.get("/projects", response_model=list[Project])
def list_projects() -> list[Project]:
    projects = [Project(**project) for project in store.list_projects()]
    return sorted(projects, key=lambda project: project.createdDate, reverse=True)


@router.post("/projects", response_model=Project)
def create_project(request: ProjectCreateRequest) -> Project:
    project = Project(
        id=generate_id("proj"),
        name=request.name,
        description=request.description,
        createdBy=request.createdBy,
        createdDate=utc_now(),
        status=ProjectStatus.draft,
    )
    store.save_project(project.model_dump())
    store.log_event(
        action="project.created",
        details={"projectId": project.id, "createdBy": request.createdBy},
    )
    return project


@router.get("/project/{project_id}", response_model=Project)
def get_project(project_id: str) -> Project:
    project = store.get_project(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return Project(**project)


@router.get("/projects/{project_id}/sources", response_model=list[KnowledgeSource])
def list_sources(project_id: str) -> list[KnowledgeSource]:
    if not store.project_exists(project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    return [KnowledgeSource(**source) for source in store.list_sources(project_id)]


@router.post("/projects/{project_id}/sources/repository", response_model=KnowledgeSource)
def add_repository_source(
    project_id: str, request: RepositorySourceCreateRequest
) -> KnowledgeSource:
    if not store.project_exists(project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    if request.sourceType not in REPOSITORY_SOURCE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid repository source type")
    source = KnowledgeSource(
        id=generate_id("src"),
        projectId=project_id,
        sourceType=request.sourceType,
        status=SourceStatus.uploaded,
        createdBy=request.createdBy,
        createdDate=utc_now(),
        metadata={"url": str(request.url)},
    )
    store.add_source(source.model_dump())
    store.log_event(
        action="source.repository.registered",
        details={"projectId": project_id, "sourceId": source.id, "sourceType": source.sourceType.value},
    )
    return source


@router.post("/projects/{project_id}/sources/document", response_model=KnowledgeSource)
def add_document_source(
    project_id: str, request: DocumentSourceCreateRequest
) -> KnowledgeSource:
    if not store.project_exists(project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    if request.sourceType not in DOCUMENT_SOURCE_TYPES:
        raise HTTPException(status_code=400, detail="Invalid document source type")
    source = KnowledgeSource(
        id=generate_id("src"),
        projectId=project_id,
        sourceType=request.sourceType,
        status=SourceStatus.uploaded,
        createdBy=request.createdBy,
        createdDate=utc_now(),
        metadata={"fileName": request.fileName, "fileSizeBytes": request.fileSizeBytes},
    )
    store.add_source(source.model_dump())
    store.log_event(
        action="source.document.registered",
        details={"projectId": project_id, "sourceId": source.id, "sourceType": source.sourceType.value},
    )
    return source


@router.post("/projects/{project_id}/sources/documents", response_model=list[KnowledgeSource])
async def add_document_sources(
    project_id: str,
    createdBy: str = Form(min_length=2, max_length=120),
    files: list[UploadFile] = File(...),
) -> list[KnowledgeSource]:
    if not store.project_exists(project_id):
        raise HTTPException(status_code=404, detail="Project not found")
    created_sources: list[KnowledgeSource] = []
    for upload in files:
        source_type = _document_source_type(upload.filename or "")
        source = KnowledgeSource(
            id=generate_id("src"),
            projectId=project_id,
            sourceType=source_type,
            status=SourceStatus.uploaded,
            createdBy=createdBy,
            createdDate=utc_now(),
            metadata={"fileName": upload.filename or "unknown"},
        )
        file_bytes = await upload.read()
        source.metadata["fileSizeBytes"] = len(file_bytes)
        source.metadata["mimeType"] = upload.content_type or "application/octet-stream"
        await upload.seek(0)
        store.add_source(source.model_dump())
        created_sources.append(source)
        await upload.close()
    store.log_event(
        action="source.documents.registered.batch",
        details={
            "projectId": project_id,
            "sourceIds": [source.id for source in created_sources],
            "count": len(created_sources),
        },
    )
    return created_sources
