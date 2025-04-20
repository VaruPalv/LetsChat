import streamlit as st
from utils.api_service import chat_with_agent, extract_ai_response
from utils.constants import MODEL_NAMES


def chat_interface():
    st.title("Let's Chat")
    st.write("Where Curiosity Meets AI")

    system_prompt = st.text_area("Define your AI Agent:", height=100,
                                  placeholder="Say act as researcher/analyst...")
    selected_model = st.selectbox("Select Model", MODEL_NAMES)
    user_input = st.text_area("Enter your message(s):", height=150,
                               placeholder="Type your message here...")

    if st.button("Submit"):
        if user_input.strip():
            ai_response = chat_with_agent(user_input, selected_model, system_prompt)
            if ai_response:
                st.subheader("Agent Response:")
                st.markdown(f"**Final Response:** {ai_response}")
            else:
                st.warning("No AI response found in the output.")
        else:
            st.warning("Please enter a message before submitting.")

    if st.button("Logout"):
        from utils.session import logout_user
        logout_user()
        st.success("Logged out successfully!")
        st.rerun()