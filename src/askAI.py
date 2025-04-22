import os
from openai import OpenAI

def askAI(message):
    api_key = os.environ.get('OPENAI_API_KEY')
    
    if not api_key or api_key == 'NO_KEY_FOUND':
        raise ValueError("No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
    
    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model='gpt-4',
            input=[
                {
                    'role': 'system',
                    'content': 'Talk like a news reporter'
                },
                {
                    'role': 'user',
                    'content': message
                }
            ]
        )
        return response.output_text
    except Exception as e:
        raise Exception(f"Error calling OpenAI API: {str(e)}")
