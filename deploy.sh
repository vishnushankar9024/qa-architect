#!/bin/bash
# Deploy QA Architect Portal (API + UI) to Google Cloud Run

set -euo pipefail

PROJECT_ID="${1:-}"
REGION="${2:-us-central1}"

BACKEND_SERVICE="${BACKEND_SERVICE:-qa-architect-api}"
FRONTEND_SERVICE="${FRONTEND_SERVICE:-qa-architect-portal}"
BACKEND_IMAGE="gcr.io/${PROJECT_ID}/${BACKEND_SERVICE}:latest"
FRONTEND_IMAGE="gcr.io/${PROJECT_ID}/${FRONTEND_SERVICE}:latest"
MONGO_URI_SECRET="${MONGO_URI_SECRET:-MONGO_URI}"
OPENAI_API_KEY_SECRET="${OPENAI_API_KEY_SECRET:-OPENAI_API_KEY}"
MONGO_DB="${MONGO_DB:-qa_architect_portal}"
API_BASE_URL_OVERRIDE="${API_BASE_URL_OVERRIDE:-}"

if [ -z "${PROJECT_ID}" ]; then
  echo "Usage: ./deploy.sh <GCP_PROJECT_ID> [REGION]"
  echo "Example: ./deploy.sh my-gcp-project us-central1"
  echo ""
  echo "Optional env vars:"
  echo "  BACKEND_SERVICE        (default: qa-architect-api)"
  echo "  FRONTEND_SERVICE       (default: qa-architect-portal)"
  echo "  MONGO_URI_SECRET       (default: MONGO_URI)"
  echo "  OPENAI_API_KEY_SECRET  (default: OPENAI_API_KEY)"
  echo "  MONGO_DB               (default: qa_architect_portal)"
  echo "  API_BASE_URL_OVERRIDE  (default: deployed backend URL)"
  exit 1
fi

echo "=========================================="
echo "Deploying QA Architect Portal to Cloud Run"
echo "=========================================="
echo "Project:          ${PROJECT_ID}"
echo "Region:           ${REGION}"
echo "Backend service:  ${BACKEND_SERVICE}"
echo "Frontend service: ${FRONTEND_SERVICE}"
echo ""

echo "Enabling required GCP APIs..."
gcloud services enable run.googleapis.com containerregistry.googleapis.com --project "${PROJECT_ID}"

echo "Configuring Docker auth for gcr.io..."
gcloud auth configure-docker --quiet

echo "Building backend image..."
docker build -f backend/Dockerfile -t "${BACKEND_IMAGE}" backend

echo "Pushing backend image..."
docker push "${BACKEND_IMAGE}"

echo "Deploying backend service..."
gcloud run deploy "${BACKEND_SERVICE}" \
  --project "${PROJECT_ID}" \
  --region "${REGION}" \
  --platform managed \
  --allow-unauthenticated \
  --image "${BACKEND_IMAGE}" \
  --memory 1Gi \
  --timeout 600 \
  --set-env-vars "MONGO_DB=${MONGO_DB}" \
  --set-secrets "MONGO_URI=${MONGO_URI_SECRET}:latest,OPENAI_API_KEY=${OPENAI_API_KEY_SECRET}:latest"

BACKEND_URL="$(gcloud run services describe "${BACKEND_SERVICE}" --project "${PROJECT_ID}" --region "${REGION}" --format='value(status.url)')"
if [ -z "${BACKEND_URL}" ]; then
  echo "Failed to determine backend URL."
  exit 1
fi

FRONTEND_API_URL="${API_BASE_URL_OVERRIDE:-${BACKEND_URL}}"
echo "Frontend will use API base URL: ${FRONTEND_API_URL}"

echo "Building frontend image..."
docker build \
  -f frontend/Dockerfile \
  --build-arg "VITE_API_BASE_URL=${FRONTEND_API_URL}" \
  -t "${FRONTEND_IMAGE}" \
  frontend

echo "Pushing frontend image..."
docker push "${FRONTEND_IMAGE}"

echo "Deploying frontend service..."
gcloud run deploy "${FRONTEND_SERVICE}" \
  --project "${PROJECT_ID}" \
  --region "${REGION}" \
  --platform managed \
  --allow-unauthenticated \
  --image "${FRONTEND_IMAGE}" \
  --port 8080 \
  --memory 512Mi \
  --timeout 300

FRONTEND_URL="$(gcloud run services describe "${FRONTEND_SERVICE}" --project "${PROJECT_ID}" --region "${REGION}" --format='value(status.url)')"

echo ""
echo "=========================================="
echo "Deployment complete"
echo "=========================================="
echo "Backend URL:  ${BACKEND_URL}"
echo "Frontend URL: ${FRONTEND_URL}"
echo ""
echo "Quick checks:"
echo "  curl ${BACKEND_URL}/health"
echo "  curl ${FRONTEND_URL}/health"
