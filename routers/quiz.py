#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import APIRouter
from pydantic import BaseModel
from langchain.chat_models import ChatOpenAI

router = APIRouter(prefix="/quiz", tags=["Quiz"])

class QuizRequest(BaseModel):
    topic: str

@router.post("/generate")
async def generate_quiz(request: QuizRequest):
    llm = ChatOpenAI(temperature=0.3)

    prompt = f"""
    Generate 5 MCQs with answers from topic: {request.topic}
    Provide explanation for each.
    """

    response = llm.predict(prompt)

    return {"quiz": response}

