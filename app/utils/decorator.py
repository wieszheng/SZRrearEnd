# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : decorator.py
@Time     : 2023/7/27 22:56
@Author   : v_wieszheng
@Function :
"""

from functools import wraps
from flask import request, jsonify
from jsonschema import validate, FormatChecker, ValidationError
from app import szr
from app.middleware.Jwt import UserToken

FORBIDDEN = "对不起, 你没有足够的权限"


class SingletonDecorator:
    def __init__(self, cls):
        self.cls = cls
        self.instance = None

    def __call__(self, *args, **kwds):
        if self.instance is None:
            self.instance = self.cls(*args, **kwds)
        return self.instance


def permission(role=szr.config.get("MEMBER")):
    def login_required(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                headers = request.headers
                token = headers.get('Authorization')
                if token is None:
                    return jsonify(dict(code=401, msg="用户信息认证失败, 请检查"))
                user_info = UserToken.parse_token(token)
                # 这里把user信息写入kwargs
                kwargs["user_info"] = user_info
            except Exception as e:
                return jsonify(dict(code=401, msg=f"token错误：{e}"))
            # 判断用户权限是否足够, 如果不足够则直接返回，不继续
            if user_info.get("role") < role:
                return jsonify(dict(code=400, msg=FORBIDDEN))
            return func(*args, **kwargs)

        return wrapper

    return login_required


def json_validate(sc):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if request.get_json() is not None:
                    validate(request.get_json(), sc, format_checker=FormatChecker())
                else:
                    raise Exception("请求json参数不合法")
            except ValidationError as e:
                return jsonify(dict(code=101, msg=str(e.message)))
            except Exception as e:
                return jsonify(dict(code=101, msg=str(e)))
            return func(*args, **kwargs)

        return wrapper

    return decorator
