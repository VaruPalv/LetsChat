import streamlit as st
from utils.api_service import validate_login
from utils.session import login_user


def login():
    st.title("Let's Chat")
    st.write("Where Curiosity Meets AI")

    st.subheader("Login to your account")
    username = st.text_input("Username").strip()
    password = st.text_input("Password", type="password").strip()
    login_button = st.button("Login")

    if login_button:
        if username and password:
            success, msg = validate_login(username, password)
            if success:
                login_user(username)
                st.success(msg)
                st.rerun()
            else:
                st.error(msg)
        else:
            st.warning("Please enter both username and password.")