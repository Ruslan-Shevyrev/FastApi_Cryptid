from fastapi import APIRouter, HTTPException
from src.model.User import User, UserNoId
import src.service.user as service
from sqlite3 import IntegrityError

router = APIRouter(prefix="/user")


@router.get("")
@router.get("/")
def get_all() -> list[User]:
    return service.get_all()


@router.get("/{id}")
def get(id) -> User | None:
    return service.get(int(id))


@router.post("/")
def create(creature: UserNoId) -> int:
    try:
        res = service.create(creature)
    except IntegrityError:
        raise HTTPException(status_code=403, detail="Duplicate")
    return res


@router.put("/")
def modify(creature: User) -> int:
    return service.modify(creature)


@router.delete("/{id}")
def delete(id: int) -> bool:
    return service.delete(int(id))
