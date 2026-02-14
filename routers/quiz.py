from fastapi import APIRouter

router = APIRouter(prefix="/quiz", tags=["Quiz"])

@router.get("/generate")
async def generate_quiz():
    return {
        "question": "What is Retrieval-Augmented Generation (RAG)?",
        "options": [
            "A database system",
            "A combination of retrieval and LLM generation",
            "A frontend framework",
            "An operating system"
        ],
        "correct_answer": "A combination of retrieval and LLM generation"
    }