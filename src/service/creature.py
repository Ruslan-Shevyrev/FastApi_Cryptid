from src.model.Creature import Creature, CreatureNoId
import src.data.creature as data


def get_all() -> list[Creature]:
    return data.get_all()


def get(id: int) -> Creature | None:
    return data.get(id)


def create(creature: CreatureNoId) -> int:
    return data.create(creature)


def modify(creature: Creature) -> int:
    return data.modify(creature)


def delete(id: int) -> bool:
    return data.delete(id)
