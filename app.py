import streamlit as st

st.set_page_config(page_title="My AI Assistant", layout="centered")
st.title("💬 Hugging Face Assistant")

user_input = st.text_input("Ask me something:")

if user_input:
    st.write("You said:", user_input)
