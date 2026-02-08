import streamlit as st
import requests
from pages.districts import states,districts
import time
if "token" not in st.session_state:
    st.warning("You cannot access this page. please login first")
    if st.button("Login",type="primary"):
        st.switch_page("pages/login_reg.py")
elif st.session_state.token["token"]==None:
    st.warning("You cannot access this page. please login first")
    if st.button("Login",type="primary"):
        st.switch_page("pages/login_reg.py")
else:
    st.title("Settings")
    st.subheader("Your Personal Details: ")
    user_data=requests.post("http://127.0.0.1:8000/get_user_details", headers={"Authorization": f"Bearer {st.session_state.token["token"]}"})
    user=user_data.json()
    name=st.text_input("Your name: ",value= user["data"].get("name"))
    email=st.text_input("your email: ",value=user["data"].get("email"),disabled=True)
    def_state=user["data"].get("state")
    def_district=user["data"].get("district")
    state=st.selectbox("Your State: ",list(states),index=states.index(def_state))
    i=districts[def_state].index(def_district)
    district=st.selectbox("Choose your District ",list(districts[def_state]),index=5)
    if st.button("Submit",type="primary"):
            with st.status("updating details: "):
                   update_user=requests.put("http://127.0.0.1:8000/update_user_det",headers={"Authorization":f"Bearer {st.session_state.token["token"]}"},
                                 json={
                                     "name":name,
                                     "email":email,
                                     "state":state,
                                     "district":district
                                 })
            if update_user.status_code==200:
                st.session_state.token=""
                token=requests.post("http://127.0.0.1:8000/token",json={
                     "name":name,"email":email,"state":state,"district":district,
                })
                st.session_state.token=token.json()
                st.success("Data succesfully Updated...")
            else:
                 st.error("Details are not updated please try agin some times latter")
    st.divider()
    st.title("Password: ")
    old_password=st.text_input("Enter your old password: ")
    new_password=st.text_input("Enter your new password: ",placeholder="Password must contain atleast 1 uppercase,lowercase,special character and digit")
    confirm_pass=st.text_input("Confirm password: ")
    if st.button("Change Password",type="primary"):
        if new_password==confirm_pass:
            response=requests.put("http://127.0.0.1:8000/update_password",headers={"Authorization": f"Bearer {st.session_state.token["token"]}"},
                               json={
                                    "email":email,
                                    "old_password":old_password,
                                    "new_password":new_password
                               })
            if response.status_code==200:
                ans=response.json()
                if ans.get("password_update")==True:    
                    st.success("Password Succesfully Updated")
                else:
                    st.error("old password is not matched")
        else:
            st.error("password and confirm password missmatch..")
    st.divider()
    col1,col2=st.columns(2)
    c1,c2,c3=col1.columns(3)
    c4,c5=col2.columns(2)
    c2.subheader("Logout")
    if col1.button("logout",type="primary",width="stretch"):
        st.session_state.clear()
        st.switch_page("pages/home.py")
    c4.subheader("Delete Account")
    if col2.button("Delete Account",type="primary",width="stretch"):
        with st.success("Processing..."):
            del_user=requests.delete("http://127.0.0.1:8000/delete_user",headers={"Authorization": f"Bearer {st.session_state.token["token"]}"})
        if del_user.status_code==200:
            ans=del_user.json()
            if ans["delete"]==True:
                st.success("User deleted")
            else:
             st.error("Error please try again some times latter")
        st.session_state.clear()
        st.switch_page("pages/home.py")