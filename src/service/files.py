from fastapi import UploadFile
from fastapi.responses import FileResponse
from typing import Generator


def upload_small(file: bytes) -> dict:
    return {"len_bytes": len(file)}


def upload_big(file: UploadFile) -> dict:
    return {"len_bytes": file.size,
            "filename": file.filename}


def download_small(filename: str):
    return FileResponse(filename)


def file_gen(path: str) -> Generator:
    with open(file=path, mode='rb') as file:
        yield file.read()


def download_big(filename: str):
    expr = file_gen(filename)
    return expr
