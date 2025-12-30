import aiofiles
from fastapi import FastAPI, APIRouter, UploadFile, Depends, status
from fastapi.responses import JSONResponse
from src.helpers.config import get_settings, Settings
from src.controllers import DataController
from src.models import ResponseSignal
import logging
import os

logger = logging.getLogger("uvicorn.error")

router = APIRouter(
    prefix="/api/data",
    tags=["api", "data"]
)


@router.post("/upload/{project_id}")
async def upload(project_id: str, file: UploadFile, app_settings: Settings = Depends(get_settings)):

    data_controller = DataController()
    # validate the file properties
    is_valid, signal = data_controller.validate_uploaded_file(file=file)

    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST, content={
                "signal": signal
            }
        )

    file_path = data_controller.generate_unique_file_name(
        original_file_name=file.filename,
        project_id=project_id
    )

    try:
        async with aiofiles.open(file_path, "wb") as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while uploading file : {e}")

        return JSONResponse(
            content={
                "signal": ResponseSignal.FILE_UPLOAD_FAILD.value
            }
        )

    return JSONResponse(
        content={
            "signal": ResponseSignal.FILE_UPLOAD_SUCCESS.value
        }
    )
