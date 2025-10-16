"""Test basic repository structure."""

from pathlib import Path


def test_repository_structure():
    """Test that main directories exist."""
    base = Path(".")
    
    assert (base / "sdks").exists()
    assert (base / "mcp").exists()
    assert (base / "agents").exists()
    assert (base / "agentkit").exists()
    assert (base / "capstones").exists()
    assert (base / "shared").exists()


def test_makefile_exists():
    """Test that Makefile exists."""
    assert Path("Makefile").exists()


def test_env_example_exists():
    """Test that .env.example exists."""
    assert Path(".env.example").exists()


def test_requirements_exist():
    """Test that requirements files exist."""
    assert Path("requirements.txt").exists()
    assert Path("requirements-dev.txt").exists()


def test_devcontainer_exists():
    """Test that devcontainer config exists."""
    assert Path(".devcontainer/devcontainer.json").exists()


def test_shared_utilities_exist():
    """Test that shared utilities exist."""
    shared = Path("shared")
    
    assert (shared / "check_env.py").exists()
    assert (shared / "gabarito.py").exists()
    assert (shared / "evaluator.py").exists()
    assert (shared / "passport.py").exists()
    assert (shared / "deploy.py").exists()
