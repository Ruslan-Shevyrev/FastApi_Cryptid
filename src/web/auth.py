from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="/who")

basic: HTTPBasic = HTTPBasic()
secret_user = 'admin'
secret_pass = 'admin'


@router.get("")
def get_user(
        creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if (creds.username == secret_user
            and creds.password == secret_pass):
        return {"username": creds.username,
                "password": creds.password}
    raise HTTPException(status_code=401, detail='NoAdmin')
