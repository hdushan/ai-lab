import os
import pytest
import unittest.mock as mock
from openai import APIError
from src.ai import ask_ai

@pytest.mark.skipif(
    not os.environ.get('OPENAI_API_KEY'),
    reason="OPENAI_API_KEY environment variable not set"
)
def test_ask_ai_with_api():
    """Test the OpenAI integration with a real API call if API key is available."""
    response = ask_ai('In one word, what is the largest plant in the solar system?')
    assert isinstance(response, dict)
    assert 'jupiter' in str(response.values()).lower()

def test_ask_ai_raises_error_with_no_key():
    """Test that an appropriate error is raised when no API key is provided."""
    # Save the current API key
    original_key = os.environ.get('OPENAI_API_KEY')
    # Temporarily unset the API key
    if 'OPENAI_API_KEY' in os.environ:
        del os.environ['OPENAI_API_KEY']
    # Test that a ValueError is raised
    with pytest.raises(ValueError) as excinfo:
        ask_ai('test message')
    assert "No OpenAI API key found" in str(excinfo.value)
    # Restore the original API key if it existed
    if original_key:
        os.environ['OPENAI_API_KEY'] = original_key

@mock.patch('src.ai.OpenAI')
def test_ask_ai_handles_api_error(mock_openai):
    """Test that APIError is properly handled and re-raised as RuntimeError."""
    # Set up the mock to raise an APIError
    mock_client = mock.MagicMock()
    mock_openai.return_value = mock_client
    mock_completion = mock_client.responses.create
    mock_completion.side_effect = APIError(
        message="API rate limit exceeded",
        request="mock_request",
        body="mock_body",
    )
    # Test that RuntimeError is raised with the appropriate message
    with pytest.raises(RuntimeError) as excinfo:
        ask_ai('test message')
    assert "OpenAI API error" in str(excinfo.value)
    assert "API rate limit exceeded" in str(excinfo.value)

@mock.patch('src.ai.OpenAI')
def test_ask_ai_handles_connection_error(mock_openai):
    """Test that ConnectionError is properly handled and re-raised."""
    # Set up the mock to raise a ConnectionError
    mock_client = mock.MagicMock()
    mock_openai.return_value = mock_client
    mock_completion = mock_client.responses.create
    mock_completion.side_effect = ConnectionError("Failed to establish a connection")
    # Test that ConnectionError is raised with the appropriate message
    with pytest.raises(ConnectionError) as excinfo:
        ask_ai('test message')
    assert "Network error when calling OpenAI API" in str(excinfo.value)
    assert "Failed to establish a connection" in str(excinfo.value)

@mock.patch('src.ai.OpenAI')
def test_ask_ai_handles_generic_exception(mock_openai):
    """Test that other exceptions are properly handled and re-raised as RuntimeError."""
    # Set up the mock to raise a generic Exception
    mock_client = mock.MagicMock()
    mock_openai.return_value = mock_client
    mock_completion = mock_client.responses.create
    mock_completion.side_effect = Exception("Unexpected error occurred")
    # Test that RuntimeError is raised with the appropriate message
    with pytest.raises(RuntimeError) as excinfo:
        ask_ai('test message')
    assert "Unexpected error when calling OpenAI API" in str(excinfo.value)
    assert "Unexpected error occurred" in str(excinfo.value)
