from fastapi import APIRouter, HTTPException
from src.model.Explorer import Explorer, ExplorerNoId
import src.service.explorer as service

router = APIRouter(prefix="/explorer")


@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/{id}")
def get(id) -> Explorer | None:
    return service.get(int(id))


@router.post("/")
def create(explorer: ExplorerNoId) -> int:
    return service.create(explorer)


@router.patch("/")
def modify(explorer: Explorer) -> int:
    return service.modify(explorer)


@router.delete("/{id}")
def delete(id: int) -> bool:
    return service.delete(int(id))
