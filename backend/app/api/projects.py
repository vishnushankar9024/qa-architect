from __future__ import annotations

from fastapi import APIRouter, HTTPException

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


@router.get("/projects", response_model=list[Project])
def list_projects() -> list[Project]:
    projects = [Project(**project) for project in store.projects.values()]
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
    store.projects[project.id] = project.model_dump()
    return project


@router.get("/project/{project_id}", response_model=Project)
def get_project(project_id: str) -> Project:
    project = store.projects.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return Project(**project)


@router.get("/projects/{project_id}/sources", response_model=list[KnowledgeSource])
def list_sources(project_id: str) -> list[KnowledgeSource]:
    if project_id not in store.projects:
        raise HTTPException(status_code=404, detail="Project not found")
    return [KnowledgeSource(**source) for source in store.sources[project_id]]


@router.post("/projects/{project_id}/sources/repository", response_model=KnowledgeSource)
def add_repository_source(
    project_id: str, request: RepositorySourceCreateRequest
) -> KnowledgeSource:
    if project_id not in store.projects:
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
    store.sources[project_id].append(source.model_dump())
    return source


@router.post("/projects/{project_id}/sources/document", response_model=KnowledgeSource)
def add_document_source(
    project_id: str, request: DocumentSourceCreateRequest
) -> KnowledgeSource:
    if project_id not in store.projects:
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
    store.sources[project_id].append(source.model_dump())
    return source
