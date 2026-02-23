import streamlit as st
from gemini_client import GeminiClient
from memory_manager import *
from prompt_manager import build_prompt

st.set_page_config(page_title="E-Commerce Assistant", layout="wide")

st.title("🛍️ Smart Shopping Assistant")

init_memory()
client = GeminiClient()

for msg in get_history():
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if user_input := st.chat_input("Ask about products, orders, returns..."):
    add_message("user", user_input)

    with st.chat_message("assistant"):
        with st.spinner("🔎 Finding the best deals for you..."):
            prompt = build_prompt(user_input, get_history())
            response = client.generate(prompt)
            st.markdown(response)

    add_message("assistant", response)


with st.sidebar:
    st.header("Store Policies")
    st.write("""
    📦 Free shipping above ₹999  
    🔁 7-day return policy  
    💳 Secure payments  
    """)

