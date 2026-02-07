import streamlit as st
if "token" not in st.session_state:
    st.warning("Please login to upload details..")
    if st.button("login",type="primary"):
        st.switch_page("pages/login_reg.py")
else:
        st.json(st.session_state.token)