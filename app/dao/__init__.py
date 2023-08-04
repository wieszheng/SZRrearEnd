# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : __init__.py.py
@Time     : 2023/8/4 23:34
@Author   : v_wieszheng
@Function :
"""
from app.models import db
from app.models.user import User
from app.models.project import Project
from app.models.project_role import ProjectRole
from app.models.test_case import TestCase

db.create_all()