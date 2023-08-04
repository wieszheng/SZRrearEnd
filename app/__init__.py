# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : __init__.py.py
@Time     : 2023/8/4 22:53
@Author   : v_wieszheng
@Function :
"""
from flask import Flask
from flask_cors import CORS
from config import Config, SZR_ENV, BANNER

szr = Flask(__name__)
CORS(szr,supports_credentials=True)

szr.config.from_object(Config)
