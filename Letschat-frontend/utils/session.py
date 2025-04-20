import streamlit as st

def init_session():
    if "username" not in st.session_state:
        st.session_state["username"] = ""
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

def is_logged_in():
    return st.session_state.get("logged_in", False)

def login_user(username):
    st.session_state["username"] = username
    st.session_state["logged_in"] = True

def logout_user():
    st.session_state["username"] = ""
    st.session_state["logged_in"] = False
