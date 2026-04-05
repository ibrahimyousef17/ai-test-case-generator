from fastapi import FastAPI
from pydantic import BaseModel
import json
import re

from nlp_engine import extract_info
from prompt_builder import build_prompt
from llm_generator import generate_test_cases

app = FastAPI()

class Requirement(BaseModel):
    id: int
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
            "error": "Failed to parse JSON from LLM output",
            "raw_output": result
        }

    return {
        "requirementId": req.id,
        "testCases": test_cases
    }