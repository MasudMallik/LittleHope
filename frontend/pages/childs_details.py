import streamlit as st
import requests
st.title("misssing childs")
st.divider()
all_posts=requests.get("https://littlehope.onrender.com/all_posts")
if all_posts.status_code==200:
    data=all_posts.json()
    data=data["result"]
    for i in data:
        for j in range(len(data[i])):
            st.subheader(f"Posted by: {i}")
            st.write(f"Posted on: {data[i][j]['other']['date_and_time']}")
            col1,col2,col3=st.columns(3)
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.write(" ")
            col1.image(data[i][j]["other"].get("img_path"),caption=f"Name: {data[i][j]['child_info']['name']}")
            col2.subheader("Childs Details: ")
            col2.table(data[i][j]["child_info"])
            col3.subheader("parent details")
            col3.table(data[i][j]["parent_info"])
            st.divider()