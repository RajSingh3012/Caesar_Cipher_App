import streamlit as st
from logo import logo
from main import caesar
st.text(logo)
st.title("Welcome to Caesar Cipher")
direction = st.selectbox("Type 'encode' to encrypt, type 'decode' to decrypt", ["encode", "decode"])
text = st.text_input("Type your message")
shift = st.number_input("Type the shift number", min_value=1, step=1)
run_cipher = st.button("Cipher It")
if run_cipher:
    result = caesar(text.lower(), shift, direction.lower())
    st.write(f"Results: {result}")