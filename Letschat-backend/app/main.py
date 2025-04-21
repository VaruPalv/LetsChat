from fastapi import FastAPI
from app.api.endpoints import router as chat_router
from app.api.auth import router as auth_router
import asyncio
from app.db.database import engine, Base

def create_app() -> FastAPI:
    app = FastAPI(title="Langgraph AI")
    app.include_router(chat_router)
    app.include_router(auth_router)
    return app

async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app = create_app()

if __name__ == "__main__":
    import uvicorn
    asyncio.run(init_models()) 
    uvicorn.run("app.main:app", reload=True)
