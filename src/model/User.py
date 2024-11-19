from pydantic import BaseModel


class UserNoId(BaseModel):
    name: str
    password: str


class User(UserNoId):
    id: int
