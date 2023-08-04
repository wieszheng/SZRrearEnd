# -*- coding:utf-8 -*-

"""
@Version  : Python3.8
@FileName : page.py
@Time     : 2023/7/29 16:08
@Author   : v_wieszheng
@Function :
"""
from flask import request

# 默认页数和页码
PAGE = 1
SIZE = 10


class PageHandler(object):

    @staticmethod
    def page():
        """
        获取page和size
        :return:
        """
        page = request.args.get("page")
        if page is None or not page.isdigit():
            page = PAGE
        size = request.args.get("size")
        if size is None or not size.isdigit():
            size = SIZE
        return int(page), int(size)
