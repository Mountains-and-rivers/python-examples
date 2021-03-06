#!/usr/bin/env python3
# coding: utf-8

"""一般将安装脚本命名为 setup.py，
然后执行 python3 setup.py install 安装.
"""

from setuptools import setup


setup(
    name='myworld',  # 库名
    version='1.0',  # 版本信息
    author='zzzzer',  # 作者
    author_email='zzzzer91@gmail.com',  # 作者邮箱
    url='https://github.com/zzzzer91/python-example',  # 库发布地址
    packages=['myworld'],  # 当前目录下哪些文件夹会被安装
    entry_points={  # 让你的库在控制台能以'hello xxx'的形式运行, xxx会以命令行参数形式传入test函数中
        'console_scripts': ['hello=myworld.core:test']
    },
    install_requires=[  # 库前置依赖
        'requests',
    ],
    include_package_data=True,  # 打包非 py 的静态资源，如 html，css 等资源
    zip_safe=False  # 安装后的库是否压缩, True 会导致 vscode 无法正常显示补全
)