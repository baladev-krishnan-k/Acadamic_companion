#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import APIRouter
from pydantic import BaseModel
from services.rag_service import vector_store
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

router = APIRouter(prefix="/ask", tags=["Q&A"])

class QuestionRequest(BaseModel):
    question: str

@router.post("/")
async def ask_question(request: QuestionRequest):
    llm = ChatOpenAI(temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 3})
    )

    response = qa_chain.run(request.question)
    return {"answer": response}

