import streamlit as st
home=st.Page(
    page="pages/home.py",
    title="home page",
    default=True
)
childs=st.Page(
    page="pages/childs_details.py",
    title="Missing Childs",
)
log=st.Page(
    page="pages/login_reg.py",
    title="login or registration",
)
cases=st.Page(
    page="pages/report_child.py",
    title="upload details"
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
        "information":[home,childs,log,cases,setting,terms_and_conditions]
    }
)

pg.run()