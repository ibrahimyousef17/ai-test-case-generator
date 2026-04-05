from fastapi import FastAPI
from pydantic import BaseModel
import json
import re
from fastapi.middleware.cors import CORSMiddleware
from app.nlp_engine import extract_info
from app.prompt_builder import build_prompt
from app.llm_generator import generate_test_cases

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Requirement(BaseModel):
    title: str
    description: str

@app.post("/generate-testcases")
def generate(req: Requirement):
    text = req.title + ". " + req.description
    structured_data = extract_info(text)
    prompt = build_prompt(structured_data)
    result = generate_test_cases(prompt)
    print(prompt)
    result = result.strip()
    result = re.sub(r'```json', '', result, flags=re.IGNORECASE)
    result = re.sub(r'```', '', result)
    result = result.strip()

    try:
        test_cases = json.loads(result)
    except json.JSONDecodeError as e:
        test_cases = {
            "error": "Failed to parse JSON from LLM output. plesae try again",
        }

    return {
        "testCases": test_cases
    }