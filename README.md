# OpenAI Question Answering Agent

A simple, powerful Question Answering Agent built with FastAPI and OpenAI's GPT models.

## Features
- **FastAPI**: High-performance web framework.
- **OpenAI Integration**: Uses GPT-3.5-turbo (or configured model) to answer questions.
- **Swagger UI**: Interactive API documentation.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    Ensure you have a `.env` file in this directory with your OpenAI API key:
    ```
    OPENAI_API_KEY=sk-...
    ```

## Running the Agent

Start the server using `uvicorn`:

```bash
uvicorn main:app --reload
```

## Usage

1.  **API Documentation**:
    Open [http://localhost:8000/docs](http://localhost:8000/docs) in your browser.

2.  **Ask a Question**:
    Use the `/ask` endpoint "Try it out" button or `curl`:

    ```bash
    curl -X 'POST' \
      'http://localhost:8000/ask' \
      -H 'accept: application/json' \
      -H 'Content-Type: application/json' \
      -d '{
      "question": "What is the capital of France?"
    }'
    ```
    <img width="961" height="947" alt="image" src="https://github.com/user-attachments/assets/a7a6d1de-0323-4f79-ad16-eb3c4e7bd3bd" />
