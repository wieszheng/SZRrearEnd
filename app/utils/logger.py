# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : logger.py
@Time     : 2023/7/27 22:54
@Author   : v_wieszheng
@Function :
"""
import logbook
from app import szr
from .decorator import SingletonDecorator

@SingletonDecorator
class Log(object):
    handler = None

    def __init__(self, name='szr', filename=szr.config['LOG_NAME']):  # Logger标识默认为app
        """
        :param name: 业务名称
        :param filename: 文件名称
        """
        self.handler = logbook.FileHandler(filename, encoding='utf-8')
        logbook.set_datetime_format("local")
        self.logger = logbook.Logger(name)
        self.handler.push_application()

    def info(self, *args, **kwargs):
        return self.logger.info(*args, **kwargs)

    def error(self, *args, **kwargs):
        return self.logger.error(*args, **kwargs)

    def warning(self, *args, **kwargs):
        return self.logger.warning(*args, **kwargs)

    def debug(self, *args, **kwargs):
        return self.logger.debug(*args, **kwargs)
