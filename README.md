# AI Test Case Generator

## Overview

This project is an intelligent system that automatically generates software test cases from textual requirements. It combines Natural Language Processing (NLP) techniques with a Large Language Model (LLM) to transform unstructured requirement descriptions into structured and executable test cases.

## Motivation

Writing test cases manually is time-consuming and prone to human error. This project aims to assist QA engineers by automating the process of test case generation, improving efficiency and consistency.

## Architecture

The system follows a simple pipeline:

1. Input requirement (title and description)
2. NLP processing using spaCy to extract structured data (actor, actions, objects, conditions)
3. Prompt construction based on extracted data
4. LLM inference using Ollama (Phi / Phi3)
5. JSON test cases generation via FastAPI

## Tech Stack

* Python
* FastAPI
* spaCy
* Ollama (Phi / Phi3)
* Requests

## Project Structure

```
app/
  main_api.py
  nlp_engine.py
  prompt_builder.py
  llm_generator.py
  config.py

requirements.txt
README.md
```

## Installation

1. Clone the repository:

```
git clone <your-repo-link>
cd ai-test-case-generator
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Install spaCy model:

```
python -m spacy download en_core_web_sm
```

4. Run Ollama:

```
ollama serve
```

5. Start the API:

```
uvicorn app.main_api:app --reload
```

## API Usage

### Endpoint

POST /generate-testcases

### Request Example

```
{
  "id": 1,
  "title": "login",
  "description": "The user can login using email and password"
}
```

### Response Example

```
{
  "requirementId": 1,
  "structuredData": {
    "actor": "the user",
    "actions": ["login"],
    "objects": ["email", "password"],
    "conditions": []
    },
  "testCases": {
    "testCases": [
      {
        "type": "positive",
        "title": "Valid login",
        "steps": ["Enter email", "Enter password", "Click login"],
        "expectedResult": "User is logged in successfully"
      }
    ]
  }
}
```

## Future Improvements

* Support multiple requirements in a single request
* Improve NLP extraction accuracy
* Add database integration
* Build a frontend interface (e.g., Flutter)
* Enhance prompt engineering for better LLM output

## License

This project is for educational purposes and graduation project use.
