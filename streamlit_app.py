import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

def generate_code(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

st.title("Code Generator")
st.caption("Por Moris Polanco")

prompt = st.text_input("Enter a prompt:")

if st.button("Generate code"):
    result = generate_code(prompt)
    st.code(result, language='python')
