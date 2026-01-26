import streamlit as st
import requests

st.title("Login")

email = st.text_input("Enter email", placeholder="email@gmail.com")
password = st.text_input(
    "Enter password",
    placeholder="At least 1 uppercase, lowercase, special character, and digit",
    type="password"
)

col1, col2 = st.columns(2)

if col1.button("Login", type="primary", use_container_width=True):
    if email and password:
        response = requests.post(
            "http://127.0.0.1:8000/",
            json={"email": email, "password": password}
        )
        if response.status_code == 200:
            st.success(response.json())
        else:
            st.error("Login failed ❌")
    else:
        st.warning("Please enter both email and password")

if col2.button("New user", type="primary", use_container_width=True):
    st.info("Redirecting to registration page...")