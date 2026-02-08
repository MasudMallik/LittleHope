import streamlit as st
import requests
if "token" not in st.session_state:
    st.error("Please login first to access this page...")
    if st.button("Login",type="primary"):
        st.switch_page("pages/login_reg.py")
else:
    st.title("Your posts...")
    st.divider()
    data=requests.get("https://littlehope.onrender.com/your_posts",headers={"Authorization": f"Bearer {st.session_state.token["token"]}"})
    if data.status_code==200:
        data=data.json()
        if data["posts"]==False:
            st.write("You dont have any posts")
        else:
            i=1
            posts=data["all_posts"]
            for post in posts:
                col1,col2=st.columns(2)
                details={
                "child":{
                    "name":post["child_info"].get("name"),
                    "nick_name":post["child_info"].get("nick_name"),
                    "gender":post["child_info"].get("gender"),
                    "dob":post["child_info"].get("dob"),
                    "height":post["child_info"].get("height"),
                    "weight":post["child_info"].get("weight"),
                    "skin_tone":post["child_info"].get("skin_tone"),
                    "birth_marks":post["child_info"].get("birth_marks"),
                    "tattos":post["child_info"].get("tattos"),
                    "disable":post["child_info"].get("disable"),
                    "date_of_missing":post["child_info"].get("date_of_missing"),
                    "time_of_missing":post["child_info"].get("time_of_missing"),
                    "last_seen_loc":post["child_info"].get("last_seen_loc"),
                },
                "parent":{                      
                        "name":post["parent_info"].get("name"),
                        "relation":post["parent_info"].get("relation"),
                        "contact":post["parent_info"].get("contact"),
                        "alternate_no":post["parent_info"].get("alternate_no"),
                        "email":post["parent_info"].get("email"),
                        "address":post["parent_info"].get("address"),
                        
                        },
                "other":{
                            "posted on":post["other"].get("date_and_time"),
                            "img_path":post["other"].get("img_path")
                        }
                        }
                col1.subheader("Child Details...")
                col1.table(details["child"])
                st.divider()
                col2.subheader("Parent Details...")
                col2.table(details["parent"])
                col2.table(details["other"])
                col2.subheader(f"post No:{i}")
                if col2.button(f"Delete post: {i}",type="primary"):
                    with col2.status("post deletion processing..."):
                        del_post=requests.delete(f"https://littlehope.onrender.com/delete_post/{post['_id']}",headers={"Authorization":f"Bearer {st.session_state.token["token"]}"})
                    if del_post.status_code==200:
                        ans=del_post.json()
                        if ans["delete_post"]==False:
                            col2.error("Post is not deleted. please try again some times letter")
                        else:
                            col2.success("post succesfully deleted")
                            st.rerun()
                    st.write(post["_id"])
                i+=1
                
           