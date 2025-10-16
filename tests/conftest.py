"""Test utilities and fixtures."""

import os
import pytest


@pytest.fixture
def mock_env():
    """Mock environment variables for testing."""
    old_env = os.environ.copy()
    
    # Set test environment variables
    os.environ["TEST_MODE"] = "true"
    os.environ["DEFAULT_BACKEND"] = "openai"
    os.environ["OPENAI_API_KEY"] = "test-key"
    
    yield
    
    # Restore original environment
    os.environ.clear()
    os.environ.update(old_env)
