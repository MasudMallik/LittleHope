import streamlit as st
import requests
from pages.districts import districts,states
if "login" not in st.session_state:
    st.session_state.login = True

def login():
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
                    "https://littlehope.onrender.com/login",
                    json={"email": email, "password": password}
                )
                if response.status_code == 200:
                    result=response.json()
                    if(result.get("login")==False):
                        st.info("you dont have an account please create it")
                    elif "error" in result:
                         st.error("password didnt match")
                    else:
                        token=requests.post("https://littlehope.onrender.com/token",
                                             json={
                                                  "name":result.get("name"),"email":result.get("email"),"state":result.get("state"),"district":result.get("district")
                                             })
                        if token.status_code==200:
                             st.session_state.token=token.json()
                             st.switch_page("pages/report_child.py")
                else:
                    st.error("Login failed ❌")
            else:
                st.warning("Please enter both email and password")

        if col2.button("New user", type="primary", use_container_width=True):
            st.session_state.login=False
            st.rerun()

def registration():
        
        st.title("Registration")
        st.text("Enter your Details properly: ")
        st.divider()
        name=st.text_input(label="Enter your full name: ",placeholder="Abc Def")
        email=st.text_input(label="Enter your email-Id: ",placeholder="email@gmail.com",)
        contact_no=st.text_input(label="Enter your contact number: ",placeholder="123XXXXXXX")
        state=st.selectbox("Choose your state: ",list(states))
        district=st.selectbox("Choose your District ",list(districts[state]))
        password = st.text_input(
            "Enter password",
            placeholder="At least 1 uppercase, 1 lowercase,1 special character, and 1 digit",
            type="password",
        )
        confirm_password = st.text_input(
            "Confirm password",
            placeholder="At least 1 uppercase, 1 lowercase,1 special character, and 1 digit",
            type="password"
        )
        col1, col2 = st.columns(2)

        if col2.button("Already have an account", type="primary", use_container_width=True):
            st.session_state.login=True
            st.rerun()
        if col1.button("Registration", type="primary", use_container_width=True):
                st.session_state.clear()
                response=requests.post("https://littlehope.onrender.com/register",
                json={
                    "name":name,
                    "email":email,
                    "contact_no":contact_no,
                    "state":state,
                    "district":district,
                    "password":password
                })
                st.write(response.status_code)
                if response.status_code == 200:
                    data = response.json()
                    st.session_state.user_details = data

                    if data.get("user_details") == "True":
                        st.info("You already have an account, please login...")
                    else:
                                tok=requests.post("https://littlehope.onrender.com/token",
                                                  json={"name":name,"email":email,"state":state,"district":district})
                                if tok.status_code==200:
                                    token=tok.json()
                                    st.session_state.token=token
                                st.success("Successfully logged in")
                                st.switch_page("pages/report_child.py")
                err=response.json()
                if "detail" in err:
                     for error in err["detail"]:
                          st.write(error["msg"])
             


if st.session_state.login==True:
    login()
else:
    registration()