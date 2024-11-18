from pydantic import BaseModel


class CreatureNoId(BaseModel):
    name: str
    country: str
    area: str
    description: str
    aka: str


class Creature(CreatureNoId):
    id: int
