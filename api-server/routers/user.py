from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.requests import Request

from extend import config, db

from . import ok, fail

router = APIRouter()


class UserForm(BaseModel):
    title: str


@router.get('/users/')
async def get_users(request: Request = None):
    """
    查询用户
    :param request: 请求参数含有pageNo和pageSize用于分页
    :return:
    """
    count, data = db.page('sci_cnki', request.query_params)
    return ok('查询用户成功', {'total': count, 'data': data})


@router.post('/users/')
async def post_users(userForm: UserForm):
    db.execute("insert into sci_cnki(title)values(%s)", (userForm.title))
    return ok('保存用户成功', {})
