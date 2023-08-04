# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : factory.py
@Time     : 2023/7/28 0:17
@Author   : v_wieszheng
@Function :
"""
from datetime import datetime
from typing import Any
from app.handler.encoder import jsonable_encoder


class SzrResponse():

    @staticmethod
    def model_to_dict(obj, *ignore: str):
        data = dict()
        for c in obj.__table__.columns:
            if c.name in ignore:
                # 如果字段忽略, 则不进行转换
                continue
            val = getattr(obj, c.name)
            if isinstance(val, datetime):
                data[c.name] = val.strftime("%Y-%m-%d %H:%M:%S")
            else:
                data[c.name] = val
        return data

    @staticmethod
    def model_to_list(data: list, *ignore: str):
        return [SzrResponse.model_to_dict(x, *ignore) for x in data]

    @staticmethod
    def encode_json(data: Any, *exclude: str):
        return jsonable_encoder(data, exclude=exclude, custom_encoder={
            datetime: lambda x: x.strftime("%Y-%m-%d %H:%M:%S")
        })

    @staticmethod
    def success(data=None, code=0, msg="操作成功", exclude=()):
        return SzrResponse.encode_json(dict(code=code, msg=msg, data=data), *exclude)

    @staticmethod
    def failed(msg, code=110, data=None):
        return dict(code=code, msg=str(msg), data=data)
