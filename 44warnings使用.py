#!/usr/bin/env python3
# coding: utf-8

import warnings


# warnings.warn('仅用于提示，而不中断执行')


"""
error 将警告提升为异常

ignore 忽略警告

always 总是抛出警告

default 从各个位置第一次生成警告时输出警告

module 从各个模块第一次生成警告时输出警告

once 第一次生成警告时输出警告
"""
warnings.filterwarnings('error')  # 将警告提升为异常

try:
    warnings.warn('测试捕获 warning')
except Warning:
    print('捕获 warning')
