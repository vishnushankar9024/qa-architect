# QA Architect Portal v1 Architecture

## Scope

Portal v1 includes:

- Project lifecycle management
- Knowledge source registration (repository + document metadata)
- Knowledge generation using existing QA Architect stages
- Human review and approval workflow
- Knowledge dashboard metrics
- Export of approved knowledge assets

Excluded for v1:

- Automation generation, Playwright generation, test strategy generation, scenario generation
- Video/audio/OCR/Document AI processing

## Backend

Technology: FastAPI (`backend/app`)

### API Surface

- `GET /projects`
- `POST /projects`
- `GET /project/{id}`
- `GET /projects/{id}/sources`
- `POST /projects/{id}/sources/repository`
- `POST /projects/{id}/sources/document`
- `GET /engine/discovery/{projectId}`
- `GET /engine/features/{projectId}`
- `GET /engine/domains/{projectId}`
- `GET /engine/traceability/{projectId}`
- `GET /engine/business-rules/{projectId}`
- `GET /engine/flow-discovery/{projectId}`
- `GET /engine/pipeline/{projectId}`
- `POST /knowledge-base/{projectId}`
- `GET /knowledge-base/{projectId}`
- `GET /knowledge-base/{projectId}/dashboard`
- `POST /review`
- `GET /export/{projectId}?format=json|markdown|csv`

### Pipeline Reuse

Portal generation preserves stage order:

`Discovery -> Features -> Domains -> Traceability -> Business Rules -> Flow Discovery`

The stage functions are centralized in `backend/app/services/pipeline.py` and exposed as legacy-compatible engine endpoints under `/engine/*`.

### Data Model (in-memory)

- `Project`: id, name, description, createdBy, createdDate, status
- `KnowledgeSource`: repository/document registration metadata with status
- `KnowledgeBase`: project + features/domains/flows/business_rules/traceability
- `Review`: approve/reject/edit actions with reviewer audit

Generated artifact is stored as:

- `backend/data/<projectId>/knowledge-base.json`

### Validation

- Request-level constraints via Pydantic:
  - required fields, string lengths
  - allowed enums for statuses and source types
  - URL validation for repository sources
  - review action contract (`approve|reject|edit`)

## Frontend

Technology: React + TypeScript + Material UI (`frontend/src`)

### Screens

- Projects (Project List + Create Project + Project Dashboard)
- Knowledge Sources
- Knowledge Dashboard
- Features Review
- Domains Review
- Business Rules Review
- Flow Review
- Exports

### UI Flow

1. Create/select project.
2. Register repository/document sources.
3. Generate knowledge base.
4. Review artifacts (approve/reject/edit).
5. Monitor dashboard metrics.
6. Export approved knowledge pack as JSON/Markdown/CSV.
