# LLM Prompt Engineering Assistant

A Streamlit-based Prompt Engineering application that demonstrates different prompting techniques using a Large Language Model (LLM).

The application allows users to enter a task, select a prompting technique, generate the corresponding prompt, and receive an AI-generated response.

## Project Overview

This project demonstrates how different prompt engineering techniques can influence the way an LLM generates responses.

The application supports:

- Zero-shot Prompting
- One-shot Prompting
- Few-shot Prompting
- Chain of Thought (CoT)
- Manual Chain of Thought
- Tree of Thought (ToT)

The application uses Google Gemini as the LLM and Streamlit for the user interface.

## Demo
https://prompt-engineering-assistant-e34ce5bpcgnygsh25fwvcd.streamlit.app/

## Features

### 1. Zero-shot Prompting

The model receives a task without any examples and generates an answer directly.

### 2. One-shot Prompting

The model receives one example before answering the user's task.

### 3. Few-shot Prompting

The model receives multiple examples to understand the expected response style before answering the user's task.

### 4. Chain of Thought

The model is guided to provide a structured educational explanation through multiple steps without exposing private internal reasoning.

### 5. Manual Chain of Thought

The prompt explicitly provides a predefined reasoning structure such as:

1. Understand the question
2. Identify the information
3. Explain the concept
4. Apply the concept
5. Verify the result
6. Give the final answer

### 6. Tree of Thought

The model is guided to consider multiple possible approaches, compare them, and select the most suitable approach.

## Technologies Used

- Python
- Streamlit
- Google Gemini API
- Google GenAI SDK
- Prompt Engineering
- Large Language Models (LLMs)

## Project Structure

```text
LLM-Prompt-Engineering/
│
├── app.py
├── llm.py
├── prompt_templates.py
├── requirements.txt
├── README.md
└── .gitignore
