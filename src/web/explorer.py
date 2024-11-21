from fastapi import APIRouter, Request
from src.model.Explorer import Explorer, ExplorerNoId
import src.service.explorer as service
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/explorer")


template_obj = Jinja2Templates(directory='templates', )


@router.get("")
@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()


@router.get("/get_one/{id}")
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


@router.get("/list")
def get_list(request: Request):
    explorers = service.get_all()
    return template_obj.TemplateResponse("explorer_list.html",
                                         {"request": request,
                                          "explorers": explorers})

