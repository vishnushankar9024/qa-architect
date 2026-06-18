from __future__ import annotations

import os
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from pymongo import ASCENDING, MongoClient
from pymongo.errors import PyMongoError


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class InMemoryStore:
    def __init__(self) -> None:
        self.projects: dict[str, dict[str, Any]] = {}
        self.sources: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.knowledge_bases: dict[str, dict[str, Any]] = {}
        self.review_logs: list[dict[str, Any]] = []
        self.app_logs: list[dict[str, Any]] = []
        self.backend_name = "in-memory"
        self.data_dir = Path(__file__).resolve().parents[1] / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def list_projects(self) -> list[dict[str, Any]]:
        return list(self.projects.values())

    def save_project(self, project: dict[str, Any]) -> None:
        self.projects[project["id"]] = project

    def get_project(self, project_id: str) -> dict[str, Any] | None:
        return self.projects.get(project_id)

    def project_exists(self, project_id: str) -> bool:
        return project_id in self.projects

    def set_project_status(self, project_id: str, status: str) -> None:
        project = self.projects.get(project_id)
        if project:
            project["status"] = status

    def list_sources(self, project_id: str) -> list[dict[str, Any]]:
        return list(self.sources[project_id])

    def add_source(self, source: dict[str, Any]) -> None:
        self.sources[source["projectId"]].append(source)

    def set_knowledge_base(self, project_id: str, knowledge_base: dict[str, Any]) -> None:
        self.knowledge_bases[project_id] = knowledge_base

    def get_knowledge_base(self, project_id: str) -> dict[str, Any] | None:
        return self.knowledge_bases.get(project_id)

    def append_review_log(self, entry: dict[str, Any]) -> None:
        self.review_logs.append(entry)

    def log_event(
        self,
        action: str,
        details: dict[str, Any],
        level: str = "INFO",
    ) -> None:
        self.app_logs.append(
            {"timestamp": utc_now().isoformat(), "level": level, "action": action, "details": details}
        )

    def reset_for_tests(self) -> None:
        self.projects.clear()
        self.sources.clear()
        self.knowledge_bases.clear()
        self.review_logs.clear()
        self.app_logs.clear()

    def project_path(self, project_id: str) -> Path:
        path = self.data_dir / project_id
        path.mkdir(parents=True, exist_ok=True)
        return path


class MongoStore:
    def __init__(self, uri: str, db_name: str) -> None:
        self.client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        self.client.admin.command("ping")
        self.db = self.client[db_name]
        self.backend_name = "mongodb"
        self.projects_collection = self.db["projects"]
        self.sources_collection = self.db["knowledge_sources"]
        self.knowledge_collection = self.db["knowledge_bases"]
        self.review_logs_collection = self.db["review_logs"]
        self.app_logs_collection = self.db["app_logs"]
        self.data_dir = Path(__file__).resolve().parents[1] / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self._ensure_indexes()

    def _ensure_indexes(self) -> None:
        self.projects_collection.create_index([("id", ASCENDING)], unique=True)
        self.sources_collection.create_index([("id", ASCENDING)], unique=True)
        self.sources_collection.create_index([("projectId", ASCENDING)])
        self.knowledge_collection.create_index([("projectId", ASCENDING)], unique=True)
        self.review_logs_collection.create_index([("projectId", ASCENDING), ("timestamp", ASCENDING)])
        self.app_logs_collection.create_index([("timestamp", ASCENDING)])

    @staticmethod
    def _without_object_id(document: dict[str, Any] | None) -> dict[str, Any] | None:
        if not document:
            return None
        normalized = dict(document)
        normalized.pop("_id", None)
        return normalized

    def list_projects(self) -> list[dict[str, Any]]:
        documents = self.projects_collection.find({}, {"_id": 0})
        return list(documents)

    def save_project(self, project: dict[str, Any]) -> None:
        self.projects_collection.update_one({"id": project["id"]}, {"$set": project}, upsert=True)

    def get_project(self, project_id: str) -> dict[str, Any] | None:
        document = self.projects_collection.find_one({"id": project_id}, {"_id": 0})
        return self._without_object_id(document)

    def project_exists(self, project_id: str) -> bool:
        return self.projects_collection.count_documents({"id": project_id}, limit=1) == 1

    def set_project_status(self, project_id: str, status: str) -> None:
        self.projects_collection.update_one({"id": project_id}, {"$set": {"status": status}})

    def list_sources(self, project_id: str) -> list[dict[str, Any]]:
        documents = self.sources_collection.find({"projectId": project_id}, {"_id": 0})
        return list(documents)

    def add_source(self, source: dict[str, Any]) -> None:
        self.sources_collection.insert_one(source)

    def set_knowledge_base(self, project_id: str, knowledge_base: dict[str, Any]) -> None:
        self.knowledge_collection.update_one(
            {"projectId": project_id},
            {
                "$set": {
                    "projectId": project_id,
                    "knowledge": knowledge_base,
                    "updatedAt": utc_now(),
                }
            },
            upsert=True,
        )

    def get_knowledge_base(self, project_id: str) -> dict[str, Any] | None:
        document = self.knowledge_collection.find_one({"projectId": project_id}, {"_id": 0})
        if not document:
            return None
        return document["knowledge"]

    def append_review_log(self, entry: dict[str, Any]) -> None:
        self.review_logs_collection.insert_one(entry)

    def log_event(
        self,
        action: str,
        details: dict[str, Any],
        level: str = "INFO",
    ) -> None:
        self.app_logs_collection.insert_one(
            {"timestamp": utc_now(), "level": level, "action": action, "details": details}
        )

    def reset_for_tests(self) -> None:
        self.projects_collection.delete_many({})
        self.sources_collection.delete_many({})
        self.knowledge_collection.delete_many({})
        self.review_logs_collection.delete_many({})
        self.app_logs_collection.delete_many({})

    def project_path(self, project_id: str) -> Path:
        path = self.data_dir / project_id
        path.mkdir(parents=True, exist_ok=True)
        return path


def _build_store() -> InMemoryStore | MongoStore:
    mongo_uri = os.getenv("MONGO_URI")
    if not mongo_uri:
        return InMemoryStore()
    mongo_db = os.getenv("MONGO_DB", "qa_architect_portal")
    try:
        return MongoStore(uri=mongo_uri, db_name=mongo_db)
    except PyMongoError as exc:
        raise RuntimeError(
            "Failed to connect to MongoDB using MONGO_URI. Check secret configuration."
        ) from exc


store = _build_store()
