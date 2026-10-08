import os
from google import genai

MODEL = "gemini-2.5-flash"


def generate_response(prompt, temperature=0.4, max_tokens=1200):

    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set."
        )

    client = genai.Client(
        api_key=api_key
    )

    system_instruction = """
You are a detailed educational assistant for college students.

Your answers must be explanatory, not short definitions.

IMPORTANT RULES:
- Give a detailed answer.
- Do not give a one-line answer.
- For conceptual questions, write approximately 200 to 350 words.
- Explain the topic using headings and paragraphs.
- Include important points.
- Include a simple example.
- Include applications or uses when relevant.
- If the question asks "explain", give a proper explanation.
- If the question asks "difference", use a comparison.
- If the question asks "steps", explain every step.
- If the question is a programming question, explain the concept,
  code logic, and expected result.
- Avoid repeating the same sentence.
- Answer the user's actual question directly.
"""

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            "system_instruction": system_instruction,
            "temperature": temperature,
            "max_output_tokens": max_tokens
        }
    )

    return response.text