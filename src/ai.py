"""AI module for interacting with language models.

This module provides functions to interact with OpenAI's GPT models
through their API.
"""

import os
import json
from openai import OpenAI, APIError


def ask_ai(message):
    """Send a message to OpenAI's API and get a response.

    Args:
        message (str): The user message to send to the API

    Returns:
        str: The AI's response

    Raises:
        ValueError: If no API key is found
        APIError: For OpenAI API specific errors
        ConnectionError: For network-related errors
        RuntimeError: For other unexpected errors
    """
    api_key = os.environ.get("OPENAI_API_KEY")

    if not api_key or api_key == "NO_KEY_FOUND":
        raise ValueError(
            "No OpenAI API key found. Please set the OPENAI_API_KEY environment variable."
        )

    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model="gpt-4",
            input=[
                {
                    "role": "system",
                    "content": "Talk like a news reporter, respond in json format",
                },
                {"role": "user", "content": message},
            ],
            text={
                "format": {
                    "type": "json_object",
                }
            },
        )
        return json.loads(response.output_text)
    except APIError as e:
        # Handle OpenAI-specific errors
        raise RuntimeError(f"OpenAI API error: {str(e)}") from e
    except ConnectionError as e:
        # Handle network-related errors
        raise ConnectionError(f"Network error when calling OpenAI API: {str(e)}") from e
    except Exception as e:
        # Handle any other unexpected errors
        raise RuntimeError(f"Unexpected error when calling OpenAI API: {str(e)}") from e
