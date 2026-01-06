from fastapi import FastAPI
from contextlib import asynccontextmanager
from .routers import base, data
from motor.motor_asyncio import AsyncIOMotorClient
from .helpers.config import get_settings

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting up…")
    settings = get_settings()
    
    app.mongo_conn = AsyncIOMotorClient(settings.MONGODB_URL)
    app.db_client = app.mongo_conn[settings.MONGODB_DATABASE]
    yield
    print("🛑 Shutting down…")
    app.mongo_conn.close()


app = FastAPI(lifespan=lifespan)


app.include_router(base.router)
app.include_router(data.router)
