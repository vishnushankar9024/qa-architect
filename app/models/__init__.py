"""Pydantic data models shared across QA Architect modules."""

from app.models.business_rules import BusinessRule, BusinessRulesModel, DomainBusinessRules
from app.models.common import HealthStatus, Message
from app.models.discovery import (
    AngularInsights,
    DiscoverRequest,
    DiscoveryResult,
    Repository,
    RepositoryFile,
)
from app.models.domain import Domain, DomainModel
from app.models.enriched_business_rules import (
    EnrichedBusinessRule,
    EnrichedBusinessRulesModel,
    QualityReport,
)
from app.models.feature import Feature, FeatureInventory
from app.models.knowledge import KnowledgeEntry
from app.models.traceability import DomainTrace, FeatureTrace, TraceabilityModel
from app.models.qa import TestCase, TestPlan
from app.models.rule_catalog import (
    CatalogRule,
    RuleCatalogModel,
    RuleCatalogSummary,
    RuleOverridesModel,
)

__all__ = [
    "HealthStatus",
    "Message",
    "DiscoverRequest",
    "DiscoveryResult",
    "AngularInsights",
    "Repository",
    "RepositoryFile",
    "Feature",
    "FeatureInventory",
    "Domain",
    "DomainModel",
    "FeatureTrace",
    "DomainTrace",
    "TraceabilityModel",
    "BusinessRule",
    "DomainBusinessRules",
    "BusinessRulesModel",
    "CatalogRule",
    "RuleOverridesModel",
    "RuleCatalogSummary",
    "RuleCatalogModel",
    "EnrichedBusinessRule",
    "EnrichedBusinessRulesModel",
    "QualityReport",
    "KnowledgeEntry",
    "TestCase",
    "TestPlan",
]
