from src.model.User import User, UserNoId
import src.data.user as data
import src.utils.auth as auth_util


def get_all() -> list[User]:
    return data.get_all()


def get(id: int) -> User | None:
    return data.get(id)


def create(user: UserNoId) -> int:
    user.password = auth_util.get_hash(user.password)
    return data.create(user)


def modify(user: User) -> int:
    user.password = auth_util.get_hash(user.password)
    return data.modify(user)


def delete(id: int) -> bool:
    return data.delete(id)

def check(username: str, password: str) -> bool:
    user = data.get_by_username(username)
    return auth_util.verify_pass(password, user.password)
