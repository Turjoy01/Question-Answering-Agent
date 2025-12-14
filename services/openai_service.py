import os
from openai import OpenAI
import httpx

# Initialize client lazily or globally
# Note: In production, consider robust error handling and async client
client = None

def get_client():
    global client
    if client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        client = OpenAI(api_key=api_key)
    return client

async def get_answer_from_openai(question: str) -> str:
    """
    Sends the question to OpenAI and returns the answer.
    Using gpt-3.5-turbo by default.
    """
    try:
        openai_client = get_client()
        
        # Create a chat completion
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful and knowledgeable assistant."},
                {"role": "user", "content": question}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"Error calling OpenAI: {e}")
        return f"Sorry, I encountered an error: {str(e)}"
