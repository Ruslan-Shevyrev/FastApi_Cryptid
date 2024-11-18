from src.model.Explorer import Explorer
import src.data.explorer as data


def get_all() -> list[Explorer]:
    return data.get_all()


def get(id: int) -> Explorer | None:
    return data.get(id)


def create(explorer: Explorer) -> int:
    return data.create(explorer)


def modify(explorer: Explorer) -> int:
    return data.modify(explorer)


def delete(id: int) -> bool:
    return data.delete(id)
