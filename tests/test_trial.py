import os
import pytest
from src.ai import ask_ai
@pytest.mark.skipif(
    not os.environ.get('OPENAI_API_KEY'),
    reason="OPENAI_API_KEY environment variable not set"
)
def test_ask_ai_with_api():
    """Test the OpenAI integration with a real API call if API key is available."""
    response = ask_ai('which country am I in')
    assert isinstance(response, str)
    assert len(response) > 0


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
    if original_key:
        os.environ['OPENAI_API_KEY'] = original_key
