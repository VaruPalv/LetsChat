

from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from app.core.config import GROQ_API_KEY, MODEL_NAMES
from app.core.tools import calculator

# Initialize the Groq model
def get_groq_model(model_name: str):
    return ChatGroq(groq_api_key=GROQ_API_KEY, model_name=model_name)

# Create the agent using Groq model, calculator, and Tavily search tool
def create_agent(model_name: str, system_prompt: str):
    if model_name not in MODEL_NAMES:
        return None

    model = get_groq_model(model_name)
    tools = [TavilySearchResults(max_results=10), calculator]

    return create_react_agent(model, tools=tools, state_modifier=system_prompt)
