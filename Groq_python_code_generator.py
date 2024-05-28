from groq import Groq
import streamlit as st

GROQ_API_KEY = "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"

client = Groq(
    api_key = GROQ_API_KEY,
)

system_prompt = f""" 
Generate python code only based on given instruction, don't generate anything else.
"""
query = st.text_input("Input here", placeholder = "Ask me!")

if query:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": system_prompt,
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model="gemma-7b-it",
    )

    response = chat_completion.choices[0].message.content

    st.markdown(":blue[Query:]")
    st.markdown(query)
    st.markdown(":green[Response: ]")
    st.markdown(response)