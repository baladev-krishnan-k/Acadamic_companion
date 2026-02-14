from fastapi import FastAPI
from routers import upload, qa, quiz, planner

app = FastAPI(title="Academic Companion - Demo Mode")

app.include_router(upload.router)
app.include_router(qa.router)
app.include_router(quiz.router)
app.include_router(planner.router)

@app.get("/")
def home():
    return {"message": "Academic Companion Backend Running 🚀"}