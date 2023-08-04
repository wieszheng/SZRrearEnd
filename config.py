# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : config.py
@Time     : 2023/8/4 23:07
@Author   : v_wieszheng
@Function :
"""
import os

from pydantic import BaseSettings

ROOT = os.path.dirname(os.path.abspath(__file__))


class BaseConfig(BaseSettings):
    LOG_DIR = os.path.join(ROOT, 'logs')
    LOG_NAME = os.path.join(ROOT, 'logs', 'szr.log')

    # Flask jsonify编码问题
    JSON_AS_ASCII = False

    # sqlalchemy
    SQLALCHEMY_DATABASE_URI = ''

    # 异步URI
    ASYNC_SQLALCHEMY_URI = ''
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 权限 0 普通用户 1 组长 2 管理员
    MEMBER = 0
    MANAGER = 1
    ADMIN = 2

    # mysql配置
    MYSQL_HOST = "43.143.159.11"
    MYSQL_PORT = 3306
    MYSQL_USER = "root"
    MYSQL_PWD = "test2023"
    DBNAME = "szr"


class DevConfig(BaseConfig):
    class Config:
        env_file = os.path.join(ROOT, "conf", "dev.env")


class ProConfig(BaseConfig):
    class Config:
        env_file = os.path.join(ROOT, "conf", "pro.env")


# 获取szr环境变量
SZR_ENV = os.environ.get("szr_env", "dev")
# 如果szr_env存在且为prod
Config = ProConfig() if SZR_ENV and SZR_ENV.lower() == "pro" else DevConfig()

# init sqlalchemy (used by apscheduler)
Config.SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@{}:{}/{}'.format(
    Config.MYSQL_USER, Config.MYSQL_PWD, Config.MYSQL_HOST, Config.MYSQL_PORT, Config.DBNAME)


BANNER = """
███─████─████
█─────██─█──█
███──██──████
──█─██───█─█─
███─████─█─█─
"""
