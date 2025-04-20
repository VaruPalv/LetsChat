from pydantic import BaseModel
from typing import List

class RequestState(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]