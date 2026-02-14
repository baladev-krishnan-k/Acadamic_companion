from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/ask", tags=["Q&A"])

class QuestionRequest(BaseModel):
    question: str

@router.post("/")
async def ask_question(request: QuestionRequest):
    return {
        "answer": f"""
        📘 Intelligent Academic Response

        Question: {request.question}

        The system retrieves relevant concepts,
        analyzes the study material,
        and generates structured explanations.

        (Demo Mode Response)
        """
    }