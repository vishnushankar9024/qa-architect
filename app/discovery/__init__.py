"""Repository discovery module.

Responsible for locating and scanning repositories so that other modules can
reason about their contents. Implementation is a placeholder for now.
"""

from app.discovery.router import router
from app.discovery.service import DiscoveryService

__all__ = ["router", "DiscoveryService"]
