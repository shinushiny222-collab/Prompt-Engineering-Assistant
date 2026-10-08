import streamlit as st
import os
from google import genai


MODEL = "gemini-2.5-flash-lite"


def generate_response(prompt, temperature=0.4, max_tokens=1200):

    api_key = st.secrets["GEMINI_API_KEY"]

    client = genai.Client(
        api_key=api_key
    )

    response = client.models.generate_content(
        model=MODEL,
        contents=prompt,
        config={
            "temperature": temperature,
            "max_output_tokens": max_tokens
        }
    )

    return response.text
