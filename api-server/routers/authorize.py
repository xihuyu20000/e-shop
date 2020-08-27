from fastapi import APIRouter
from pydantic import BaseModel
from extend import config, db




from datetime import timedelta, datetime
import jwt

from routers import ok, fail


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, config.JWT_KEY, algorithm="HS256")
    return encoded_jwt


def decode_access_token(*, data: str):
    to_decode = data
    return jwt.decode(to_decode, config.JWT_KEY, algorithm="HS256")


router = APIRouter()

class LoginForm(BaseModel):
    username:str
    password:str

@router.post('/login/')
async def login(loginForm: LoginForm):
    user = db.fetchone('select * from stu where name=%s and pwd=%s', (loginForm.username, loginForm.password))
    if user:
        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"username": loginForm.username}, expires_delta=access_token_expires)
        user['token'] = access_token
        return ok("登录成功", user)
    else:
        return fail(400, '没有此用户')
