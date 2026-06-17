from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4

from pydantic import BaseModel, Field, HttpUrl


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def generate_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex[:8]}"


class ProjectStatus(str, Enum):
    draft = "Draft"
    knowledge_generation = "Knowledge Generation"
    review = "Review"
    approved = "Approved"


class SourceType(str, Enum):
    github = "GitHub URL"
    gitlab = "GitLab URL"
    bitbucket = "Bitbucket URL"
    pdf = "PDF"
    docx = "DOCX"
    xlsx = "XLSX"
    pptx = "PPTX"
    txt = "TXT"
    markdown = "Markdown"


class SourceStatus(str, Enum):
    uploaded = "Uploaded"
    processing = "Processing"
    completed = "Completed"
    failed = "Failed"


class ReviewStatus(str, Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"


class ProjectCreateRequest(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    description: str = Field(default="", max_length=2000)
    createdBy: str = Field(min_length=2, max_length=120)


class Project(BaseModel):
    id: str
    name: str
    description: str
    createdBy: str
    createdDate: datetime
    status: ProjectStatus


class RepositorySourceCreateRequest(BaseModel):
    sourceType: SourceType
    url: HttpUrl
    createdBy: str = Field(min_length=2, max_length=120)


class DocumentSourceCreateRequest(BaseModel):
    sourceType: SourceType
    fileName: str = Field(min_length=1, max_length=255)
    fileSizeBytes: int = Field(ge=0)
    createdBy: str = Field(min_length=2, max_length=120)


class KnowledgeSource(BaseModel):
    id: str
    projectId: str
    sourceType: SourceType
    status: SourceStatus
    createdBy: str
    createdDate: datetime
    metadata: dict[str, Any]


class ArtifactType(str, Enum):
    features = "features"
    domains = "domains"
    flows = "flows"
    business_rules = "business_rules"
    traceability = "traceability"


class ReviewableItem(BaseModel):
    id: str
    name: str
    description: str
    status: ReviewStatus = ReviewStatus.pending
    approvedBy: str | None = None
    approvedDate: datetime | None = None


class TraceabilityItem(BaseModel):
    id: str
    source: str
    target: str
    status: ReviewStatus = ReviewStatus.pending
    approvedBy: str | None = None
    approvedDate: datetime | None = None


class KnowledgeBase(BaseModel):
    project: dict[str, Any]
    features: list[ReviewableItem]
    domains: list[ReviewableItem]
    flows: list[ReviewableItem]
    business_rules: list[ReviewableItem]
    traceability: list[TraceabilityItem]


class ReviewRequest(BaseModel):
    projectId: str
    artifactType: ArtifactType
    itemId: str
    action: str = Field(pattern="^(approve|reject|edit)$")
    reviewer: str = Field(min_length=2, max_length=120)
    name: str | None = None
    description: str | None = None


class ReviewResponse(BaseModel):
    projectId: str
    artifactType: ArtifactType
    itemId: str
    status: ReviewStatus
    approvedBy: str | None
    approvedDate: datetime | None


class DashboardMetrics(BaseModel):
    featureCount: int
    domainCount: int
    ruleCount: int
    flowCount: int
    approvalPercentage: float
    coverageMetrics: dict[str, float]
