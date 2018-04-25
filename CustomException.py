#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-25 16:27:24
# @Author  : Zhilin Shuai (zhilin_shuai@trendmicro.com.cn)
# @Link    : http://www.example.com.cn/
# @Version : $Id$


class CustomException(Exception):
    """docstring for CustomException"""

    def __init__(self, error_message):
        super(CustomException, self).__init__()
        self.message = error_message

    def __str__(self):
        return self.message


class EncryptKeyErrorException(CustomException):
    """docstring for KeyErrorException"""

    def __init__(self, error_message):
        super(EncryptKeyErrorException, self).__init__(error_message)
