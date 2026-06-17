"""Business rule discovery stage.

Infers deterministic business rule candidates from existing pipeline artifacts
and writes ``business-rules.json``. No repositories are read or cloned and no LLM
calls are made.
"""

from app.business_rules.engine import build_business_rules
from app.business_rules.router import router
from app.business_rules.service import BusinessRulesInputError, BusinessRulesService

__all__ = [
    "build_business_rules",
    "router",
    "BusinessRulesService",
    "BusinessRulesInputError",
]
