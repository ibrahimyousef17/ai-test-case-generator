import requests
from config import MODEL_NAME, OLLAMA_URL
from prompt_builder import build_prompt
from nlp_engine import extract_info
def generate_test_cases(prompt):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
                "format": "json"
            }
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except requests.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
    except Exception as e:
        return {"error": f"Unknown error: {str(e)}"}
    

# testing 
text = ' the user can login using email and password'
text = extract_info(text)
prompt = build_prompt(text)
print(prompt)
# print(generate_test_cases(prompt))