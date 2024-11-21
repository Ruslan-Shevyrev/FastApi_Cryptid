from fastapi import APIRouter, File, UploadFile
from src.service import files
from fastapi.responses import StreamingResponse


router = APIRouter(prefix="/files")


@router.post("/upload_small")
def upload_small(file: bytes = File()) -> dict:
    return files.upload_small(file)


@router.post("/upload_big")
def upload_big(file: UploadFile) -> dict:
    return files.upload_big(file)


@router.get("/download_small/{filename}")
def download_small(filename: str):
    return files.download_small(filename)


@router.get("/download_big/{filename}")
def download_big(filename: str):
    response = StreamingResponse(content=files.download_big(filename),
                                 status_code=200)
    return response
