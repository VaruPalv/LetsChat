import streamlit as st

def init_session():
    """
    Initialize session state variables if they don't exist.
    """
    st.session_state.setdefault("username", "")
    st.session_state.setdefault("logged_in", False)

def is_logged_in():
    """
    Check if the user is logged in.
    """
    return st.session_state.get("logged_in", False)

def login_user(username):
    """
    Mark user as logged in and store their username.
    """
    st.session_state["username"] = username
    st.session_state["logged_in"] = True

def logout_user():
    """
    Log the user out and clear session state.
    """
    st.session_state["username"] = ""
    st.session_state["logged_in"] = False
