"""Tests for the deterministic repository discovery capability.

These tests build synthetic repositories on disk so they run fully offline
(no network / git clone required).
"""

from __future__ import annotations

import json
from contextlib import contextmanager
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.config import get_settings
from app.discovery import service as discovery_service
from app.discovery.analyzer import analyze_repository
from app.discovery.cloner import CloneError, derive_application_name

client = TestClient(app)


def _write(root: Path, rel: str, content: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    """Redirect the discovery artifact output to a temp directory."""

    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


@pytest.fixture
def node_repo(tmp_path: Path) -> Path:
    """A MEAN-style repo: Angular + React + NodeJS/Express + Mongoose."""

    _write(
        tmp_path,
        "package.json",
        """
        {
          "name": "demo-app",
          "dependencies": {
            "@angular/core": "^17.0.0",
            "react": "^18.0.0",
            "react-dom": "^18.0.0",
            "express": "^4.18.0",
            "mongoose": "^8.0.0"
          }
        }
        """,
    )
    _write(tmp_path, "angular.json", "{}")
    _write(
        tmp_path,
        "src/app/app.module.ts",
        "import { NgModule } from '@angular/core';\n@NgModule({})\nexport class AppModule {}\n",
    )
    _write(
        tmp_path,
        "src/app/users/users.module.ts",
        "@NgModule({})\nexport class UsersModule {}\n",
    )
    _write(
        tmp_path,
        "src/app/app-routing.module.ts",
        """
        import { RouterModule, Routes } from '@angular/router';
        const routes: Routes = [
          { path: '', component: HomeComponent },
          { path: 'users', component: UsersComponent },
          { path: 'admin/dashboard', component: AdminComponent }
        ];
        """,
    )
    _write(
        tmp_path,
        "frontend/App.tsx",
        """
        import { Route } from 'react-router-dom';
        export default function App() {
          return (
            <Routes>
              <Route path="/login" element={<Login />} />
              <Route path="/profile" element={<Profile />} />
            </Routes>
          );
        }
        """,
    )
    _write(
        tmp_path,
        "server/routes/api.js",
        """
        const router = require('express').Router();
        router.get('/api/users', getUsers);
        router.post('/api/users', createUser);
        router.delete('/api/users/:id', deleteUser);
        module.exports = router;
        """,
    )
    _write(
        tmp_path,
        "server/models/user.model.js",
        """
        const mongoose = require('mongoose');
        const User = mongoose.model('User', userSchema);
        const Order = mongoose.model('Order', orderSchema);
        const roles = ['admin', 'editor', 'viewer'];
        """,
    )
    _write(
        tmp_path,
        "src/app/users/users.service.ts",
        "@Injectable()\nexport class UsersService {}\n",
    )
    _write(
        tmp_path,
        "server/controllers/users.controller.ts",
        "@Controller('users')\nexport class UsersController {}\n",
    )
    _write(tmp_path, "tsconfig.json", "{}")
    _write(tmp_path, ".env.example", "PORT=3000\n")
    return tmp_path


@pytest.fixture
def python_repo(tmp_path: Path) -> Path:
    """A Python + FastAPI + PyMongo repo."""

    _write(tmp_path, "requirements.txt", "fastapi\npymongo\nmotor\n")
    _write(tmp_path, "app/__init__.py", "")
    _write(tmp_path, "app/orders/__init__.py", "")
    _write(
        tmp_path,
        "app/api.py",
        """
        from fastapi import APIRouter
        router = APIRouter()

        @router.get('/items')
        def list_items():
            return []

        @router.post('/items')
        def create_item():
            return {}
        """,
    )
    _write(
        tmp_path,
        "app/db.py",
        """
        from pymongo import MongoClient
        client = MongoClient('mongodb://localhost:27017')
        db = client.shop
        users = db.get_collection('users')
        products = db['products']
        """,
    )
    _write(
        tmp_path,
        "app/orders/service.py",
        "class OrderService:\n    def place(self):\n        pass\n",
    )
    _write(
        tmp_path,
        "app/auth.py",
        "ROLES = ['admin', 'customer']\nif role == 'manager':\n    pass\n",
    )
    return tmp_path


def test_node_repo_technology(node_repo: Path) -> None:
    result = analyze_repository(node_repo, "demo-app")
    assert result.application == "demo-app"
    assert result.technology == ["Angular", "React", "NodeJS", "MongoDB"]


def test_node_repo_discovery(node_repo: Path) -> None:
    result = analyze_repository(node_repo, "demo-app")
    assert "app" in result.modules
    assert "users" in result.modules
    assert "/" in result.routes and "users" in result.routes
    assert "/login" in result.routes and "/profile" in result.routes
    assert "GET /api/users" in result.apis
    assert "POST /api/users" in result.apis
    assert "DELETE /api/users/:id" in result.apis
    assert "User" in result.collections and "Order" in result.collections
    assert "users" in result.services or "UsersService" in result.services
    assert {"admin", "editor", "viewer"}.issubset(set(result.roles))
    assert "users" in result.controllers or "UsersController" in result.controllers
    assert "package.json" in result.config_files
    assert "angular.json" in result.config_files
    assert "tsconfig.json" in result.config_files
    assert ".env.example" in result.config_files


def test_python_repo(python_repo: Path) -> None:
    result = analyze_repository(python_repo, "shop")
    assert "Python" in result.technology
    assert "MongoDB" in result.technology
    assert "GET /items" in result.apis
    assert "POST /items" in result.apis
    assert "users" in result.collections
    assert "products" in result.collections
    assert "orders" in result.modules or "app" in result.modules
    assert {"admin", "customer", "manager"}.issubset(set(result.roles))


def test_discover_endpoint(
    monkeypatch: pytest.MonkeyPatch, node_repo: Path, artifact_dir: Path
) -> None:
    @contextmanager
    def fake_clone(repo_url, branch=None, timeout=180):  # noqa: ANN001
        yield node_repo

    monkeypatch.setattr(discovery_service, "clone_repository", fake_clone)

    response = client.post(
        "/discover",
        json={"repo_url": "https://github.com/acme/demo-app"},
    )
    assert response.status_code == 200
    body = response.json()
    assert body["application"] == "demo-app"
    assert set(body.keys()) == {
        "application",
        "technology",
        "modules",
        "routes",
        "controllers",
        "apis",
        "services",
        "collections",
        "roles",
        "config_files",
    }
    assert "Angular" in body["technology"]
    assert "GET /api/users" in body["apis"]

    # The reusable artifact must be written to outputs/application.json.
    artifact = artifact_dir / "application.json"
    assert artifact.is_file()
    saved = json.loads(artifact.read_text())
    assert saved["application"] == "demo-app"
    assert saved == body


def test_application_artifact_roundtrip(
    monkeypatch: pytest.MonkeyPatch, node_repo: Path, artifact_dir: Path
) -> None:
    @contextmanager
    def fake_clone(repo_url, branch=None, timeout=180):  # noqa: ANN001
        yield node_repo

    monkeypatch.setattr(discovery_service, "clone_repository", fake_clone)

    # No artifact yet -> 404.
    assert client.get("/application").status_code == 404

    discover = client.post("/discover", json={"repo_url": "https://github.com/acme/demo-app"})
    assert discover.status_code == 200

    # Future stages consume the saved artifact without re-reading the repo.
    loaded = client.get("/application")
    assert loaded.status_code == 200
    assert loaded.json() == discover.json()


def test_discover_endpoint_clone_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    @contextmanager
    def failing_clone(repo_url, branch=None, timeout=180):  # noqa: ANN001
        raise CloneError("git clone failed: repository not found")
        yield  # pragma: no cover

    monkeypatch.setattr(discovery_service, "clone_repository", failing_clone)

    response = client.post("/discover", json={"repo_url": "https://github.com/x/y"})
    assert response.status_code == 400
    assert "git clone failed" in response.json()["detail"]


def test_derive_application_name() -> None:
    assert derive_application_name("https://github.com/octocat/Hello-World") == "Hello-World"
    assert derive_application_name("https://github.com/acme/demo.git") == "demo"
    assert derive_application_name("git@github.com:acme/demo.git") == "demo"
