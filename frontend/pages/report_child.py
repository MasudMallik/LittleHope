import streamlit as st
st.json(st.session_state.user_details)
st.write(st.session_state.user_details["details"])