from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import engine, export, knowledge, projects, review

app = FastAPI(title="QA Architect Portal API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(projects.router)
app.include_router(engine.router)
app.include_router(knowledge.router)
app.include_router(review.router)
app.include_router(export.router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
