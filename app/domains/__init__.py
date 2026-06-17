"""Domain discovery stage.

Groups the feature inventory (``feature-inventory.json``) into business domains
(``domain-model.json``) using a deterministic keyword taxonomy. No repositories
are read or cloned and no LLM calls are made.
"""

from app.domains.grouping import build_domain_model
from app.domains.router import router
from app.domains.service import DomainInputError, DomainService

__all__ = [
    "build_domain_model",
    "router",
    "DomainService",
    "DomainInputError",
]
