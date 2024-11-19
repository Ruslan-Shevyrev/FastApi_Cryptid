from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import src.service.user as data

router = APIRouter(prefix="/check_auth")

basic: HTTPBasic = HTTPBasic()


@router.get("")
def get_user(
        creds: HTTPBasicCredentials = Depends(basic)) -> dict:
    if data.check(str(creds.username), str(creds.password)):
        return {"username": creds.username,
                "password": creds.password}
    raise HTTPException(status_code=401, detail='No Authorised')
