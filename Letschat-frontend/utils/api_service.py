import requests
from utils.config import LOGIN_API_URL, CHAT_API_URL, SIGNUP_API_URL

def validate_login(username, password):
    username = username.strip().lower()
    
    payload = {"username": username, "password": password}
    try:
        response = requests.post(LOGIN_API_URL, json=payload) 
        if response.status_code == 200:
            return True, "Login successful!"
        else:
            return False, "Invalid credentials, please try again."
    except requests.exceptions.RequestException as e:
        return False, f"An error occurred: {e}"

def register_user(username, password):
    username = username.strip().lower()
    
    payload = {"username": username, "password": password}
    try:
        response = requests.post(SIGNUP_API_URL, json=payload)
        if response.status_code == 200:
            return True, "Signup successful!"
        elif response.status_code == 400:
            return False, response.json().get("detail", "Signup failed.")
        else:
            return False, "Signup failed. Please try again."
    except requests.exceptions.RequestException as e:
        return False, f"An error occurred: {e}"

def chat_with_agent(user_input, model_name, system_prompt):
    payload = {
        "messages": [user_input],
        "model_name": model_name,
        "system_prompt": system_prompt
    }
    try:
        response = requests.post(CHAT_API_URL, json=payload)
        if response.status_code == 200:
            return extract_ai_response(response.json())
        else:
            return None
    except requests.exceptions.RequestException:
        return None

def extract_ai_response(response_json):
    return [
        msg.get("content", "")
        for msg in response_json.get("messages", [])
        if msg.get("type") == "ai"
    ][-1] if response_json.get("messages") else None
