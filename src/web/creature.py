from fastapi import APIRouter, HTTPException
from src.model.Creature import Creature, CreatureNoId
import src.service.creature as service
from sqlite3 import IntegrityError

router = APIRouter(prefix="/creature")


@router.get("")
@router.get("/")
def get_all() -> list[Creature]:
    return service.get_all()


@router.get("/get_one/{id}")
def get(id) -> Creature | None:
    return service.get(int(id))


@router.post("/")
def create(creature: CreatureNoId) -> int:
    try:
        res = service.create(creature)
    except IntegrityError:
        raise HTTPException(status_code=403, detail="Duplicate")
    return res


@router.put("/")
def modify(creature: Creature) -> int:
    return service.modify(creature)


@router.delete("/{id}")
def delete(id: int) -> bool:
    return service.delete(int(id))
