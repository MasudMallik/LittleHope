import streamlit as st
home=st.Page(
    page="pages/home.py",
    title="home page",
    icon="🏠",
    default=True
)
childs=st.Page(
    page="pages/childs_details.py",
    title="Missing Childs",
    icon="👶"
)
log=st.Page(
    page="pages/login_reg.py",
    title="login or registration",
    icon="🔐"
)
cases=st.Page(
    page="pages/report_child.py",
    title="upload details",
    icon="🔍"
)
posts=st.Page(
    page="pages/your_posts.py",
    title="Your posts",
    icon="📚"
)
setting=st.Page(
    page="pages/setting.py",
    title="settings",
    icon="🛠️"
)
terms_and_conditions=st.Page(
    page="pages/terms_and_conditions.py",
    title="Terms and Conditions",
    icon="📜"
)
pg=st.navigation(
    {
        "information":[home,childs,log,cases,posts,setting,terms_and_conditions]
    }
)

pg.run()