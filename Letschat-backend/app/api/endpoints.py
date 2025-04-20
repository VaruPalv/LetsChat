from fastapi import APIRouter
from app.models.request_schema import RequestState
from app.core.agent import create_agent

router = APIRouter()

@router.post("/chat")
def chat_endpoint(request: RequestState):
    agent = create_agent(request.model_name, request.system_prompt)
    
    if agent is None:
        return {"error": "Invalid model name. Please select a valid model."}
    
    state = {"messages": request.messages}
    result = agent.invoke(state)
    return result
