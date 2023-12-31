# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : testcase.py
@Time     : 2023/7/30 15:17
@Author   : v_wieszheng
@Function :
"""
from flask import request, Blueprint, jsonify

from app.dao.testcase.TestCaseDao import TestCaseDao
from app.utils.decorator import permission, json_validate

ts = Blueprint("testcase", __name__, url_prefix="/testcase")
testcase = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
        },
        "name": {
            "type": "string",
        },
        "request_type": {
            "type": "integer",
        },
        "url": {
            "type": "string",
        },
        "request_method": {
            "type": "string",
        },
        "request_header": {
            "type": "string",
        },
        "params": {
            "type": "string",
        },
        "body": {
            "type": "string",
        },
        "project_id": {
            "type": "integer",
        },
        "tag": {
            "type": "string",
        },
        "status": {
            "type": "integer",
        },
        "priority": {
            "type": "string",
        },
        "catalogue": {
            "type": "string",
        },
        "expected": {
            "type": "string",
        },
    },
    "required": ["expected", "catalogue", "priority", "status", "project_id", "request_type", "url", "name"]
}


@ts.route("/insert", methods=["POST"])
@json_validate(testcase)
@permission()
def insert_testcase(user_info):
    data = request.get_json()
    err = TestCaseDao.insert_test_case(data, user_info['id'])
    if err:
        return jsonify(dict(code=110, msg=err))
    return jsonify(dict(code=0, msg="操作成功"))
