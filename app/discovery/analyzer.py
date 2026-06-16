"""Deterministic repository analysis (no AI).

Walks a cloned repository and extracts:

* ``technology`` — Angular, React, NodeJS, Python, MongoDB.
* ``modules``     — Angular/Nest modules and Python packages.
* ``routes``      — frontend routes (Angular Router / React Router).
* ``apis``        — backend HTTP endpoints (Express / FastAPI / Flask).
* ``collections`` — MongoDB collections/models (Mongoose / mongoengine / PyMongo).
* ``roles``       — best-effort role identifiers.

All detection is regex/structure based and fully deterministic.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from app.models.discovery import DiscoveryResult

# Directories that never contain first-party source worth scanning.
IGNORED_DIRS = {
    ".git",
    "node_modules",
    "dist",
    "build",
    "out",
    "coverage",
    "target",
    ".next",
    ".nuxt",
    ".angular",
    ".venv",
    "venv",
    "env",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".idea",
    ".vscode",
    "vendor",
}

# Extensions whose text content we read for pattern scanning.
TEXT_EXTENSIONS = {
    ".ts",
    ".tsx",
    ".js",
    ".jsx",
    ".mjs",
    ".cjs",
    ".py",
    ".json",
    ".yml",
    ".yaml",
    ".toml",
    ".cfg",
    ".ini",
    ".txt",
    ".html",
    ".env",
}
TEXT_FILENAMES = {".env", "Pipfile", "Dockerfile"}

MAX_FILE_BYTES = 2_000_000

HTTP_METHODS = ("get", "post", "put", "delete", "patch", "options", "head")

# --- Regexes ---------------------------------------------------------------

_EXPRESS_API = re.compile(
    r"\b(?:app|router|api)\s*\.\s*(" + "|".join(HTTP_METHODS) + r")\s*\(\s*['\"]([^'\"]+)['\"]",
    re.IGNORECASE,
)
_FASTAPI_API = re.compile(
    r"@\s*(?:app|router|api)\s*\.\s*(" + "|".join(HTTP_METHODS) + r")\s*\(\s*['\"]([^'\"]+)['\"]",
    re.IGNORECASE,
)
_FLASK_ROUTE = re.compile(
    r"@\s*(?:app|bp|blueprint|\w+)\s*\.\s*route\s*\(\s*['\"]([^'\"]+)['\"]([^)]*)\)",
)
_FLASK_METHODS = re.compile(r"methods\s*=\s*\[([^\]]*)\]")

_ANGULAR_PATH = re.compile(r"\bpath\s*:\s*['\"]([^'\"]*)['\"]")
_REACT_ROUTE = re.compile(r"<Route\b[^>]*\bpath\s*=\s*['\"]([^'\"]+)['\"]")

_MONGOOSE_MODEL = re.compile(r"\.model\s*\(\s*['\"]([A-Za-z_][\w-]*)['\"]")
_MONGOENGINE_DOC = re.compile(
    r"class\s+(\w+)\s*\(\s*[^)]*\b(?:Dynamic)?(?:Document|EmbeddedDocument)\b[^)]*\)"
)
_PYMONGO_GETCOLL = re.compile(
    r"(?:get_collection|create_collection)\s*\(\s*['\"]([^'\"]+)['\"]"
)
_PYMONGO_INDEX = re.compile(r"\bdb\s*\[\s*['\"]([^'\"]+)['\"]\s*\]")
_PYMONGO_ATTR = re.compile(r"\bdb\s*\.\s*([A-Za-z_]\w*)\b")
_MONGO_ATTR_DENYLIST = {
    "command",
    "drop",
    "drop_collection",
    "create_collection",
    "get_collection",
    "list_collection_names",
    "list_collections",
    "collection_names",
    "client",
    "name",
    "database",
    "admin",
    "with_options",
    "validate_collection",
    "dereference",
}

_NEST_SERVICE_CLASS = re.compile(r"class\s+(\w+Service)\b")
_PY_SERVICE_CLASS = re.compile(r"class\s+(\w+Service)\b")

_CONTROLLER_CLASS = re.compile(r"class\s+(\w+Controller)\b")
_ANGULARJS_CONTROLLER = re.compile(r"\.controller\s*\(\s*['\"]([^'\"]+)['\"]")

_NEST_ROLES = re.compile(r"@Roles\s*\(([^)]*)\)")
_ROLES_ASSIGN = re.compile(r"\broles?\b\s*[:=]\s*\[([^\]]*)\]", re.IGNORECASE)
_ROLE_ENUM = re.compile(r"enum\s+\w*Roles?\w*\s*\{([^}]*)\}", re.IGNORECASE)
_ROLE_COMPARE = re.compile(
    r"\brole\b\s*={2,3}\s*['\"]([^'\"]+)['\"]", re.IGNORECASE
)
_HAS_ROLE = re.compile(r"hasRole\s*\(\s*['\"]([^'\"]+)['\"]")
_QUOTED = re.compile(r"['\"]([^'\"]+)['\"]")

# Configuration files recognised by exact name.
_CONFIG_FILENAMES = {
    "package.json",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
    "angular.json",
    "nx.json",
    "nest-cli.json",
    "requirements.txt",
    "pyproject.toml",
    "setup.py",
    "setup.cfg",
    "Pipfile",
    "Pipfile.lock",
    "poetry.lock",
    "manage.py",
    "alembic.ini",
    "pytest.ini",
    "tox.ini",
    "mypy.ini",
    "Dockerfile",
    "docker-compose.yml",
    "docker-compose.yaml",
    "Makefile",
    "Procfile",
}

# Configuration files recognised by filename prefix.
_CONFIG_PREFIXES = (
    "tsconfig",
    ".env",
    "requirements",
    ".eslintrc",
    ".prettierrc",
    ".babelrc",
    "babel.config",
    "jest.config",
    "vite.config",
    "vitest.config",
    "webpack.config",
    "rollup.config",
    "next.config",
    "nuxt.config",
    "karma.conf",
    "cypress.config",
    "playwright.config",
    "environment.",
)


def _iter_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel_parts = path.relative_to(root).parts
        if any(part in IGNORED_DIRS for part in rel_parts):
            continue
        files.append(path)
    return files


def _read(path: Path) -> str:
    try:
        if path.stat().st_size > MAX_FILE_BYTES:
            return ""
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def _is_text(path: Path) -> bool:
    return path.suffix in TEXT_EXTENSIONS or path.name in TEXT_FILENAMES


def _sorted_unique(values: object) -> list[str]:
    return sorted({v for v in values if v})


class _Index:
    """Pre-read view of a repository used by the detectors."""

    def __init__(self, root: Path) -> None:
        self.root = root
        self.files = _iter_files(root)
        self.contents: dict[Path, str] = {}
        self.package_jsons: list[dict] = []
        self.node_deps: dict[str, str] = {}
        self.python_dep_text = ""

        py_dep_chunks: list[str] = []
        for path in self.files:
            name = path.name
            if name == "package.json":
                try:
                    pkg = json.loads(_read(path))
                except (json.JSONDecodeError, ValueError):
                    pkg = None
                if isinstance(pkg, dict):
                    self.package_jsons.append(pkg)
                    for key in (
                        "dependencies",
                        "devDependencies",
                        "peerDependencies",
                        "optionalDependencies",
                    ):
                        deps = pkg.get(key)
                        if isinstance(deps, dict):
                            self.node_deps.update(deps)
            if (
                name.startswith("requirements")
                and name.endswith(".txt")
                or name in {"pyproject.toml", "setup.py", "setup.cfg", "Pipfile"}
            ):
                py_dep_chunks.append(_read(path))
            if _is_text(path):
                self.contents[path] = _read(path)

        self.python_dep_text = "\n".join(py_dep_chunks).lower()

    def code_items(self, *suffixes: str):
        for path, text in self.contents.items():
            if not suffixes or path.suffix in suffixes:
                yield path, text


def _detect_technology(index: _Index) -> list[str]:
    techs: list[str] = []

    names = {p.name for p in index.files}
    suffixes = {p.suffix for p in index.files}
    deps = {d.lower() for d in index.node_deps}

    has_angular = "angular.json" in names or any(d.startswith("@angular/") for d in deps)
    has_react = "react" in deps or "react-dom" in deps or "next" in deps
    has_node = bool(index.package_jsons)
    has_python = (
        ".py" in suffixes
        or bool(index.python_dep_text.strip())
        or {"pyproject.toml", "setup.py", "Pipfile"} & names
    )

    mongo_node = any(d in deps for d in ("mongoose", "mongodb", "@nestjs/mongoose"))
    mongo_python = any(
        lib in index.python_dep_text for lib in ("pymongo", "motor", "mongoengine")
    )
    mongo_conn = any(
        "mongodb://" in text or "mongodb+srv://" in text
        for text in index.contents.values()
    )
    has_mongo = mongo_node or mongo_python or mongo_conn

    # Fixed, deterministic ordering.
    if has_angular:
        techs.append("Angular")
    if has_react:
        techs.append("React")
    if has_node:
        techs.append("NodeJS")
    if has_python:
        techs.append("Python")
    if has_mongo:
        techs.append("MongoDB")
    return techs


def _detect_modules(index: _Index) -> list[str]:
    modules: set[str] = set()

    for path, _text in index.code_items(".ts"):
        if path.name.endswith(".module.ts"):
            modules.add(path.name[: -len(".module.ts")])

    # Python packages: directories containing __init__.py.
    for path in index.files:
        if path.name == "__init__.py":
            modules.add(path.parent.name)

    return _sorted_unique(modules)


def _detect_routes(index: _Index) -> list[str]:
    routes: set[str] = set()

    for path, text in index.code_items(".ts"):
        if "RouterModule" in text or "Routes" in text or "rout" in path.name.lower():
            for match in _ANGULAR_PATH.findall(text):
                routes.add(match if match != "" else "/")

    for path, text in index.code_items(".tsx", ".jsx", ".js", ".ts"):
        for match in _REACT_ROUTE.findall(text):
            routes.add(match)

    return _sorted_unique(routes)


def _detect_apis(index: _Index) -> list[str]:
    apis: set[str] = set()

    for _path, text in index.code_items(".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"):
        for method, route in _EXPRESS_API.findall(text):
            apis.add(f"{method.upper()} {route}")

    for _path, text in index.code_items(".py"):
        for method, route in _FASTAPI_API.findall(text):
            apis.add(f"{method.upper()} {route}")
        for route, tail in _FLASK_ROUTE.findall(text):
            methods_match = _FLASK_METHODS.search(tail)
            if methods_match:
                methods = _QUOTED.findall(methods_match.group(1))
                for method in methods or ["GET"]:
                    apis.add(f"{method.upper()} {route}")
            else:
                apis.add(f"GET {route}")

    return _sorted_unique(apis)


def _detect_services(index: _Index) -> list[str]:
    services: set[str] = set()

    for path, text in index.code_items(".ts"):
        if path.name.endswith(".service.ts"):
            services.add(path.name[: -len(".service.ts")])
        for match in _NEST_SERVICE_CLASS.findall(text):
            services.add(match)

    for _path, text in index.code_items(".py"):
        for match in _PY_SERVICE_CLASS.findall(text):
            services.add(match)

    return _sorted_unique(services)


def _detect_controllers(index: _Index) -> list[str]:
    controllers: set[str] = set()

    for path, text in index.code_items(".ts"):
        if path.name.endswith(".controller.ts"):
            controllers.add(path.name[: -len(".controller.ts")])
        for match in _CONTROLLER_CLASS.findall(text):
            controllers.add(match)

    for _path, text in index.code_items(".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"):
        if ".controller(" in text:
            for match in _ANGULARJS_CONTROLLER.findall(text):
                controllers.add(match)

    for _path, text in index.code_items(".py"):
        for match in _CONTROLLER_CLASS.findall(text):
            controllers.add(match)

    return _sorted_unique(controllers)


def _detect_config_files(index: _Index) -> list[str]:
    config_files: set[str] = set()

    for path in index.files:
        name = path.name
        if name in _CONFIG_FILENAMES or name.startswith(_CONFIG_PREFIXES):
            config_files.add(path.relative_to(index.root).as_posix())

    return _sorted_unique(config_files)


def _detect_collections(index: _Index) -> list[str]:
    collections: set[str] = set()

    for _path, text in index.code_items(".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs"):
        if "mongoose" in text or "@nestjs/mongoose" in text:
            for match in _MONGOOSE_MODEL.findall(text):
                collections.add(match)

    for _path, text in index.code_items(".py"):
        for match in _MONGOENGINE_DOC.findall(text):
            collections.add(match)
        for match in _PYMONGO_GETCOLL.findall(text):
            collections.add(match)
        for match in _PYMONGO_INDEX.findall(text):
            collections.add(match)
        if "pymongo" in text or "motor" in text or "MongoClient" in text:
            for match in _PYMONGO_ATTR.findall(text):
                if match not in _MONGO_ATTR_DENYLIST and not match.startswith("_"):
                    collections.add(match)

    return _sorted_unique(collections)


def _detect_roles(index: _Index) -> list[str]:
    roles: set[str] = set()

    for _path, text in index.contents.items():
        for match in _NEST_ROLES.findall(text):
            roles.update(_QUOTED.findall(match))
            # also bare enum-style identifiers e.g. Role.Admin
            for ident in re.findall(r"\b\w+\.(\w+)\b", match):
                roles.add(ident)
        for block in _ROLES_ASSIGN.findall(text):
            roles.update(_QUOTED.findall(block))
        for block in _ROLE_ENUM.findall(text):
            for member in re.findall(r"\b([A-Za-z_]\w*)\b", block):
                roles.add(member)
        roles.update(_ROLE_COMPARE.findall(text))
        roles.update(_HAS_ROLE.findall(text))

    # Drop obviously non-role tokens that can leak from enum bodies.
    cleaned = {r.strip() for r in roles if r.strip() and len(r.strip()) <= 40}
    return _sorted_unique(cleaned)


def analyze_repository(root: Path, application: str) -> DiscoveryResult:
    """Analyze the repository rooted at ``root`` and return a discovery result."""

    index = _Index(Path(root))
    return DiscoveryResult(
        application=application,
        technology=_detect_technology(index),
        modules=_detect_modules(index),
        routes=_detect_routes(index),
        controllers=_detect_controllers(index),
        apis=_detect_apis(index),
        services=_detect_services(index),
        collections=_detect_collections(index),
        roles=_detect_roles(index),
        config_files=_detect_config_files(index),
    )
