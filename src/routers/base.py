from fastapi import FastAPI , APIRouter
import os

router = APIRouter(
    prefix="/api",
    tags=["basic"]
)

@router.get("/")
async def welcome():
    return {
        "app_name": os.getenv("APP_NAME"),
        "app_version":os.getenv("APP_VERSION")
    }