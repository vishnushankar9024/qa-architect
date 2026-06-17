"""QA Architect entrypoint.

Run the development server with:

    uvicorn main:app --reload

or simply:

    python main.py
"""

from __future__ import annotations

import uvicorn

from app.api import app
from app.config import get_settings

__all__ = ["app"]


def main() -> None:
    """Start the development server."""

    settings = get_settings()
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )


if __name__ == "__main__":
    main()
