import streamlit as st
from utils.api_service import register_user
from utils.session import login_user

def signup():
    st.title("Let's Chat")
    st.write("Create an account to get started!")

    st.subheader("Signup")
    username = st.text_input("Choose a Username").strip()
    password = st.text_input("Choose a Password", type="password").strip()
    signup_button = st.button("Sign Up")

    if signup_button:
        if username and password:
            success, msg = register_user(username, password)
            if success:
                st.success(msg)
                login_user(username)  # auto login after signup
                st.rerun()
            else:
                st.error(msg)
        else:
            st.warning("Please enter both username and password.")
