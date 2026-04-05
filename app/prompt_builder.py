def build_prompt(data):
    return f"""
Act as a QA Engineer. Generate test cases based on these requirements:
Actor: {data['actor']}
Actions: {data['actions']}
Objects: {data['objects']}
Conditions: {data['conditions']}

Output MUST be a valid JSON object following this EXACT schema:
{{
  "testCases": [
    {{
      "type": "positive/negative",
      "title": "short description",
      "steps": ["step 1", "step 2"],
      "expectedResult": "result description"
    }}
  ]
}}
Do not include any explanations, code, or text outside the JSON.
"""