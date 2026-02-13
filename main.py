#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from routers import upload, qa, quiz, planner

app = FastAPI(title="AI Study Companion Backend")

app.include_router(upload.router)
app.include_router(qa.router)
app.include_router(quiz.router)
app.include_router(planner.router)

@app.get("/")
def home():
    return {"message": "AI Study Companion API Running 🚀"}

