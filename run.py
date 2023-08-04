# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : run.py
@Time     : 2023/7/27 22:52
@Author   : v_wieszheng
@Function :
"""

from app import szr
from app.controller.auth.user import auth
from app.controller.request.http import req
from app.controller.project.project import pr
from app.controller.testcase.testcase import ts
from app.utils.logger import Log
from app import dao

# 注册蓝图
szr.register_blueprint(auth)
szr.register_blueprint(req)
szr.register_blueprint(pr)
szr.register_blueprint(ts)



if __name__ == "__main__":
    szr.run("0.0.0.0", threaded=True, port=7777, debug=True)
