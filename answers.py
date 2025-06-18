import argparse
import base64
import json
import os
import re
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel
import httpx
from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions

# print(os.getenv("OPENAI_API_KEY"))

app = FastAPI()
class QuestionyRequest(BaseModel):
    query: str
    image: str = None

def answer(question: str, image: str = None):
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable is not set.")

@app.post("/api/")
async def api_answer(request: QuestionRequest):
    try:
        return await answer(request.question, request.image)
    except Exception as e:
        return {"error": str(e)}
    


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)