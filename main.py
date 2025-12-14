from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from services.openai_service import get_answer_from_openai
from models.schemas import QuestionRequest, AnswerResponse
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = FastAPI(
    title="OpenAI QA Agent",
    description="A simple Question Answering Agent using OpenAI API"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    if not os.getenv("OPENAI_API_KEY"):
        print("WARNING: OPENAI_API_KEY is not set in .env file!")

@app.get("/")
async def root():
    return {"message": "OpenAI QA Agent is running. use /ask to ask questions."}

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        answer = await get_answer_from_openai(request.question)
        return AnswerResponse(question=request.question, answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
