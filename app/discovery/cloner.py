"""Utilities for cloning a GitHub repository for analysis."""

from __future__ import annotations

import re
import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from collections.abc import Iterator
from pathlib import Path
from urllib.parse import urlparse, urlunparse

from app.config import get_settings

# Accept https(s)/git URLs and the ``git@host:owner/repo`` SSH shorthand.
_SSH_SHORTHAND = re.compile(r"^[\w.-]+@[\w.-]+:[\w./-]+$")


class CloneError(RuntimeError):
    """Raised when a repository cannot be cloned."""


def normalize_repo_url(repo_url: str) -> str:
    """Validate and lightly normalize a repository URL.

    Raises ``CloneError`` if the URL is obviously not a cloneable git URL.
    """

    url = (repo_url or "").strip()
    if not url:
        raise CloneError("Repository URL must not be empty.")

    if _SSH_SHORTHAND.match(url):
        return url

    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https", "git"} or not parsed.netloc:
        raise CloneError(
            "Repository URL must be an http(s)/git URL or a git@host:owner/repo SSH URL."
        )
    return url


def derive_application_name(repo_url: str) -> str:
    """Derive a human-friendly application name from a repository URL."""

    url = (repo_url or "").strip()
    if _SSH_SHORTHAND.match(url):
        tail = url.split(":", 1)[1]
    else:
        tail = urlparse(url).path
    name = tail.rstrip("/").split("/")[-1] if tail else ""
    if name.endswith(".git"):
        name = name[: -len(".git")]
    return name


def _authenticated_url(url: str) -> str:
    """Inject a configured GitHub token for https github.com URLs, if present."""

    settings = get_settings()
    token = settings.github_token
    if not token:
        return url

    parsed = urlparse(url)
    if parsed.scheme != "https" or "github.com" not in parsed.netloc:
        return url
    if "@" in parsed.netloc:  # credentials already present
        return url

    netloc = f"x-access-token:{token}@{parsed.netloc}"
    return urlunparse(parsed._replace(netloc=netloc))


@contextmanager
def clone_repository(
    repo_url: str,
    branch: str | None = None,
    timeout: int = 180,
) -> Iterator[Path]:
    """Clone ``repo_url`` into a temporary directory.

    Yields the path to the cloned working tree and removes it on exit. A shallow
    clone (``--depth 1``) is used to keep things fast.
    """

    url = normalize_repo_url(repo_url)
    tmp_dir = Path(tempfile.mkdtemp(prefix="qa-architect-"))
    target = tmp_dir / "repo"

    cmd = ["git", "clone", "--depth", "1", "--single-branch"]
    if branch:
        cmd += ["--branch", branch]
    cmd += [_authenticated_url(url), str(target)]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=False,
        )
        if result.returncode != 0:
            # Avoid leaking a token that may be embedded in the URL.
            stderr = (result.stderr or "").replace(_authenticated_url(url), url)
            raise CloneError(f"git clone failed: {stderr.strip() or 'unknown error'}")
        yield target
    except subprocess.TimeoutExpired as exc:  # pragma: no cover - timing dependent
        raise CloneError(f"git clone timed out after {timeout}s.") from exc
    except FileNotFoundError as exc:  # pragma: no cover - git missing
        raise CloneError("git executable not found on PATH.") from exc
    finally:
        shutil.rmtree(tmp_dir, ignore_errors=True)
