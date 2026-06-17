from __future__ import annotations

from collections import defaultdict
from pathlib import Path
from typing import Any


class InMemoryStore:
    def __init__(self) -> None:
        self.projects: dict[str, dict[str, Any]] = {}
        self.sources: dict[str, list[dict[str, Any]]] = defaultdict(list)
        self.knowledge_bases: dict[str, dict[str, Any]] = {}
        self.review_log: list[dict[str, Any]] = []
        self.data_dir = Path(__file__).resolve().parents[1] / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def project_path(self, project_id: str) -> Path:
        path = self.data_dir / project_id
        path.mkdir(parents=True, exist_ok=True)
        return path


store = InMemoryStore()
