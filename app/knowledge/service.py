"""Knowledge service (placeholder)."""

from __future__ import annotations

from app.models.knowledge import KnowledgeEntry


class KnowledgeService:
    """Manages stored project knowledge.

    This is a scaffold. Persistence and retrieval will be implemented later.
    """

    def list_entries(self) -> list[KnowledgeEntry]:
        """Return stored knowledge entries.

        Currently returns an empty list as a placeholder.
        """

        return []
