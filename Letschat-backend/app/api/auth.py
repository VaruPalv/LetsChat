from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
class LoginPayload(BaseModel):
    username: str
    password: str
users_db = {
    "varshini": "varshini@11",
}
@router.post("/validate_login")
def validate_login(payload: LoginPayload):
    if users_db.get(payload.username) == payload.password:
        return {"success": True, "message": "Login successful!"}
    raise HTTPException(status_code=400, detail="Invalid credentials")
