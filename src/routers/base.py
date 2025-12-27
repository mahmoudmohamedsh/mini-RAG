from fastapi import FastAPI, APIRouter, Depends
from src.helpers.config import get_settings, Settings

router = APIRouter(
    prefix="/api",
    tags=["basic"]
)


@router.get("/")
async def welcome(app_settings: Settings = Depends(get_settings)):

    return {
        "app_name": app_settings.APP_NAME,
        "app_version": app_settings.APP_VERSION
    }
