from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_hash(plain: str) -> str:
    return pwd_context.hash(plain)


def verify_pass(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)