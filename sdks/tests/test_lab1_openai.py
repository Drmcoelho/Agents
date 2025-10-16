"""
Tests for Lab 1: OpenAI SDK Basics
"""

import os
import pytest
from unittest.mock import Mock, patch

# Skip tests if no API key
pytestmark = pytest.mark.skipif(
    not os.getenv("OPENAI_API_KEY") or os.getenv("TEST_MODE") == "true",
    reason="OPENAI_API_KEY not set or in test mode"
)


@pytest.fixture
def mock_openai_client():
    """Mock OpenAI client for testing."""
    with patch('sdks.labs.lab1_openai.OpenAI') as mock:
        mock_client = Mock()
        mock.return_value = mock_client
        
        # Mock simple completion
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "This is a test response"
        mock_client.chat.completions.create.return_value = mock_response
        
        yield mock_client


def test_import():
    """Test that the lab module can be imported."""
    from sdks.labs import lab1_openai
    assert lab1_openai is not None


def test_openai_lab_init(mock_openai_client):
    """Test OpenAI lab initialization."""
    from sdks.labs.lab1_openai import OpenAILab
    
    os.environ["OPENAI_API_KEY"] = "test-key"
    lab = OpenAILab()
    assert lab is not None
    assert lab.client is not None


def test_exercise_1_simple_completion():
    """Test exercise 1: simple completion."""
    # This is a placeholder test
    # Students should implement the actual functionality
    assert True


def test_exercise_2_system_prompt():
    """Test exercise 2: system prompt."""
    # This is a placeholder test
    assert True


def test_exercise_3_streaming():
    """Test exercise 3: streaming."""
    # This is a placeholder test
    assert True


def test_exercise_4_temperature_control():
    """Test exercise 4: temperature control."""
    # This is a placeholder test
    assert True
