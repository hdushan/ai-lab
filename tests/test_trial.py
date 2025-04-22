import pytest
import os
from src.askAI import askAI

@pytest.mark.skipif(
    not os.environ.get('OPENAI_API_KEY'),
    reason="OPENAI_API_KEY environment variable not set"
)

def test_askAI_with_api():
    """Test the OpenAI integration with a real API call if API key is available"""
    response = askAI('In one word, which is the largest planet?')
    assert isinstance(response, str)
    assert len(response) > 0
    assert 'jupiter' in response.lower()

def test_askAI_raises_error_with_no_key():
    """Test that an appropriate error is raised when no API key is provided"""
    # Save the current API key
    original_key = os.environ.get('OPENAI_API_KEY')
    
    # Temporarily unset the API key
    if 'OPENAI_API_KEY' in os.environ:
        del os.environ['OPENAI_API_KEY']
    
    # Test that a ValueError is raised
    with pytest.raises(ValueError) as excinfo:
        askAI('test message')
    assert "No OpenAI API key found" in str(excinfo.value)
    
    # Restore the original API key if it existed
    if original_key:
        os.environ['OPENAI_API_KEY'] = original_key
