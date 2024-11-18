from pydantic import BaseModel


class ExplorerNoId(BaseModel):
    name: str
    country: str
    description: str


class Explorer(ExplorerNoId):
    id: int
