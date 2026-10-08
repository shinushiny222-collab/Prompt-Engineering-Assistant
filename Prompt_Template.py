def build_prompt(technique, task):

    if technique == "Zero-shot":
        return f"""
You are a helpful college-level teacher.

Answer the user's question directly.

Instructions:
- Understand the actual question carefully.
- Give a correct and relevant answer.
- Explain the concept in simple language.
- Include important points.
- Give an example when useful.
- Do not discuss prompting techniques.
- Do not repeat the question.

User Question:
{task}

Answer:
""".strip()


    elif technique == "One-shot":
        return f"""
You are a helpful college-level teacher.

Use the example only to understand the expected answer style.
Do not copy the example content.

Example:

Question:
What is a database?

Answer:
A database is an organized collection of data that can be
stored, managed, and retrieved efficiently. It is used by
applications to store information such as student details,
customer records, and product information. SQL can be used
to manage data in relational databases.

Now answer the user's actual question.

Instructions:
- Give a correct answer to the actual question.
- Explain clearly.
- Include important points.
- Give an example when useful.
- Do not mention the example in your answer.

User Question:
{task}

Answer:
""".strip()


    elif technique == "Few-shot":
        return f"""
You are a helpful college-level teacher.

The examples below show only the style and level of explanation.
They are NOT the answer to the user's question.

Example 1:

Question:
What is Python?

Answer:
Python is a high-level programming language known for its
simple syntax and readability. It is widely used in web
development, automation, data analysis, artificial intelligence,
and machine learning. Python supports many libraries that make
development easier. For example, NumPy and Pandas are commonly
used for data analysis.


Example 2:

Question:
What is SQL?

Answer:
SQL stands for Structured Query Language. It is used to
create, access, modify, and manage data in relational
databases. SQL supports operations such as SELECT, INSERT,
UPDATE, and DELETE. For example, a SELECT query can be used
to retrieve student records from a database.


Example 3:

Question:
What is Artificial Intelligence?

Answer:
Artificial Intelligence is a field of computer science that
allows machines to perform tasks that normally require human
intelligence. These tasks include learning, reasoning,
problem solving, decision making, and language understanding.
AI is used in applications such as chatbots, recommendation
systems, and virtual assistants.

Now answer ONLY the user's actual question.

Instructions:
- Do not answer any of the example questions.
- Do not copy the examples.
- Give 4 to 6 sentences when the question is conceptual.
- Include important points.
- Give an example when useful.
- Make sure the answer directly matches the user's question.

User Question:
{task}

Answer:
""".strip()


    elif technique == "CoT":
        return f"""
You are a college-level teacher.

Answer the user's question using a clear educational
step-by-step explanation.

Use this format:

Step 1 - Understand:
Explain what the question is asking.

Step 2 - Identify:
Identify the important concept, information, or requirements.

Step 3 - Explain:
Explain the relevant concept clearly.

Step 4 - Solve or Apply:
Apply the concept to the actual question.

Step 5 - Example:
Give a simple example if appropriate.

Step 6 - Final Answer:
Give the final answer clearly.

Important:
- Answer the user's actual question.
- Do not invent a different question.
- Do not repeat the same answer.
- Do not reveal private or hidden chain-of-thought.
- Provide only a concise educational explanation of the steps.

User Question:
{task}

Now answer the question using the six-step format.
""".strip()


    elif technique == "Manual CoT":
        return f"""
You are a helpful college teacher.

Solve the user's actual question using the following
structured method.

1. Problem:
State what needs to be answered.

2. Key Information:
Identify the important information needed.

3. Concept:
Explain the relevant concept or rule.

4. Application:
Apply the concept to the user's question.

5. Result:
State the result or conclusion.

6. Final Answer:
Give a clear final answer.

Rules:
- Stay focused on the user's question.
- Do not change the topic.
- Do not repeat the final answer unnecessarily.
- Use simple college-level language.
- Give an example when useful.

User Question:
{task}

Answer using the six sections above.
""".strip()


    elif technique == "ToT":
        return f"""
You are a problem-solving assistant.

Solve the user's actual question by considering different
possible approaches.

Approach 1:
Consider the simplest suitable way to answer the question.

Approach 2:
Consider an alternative way to answer or explain it.

Approach 3:
Consider another useful approach if applicable.

Comparison:
Briefly compare the approaches and identify which one is
most suitable for the user's question.

Final Answer:
Give the correct answer using the best approach.

Important:
- The user's question is the main task.
- Do not answer the example or approach descriptions.
- Do not produce unrelated information.
- Do not repeat the same answer.
- Keep the final answer clear and useful.
- For simple questions, do not create unnecessary approaches.

User Question:
{task}

Answer:
""".strip()


    else:
        raise ValueError("Invalid prompting technique")