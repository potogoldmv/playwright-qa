from openai import OpenAI
import json
import re

client = OpenAI(api_key="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")


def extract_json(raw: str):
    match = re.search(r"\{.*\}", raw, re.DOTALL)
    return json.loads(match.group())


def generate_form_data():
    prompt = """
    Return ONLY a valid JSON object.

    Output format MUST be exactly:

    {
      "first_name": "string",
      "last_name": "string",
      "job_title": "string",
      "date": "MM/DD/YYYY"
    }
    
    Get creative with the strings you pick. 
    Respect!! the output format.

    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    return extract_json(raw)


def generate_checkbox_data():
    prompt = """
    Return ONLY a valid JSON object.

    Do not include:
    - explanations
    - markdown
    - code blocks
    - extra text

    Output format MUST be exactly:

    {
      "checkbox_1": true,
      "checkbox_2": false,
      "checkbox_3": true
    }

    Rules:
    - values must be random
    - mix true/false realistically
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.choices[0].message.content
    return extract_json(raw)