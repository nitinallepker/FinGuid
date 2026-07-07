from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from ai import process_message

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Financial Goal Navigator Backend Running"}

@app.post("/chat")
def chat(request: ChatRequest):

    result = process_message(
    request.message
    )

    if isinstance(result, dict):
        return result

    return {
        "answer": result,
        "question": ""
    }