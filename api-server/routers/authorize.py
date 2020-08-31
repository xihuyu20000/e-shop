from fastapi import APIRouter
from pydantic import BaseModel
from extend import config, db

from datetime import timedelta, datetime
import jwt

from . import ok, fail

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
    user = db.fetchone('select * from sys_user where user_name=%s and passwd=%s', (loginForm.username, loginForm.password))
    if user:
        access_token_expires = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"username": loginForm.username}, expires_delta=access_token_expires)
        user['token'] = access_token
        return ok("登录成功", user)
    else:
        return fail(400, '没有此用户')

@router.get('/menus/')
async def menus():
    menus = [
        {"path": "/home", "label": "首页", "icon": "el-icon-s-home"},
        {"id":125,      "label":"用户管理",     "icon": "el-icon-user",
         "children": [
             {"path": "users", "label": "用户列表", "icon": "el-icon-setting"},
         ]
         },
        {"id": 103,     "label":"权限管理",     "icon": "el-icon-user",
         "children": [
             {"path": "/roles", "label": "角色列表", "icon": "el-icon-setting"},
             {"path": "/rights", "label": "权限列表", "icon": "el-icon-setting"}
         ]
         },
        {"id": 101, "label": "商品管理", "icon": "el-icon-user",
         "children": [
             {"path": "/page1", "label": "页面一", "icon": "el-icon-setting"},
             {"path": "/page2", "label": "页面二", "icon": "el-icon-setting"}
         ]
         },
        {"id": 102, "label": "订单管理", "icon": "el-icon-user",
         "children": [
             {"path": "/page1", "label": "页面一", "icon": "el-icon-setting"},
             {"path": "/page2", "label": "页面二", "icon": "el-icon-setting"}
         ]
         },
        {"id": 145, "label": "数据统计", "path": "reports", "icon": "el-icon-setting",
         "children": [
             {"path": "/page1", "label": "页面一", "icon": "el-icon-setting"},
             {"path": "/page2", "label": "页面二", "icon": "el-icon-setting"}
         ]
         }

    ]
    return ok("获取菜单成功", menus)