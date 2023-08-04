# -*- coding: utf-8 -*-

"""
@file    : http.py
@author  : v_wieszheng
@Data    : 2023-07-28 下午 05:56
@software: PyCharm
"""
import json

from flask import Blueprint
from flask import jsonify
from flask import request

from app import szr
from app.handler.factory import SzrResponse
from app.middleware.HttpClient import Request
from app.utils.decorator import permission

req = Blueprint("request", __name__, url_prefix="/request")


@req.route("/http", methods=['POST'])
@permission()
def http_request(user_info):
    data = request.get_json()
    method = data.get("method")
    if not method:
        return SzrResponse.success(code=101, msg="请求方式不能为空")
    url = data.get("url")
    if not url:
        return SzrResponse.success(code=101, msg="请求地址不能为空")
    body = data.get("body")
    headers = data.get("headers")
    r = Request(url, data=body, headers=headers)
    response = r.request(method)
    if response.get("status"):
        return SzrResponse.success(response)
    return SzrResponse.failed(response.get("msg"), data=response)
