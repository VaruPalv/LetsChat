from fastapi import FastAPI
from app.api.endpoints import router as chat_router
from app.api.auth import router as auth_router

def create_app() -> FastAPI:
    app = FastAPI(title="Langgraph AI")
    app.include_router(chat_router)
    app.include_router(auth_router)
    return app

app = create_app()
