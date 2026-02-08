import streamlit as st
import datetime
import requests
from dotenv import load_dotenv
import os
from supabase import create_client,client
load_dotenv()
supabase :client =create_client(os.getenv("supabase_url"),os.getenv("supabase_anomkey"))
if "token" not in st.session_state:
    st.warning("Please login to upload details..")
    if st.button("login",type="primary"):
        st.switch_page("pages/login_reg.py")
else:
        child={
             "name":"",
             "nick_name":"",
             "gender":"",
             "dob":"",
             "height":"",
             "weight":"",
             "skin_tone":"",
             "birth_marks":"",
             "tattos":"",
             "disable":"",
             "date_of_missing":"",
             "time_of_missing":"",
             "last_seen_loc":"",
        }
        parent={
              "name":"",
              "relation":"",
              "contact":"",
              "alternate_no":"",
              "email":"",
              "address":"",
        }
        other={
                 "date_and_time":"",
                 "img_path":"",
                 "file_path":""
        }
        st.title("Upload Missing Child Case....")
        st.divider()

        st.subheader("Child Personal Details")
        name=st.text_input("Enter Full Name: ")
        nick_name=st.text_input("Enter Nick name: ",placeholder="Optional")
        gender=st.radio("Gender: ",options=["male","female","others"])
        dob=st.date_input("Date-Of-Birth: ",max_value="today",min_value=datetime.date(1950,1,1),)
        height=st.number_input("Enter the Height(in foot): ")
        weight=st.number_input("Enter the weight(in kg ):")
        skin_tone=st.text_input("Skin tone / complexion ")
        st.divider()

        st.subheader("Physical Identification Marks")
        Birthmarks=st.text_input("Birthmarks if any: ",placeholder="optional")
        Tattoos=st.text_input("Tattoos: ",placeholder="optional")
        disable=st.radio("Disability / medical condition",options=["yes","no"])
        st.divider()

        st.subheader("Last Seen Information")
        date_of_missing=st.date_input("Date child went missing: ",max_value="today",min_value=datetime.date(1950,1,1),)
        time_of_missing=st.time_input("Time child went missing",value=datetime.time(12,00))
        Last_seen_location=st.text_input("Last seen location: ")
        st.divider()

        st.subheader("Upload Image: ")
        img_path=st.file_uploader("Upload Image: ",type=["jpg","png","jpeg"])
        st.divider()
      
        st.subheader("Reporter / Parent / Guardian Details")
        Reporter_name=st.text_input("Enter Reporter Name: ")
        Relationship_with_child=st.text_input("Enter RelationShip With Child: ")
        Contact_number=st.text_input("Enter Contact Number: ")
        Alternate_contact_number=st.text_input("Alternate contact number: ")
        Email_address=st.text_input("Email: ",placeholder="example@gmail.com")
        Address=st.text_area("Enter yor Address with Po and Ps: ",height=20,)

        condition1=st.checkbox("I confirm that information provided is true")
        condition2=st.checkbox("Consent to display details publicly")
        condition3=st.checkbox("Privacy agreement")
        status=not(condition1 and condition2 and condition3 and img_path)
        if st.button("Submit",type="primary",disabled=status):
                    child["name"]=name
                    child["nick_name"]=nick_name
                    child["gender"]=gender
                    child["dob"]=str(dob)
                    child["height"]=height
                    child["weight"]=weight
                    child["skin_tone"]=skin_tone
                    child["birth_marks"]=Birthmarks
                    child["tattos"]=Tattoos
                    child["disable"]=disable
                    child["date_of_missing"]=str(date_of_missing)
                    child["time_of_missing"]=str(time_of_missing)
                    child["last_seen_loc"]=Last_seen_location
                    parent["name"]=Reporter_name
                    parent["relation"]=Relationship_with_child
                    parent["contact"]=Contact_number
                    parent["alternate_no"]=Alternate_contact_number
                    parent["email"]=Email_address
                    parent["address"]=Address
                    other["date_and_time"]=str(datetime.datetime.now())
                    files = supabase.storage.from_(os.getenv("bucket")).list()
                    if img_path is not None:
                        file_path = f"images/{img_path.name}.{len(files)}"
                        file_bytes = img_path.read()
                        res = supabase.storage.from_(os.getenv("bucket")).upload(file_path, file_bytes)

                        if res:
                              public_url = supabase.storage.from_(os.getenv("bucket")).get_public_url(file_path)
                        other["img_path"]=public_url
                        other["file_path"]=file_path

                    with st.status("uploading your details.."):
                              data=requests.post("https://littlehope.onrender.com/new_case",headers={"Authorization": f"Bearer {st.session_state.token["token"]}"},
                                                                                                                         json={
                                                                                                                               "child_info":child,
                                                                                                                               "parent_info":parent,
                                                                                                                               "other":other
                                                                                                                         })
                    if data.status_code==200:
                        upload=data.json()
                        if upload["status_of_upload"]==True:
                              st.success("Your data succesfully Uploaded")
                        else:
                              st.error("not uploaded due to some reason.please try again some time later")
                                          
            