import streamlit as st
from components.login_form import login
from components.signup_form import signup 
from components.chat_box import chat_interface
from utils.session import init_session, is_logged_in

st.set_page_config(page_title="Langgraph Agent", layout="centered")

init_session()

if not is_logged_in():
    auth_mode = st.radio("Choose an option:", ("Login", "Signup"))

    if auth_mode == "Login":
        login()
    else:
        signup()  
else:
    chat_interface()
