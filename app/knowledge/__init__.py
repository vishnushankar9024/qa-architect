"""Knowledge module.

Stores and retrieves project knowledge used to inform QA work. Implementation
is a placeholder for now.
"""

from app.knowledge.router import router
from app.knowledge.service import KnowledgeService

__all__ = ["router", "KnowledgeService"]
