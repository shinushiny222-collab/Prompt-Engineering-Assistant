import streamlit as st
from LLM import generate_response
from Prompt_Template import build_prompt


st.set_page_config(
    page_title="LLM Prompt Studio",
    page_icon="AI",
    layout="centered"
)


st.title("LLM Prompt Studio")

st.write(
    "Experiment with different prompting techniques "
    "and generate answers using the Qwen language model."
)


st.header("Prompt Configuration")


technique = st.selectbox(
    "Choose a Prompting Method",
    [
        "Zero-shot",
        "One-shot",
        "Few-shot",
        "CoT",
        "Manual CoT",
        "ToT"
    ]
)


task = st.text_area(
    "Enter your question or task",
    height=150,
    placeholder=(
        "Example: Explain how Artificial Intelligence "
        "is used in healthcare."
    )
)


col1, col2 = st.columns(2)


with col1:
    temperature = st.slider(
        "Response Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.2,
        step=0.1
    )


with col2:
    max_tokens = st.slider(
        "Response Length",
        min_value=500,
        max_value=2000,
        value=1200,
        step=100
    )


if st.button("Generate Answer", use_container_width=True):

    if not task.strip():

        st.warning(
            "Please enter a question or task before generating."
        )

    else:

        try:

            final_prompt = build_prompt(
                technique,
                task
            )


            with st.expander("View Generated Prompt"):

                st.code(
                    final_prompt,
                    language="text"
                )


            with st.spinner(
                "Generating answer using Qwen..."
            ):

                answer = generate_response(
                    final_prompt,
                    temperature=temperature,
                    max_tokens=max_tokens
                )


            st.subheader("Generated Answer")

            st.write(answer)


        except Exception as e:

            st.error(
                f"Unable to generate response: {e}"
            )