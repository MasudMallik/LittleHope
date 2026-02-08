import streamlit as st
import requests
st.title("misssing childs")
all_posts=requests.get("http://127.0.0.1:8000/all_posts")
if all_posts.status_code==200:
    data=all_posts.json()
    data=data["result"]
    for i in data:
        st.write(i["child_info"])