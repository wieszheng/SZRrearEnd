# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : __init__.py.py
@Time     : 2023/7/27 23:14
@Author   : v_wieszheng
@Function :
"""
# flask_sqlalchemy SQLAlchemy 版本问题
from flask_sqlalchemy import SQLAlchemy

from app import szr

db = SQLAlchemy(szr)