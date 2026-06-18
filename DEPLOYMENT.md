# QA Architect Portal - Cloud Run Deployment

This repository uses the same deployment style as `smart-gatekeeper`: Docker images + Google Cloud Run.

## Services

- Backend API service (FastAPI): `qa-architect-api`
- Frontend UI service (React static site via Nginx): `qa-architect-portal`

## Prerequisites

- Google Cloud SDK (`gcloud`) installed and authenticated.
- Docker installed and running.
- Access to your GCP project.
- Secret Manager secrets available:
  - `MONGO_URI`
  - `OPENAI_API_KEY`

## One-command deploy

From repo root:

`chmod +x deploy.sh`

`./deploy.sh <GCP_PROJECT_ID> <REGION>`

Example:

`./deploy.sh my-project us-central1`

## Optional environment overrides

- `BACKEND_SERVICE` (default `qa-architect-api`)
- `FRONTEND_SERVICE` (default `qa-architect-portal`)
- `MONGO_URI_SECRET` (default `MONGO_URI`)
- `OPENAI_API_KEY_SECRET` (default `OPENAI_API_KEY`)
- `MONGO_DB` (default `qa_architect_portal`)
- `API_BASE_URL_OVERRIDE` (if frontend should use custom backend URL/domain)

Example:

`API_BASE_URL_OVERRIDE=https://api.mycompany.com ./deploy.sh my-project us-central1`

## Post-deploy checks

1. Backend health:
   - `curl https://<backend-url>/health`
   - Response includes `"persistence":"mongodb"` when `MONGO_URI` is injected correctly.
2. Frontend health:
   - `curl https://<frontend-url>/health`
3. Open frontend URL and run flow:
   - create project
   - add repository and documents
   - generate knowledge base
   - approve and export

## Cloud Build option

You can also use `cloudbuild.yaml`.

Important:
- `_API_BASE_URL` substitution must point to your backend URL/domain.
- If backend URL changes, rerun frontend build/deploy with updated `_API_BASE_URL`.

Example:

`gcloud builds submit --config=cloudbuild.yaml --substitutions=_REGION=us-central1,_API_BASE_URL=https://qa-architect-api-xxxxx.run.app`
