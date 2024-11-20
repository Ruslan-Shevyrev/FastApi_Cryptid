from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ALGORITHM = 'HS256'
KEY = 'secret'
TIME_DELTA = 15


def get_hash(plain: str) -> str:
    return pwd_context.hash(plain)


def verify_pass(plain: str, hash: str) -> bool:
    return pwd_context.verify(plain, hash)


def encode_jwt(data: dict) -> str:
    now = datetime.now()
    expire = now + timedelta(minutes=TIME_DELTA)
    data['expire'] = str(expire)
    token = jwt.encode(data, key=KEY, algorithm=ALGORITHM)
    return token


def decode_jwt(token: str) -> dict:
    data = jwt.decode(token, key=KEY, algorithms=ALGORITHM)
    return data
