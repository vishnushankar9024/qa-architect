# QA Architect

QA Architect Portal v1 lives in:

- Backend: `backend/` (FastAPI)
- Frontend: `frontend/` (React + TypeScript + Material UI)

## Run backend

1. `cd backend`
2. `pip install -r requirements.txt`
3. Set Mongo env vars for persistent mode:
   - `export MONGO_URI="<your-mongodb-uri>"`
   - `export MONGO_DB="qa_architect_portal"` (optional)
4. `uvicorn app.main:app --reload`

## Run frontend

1. `cd frontend`
2. `npm install`
3. `npm run dev`
