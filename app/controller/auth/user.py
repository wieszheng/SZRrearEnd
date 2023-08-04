# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : user.py
@Time     : 2023/7/27 23:03
@Author   : v_wieszheng
@Function :
"""
from flask import Blueprint, request
from flask import jsonify

from app.dao.auth.UserDao import UserDao
from app.middleware.Jwt import UserToken
from app.handler.factory import SzrResponse
from app.utils.decorator import permission

auth = Blueprint("auth", __name__, url_prefix="/auth")


# 这里以auth.route注册的函数都会自带/auth，所以url是/auth/register
@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return jsonify(dict(code=101, msg="Invalid username or password"))
    email, name = data.get("email"), data.get("name")
    if not email or not name:
        return jsonify(dict(code=101, msg="姓名或邮箱不能为空"))
    err = UserDao.register_user(username, name, password, email)
    if err is not None:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=0, msg="注册成功"))


@auth.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    username, password = data.get("username"), data.get("password")
    if not username or not password:
        return SzrResponse.failed(code=101, msg="用户名或密码不能为空")
    user, err = UserDao.login(username, password)
    if err is not None:
        return SzrResponse.failed(str(err))
    user = SzrResponse.model_to_dict(user, "password")
    expire, token = UserToken.get_token(user)
    return SzrResponse.success(dict(token=token, user=user, expire=expire), msg="登录成功")


@auth.route("/profile")
@permission()
def profile(user_info):
    return jsonify(dict(code=0, data=user_info))


@auth.route("/listUser")
@permission()
def list_users(user_info):
    users, err = UserDao.list_users()
    if err is not None:
        return SzrResponse.failed(str(err))
    return SzrResponse.success(users, exclude=("password",))
