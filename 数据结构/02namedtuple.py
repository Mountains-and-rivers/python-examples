#!/usr/bin/env python3
# coding: utf-8

"""具名元组。
"""

from collections import namedtuple


def main():
    # 字符串 'Point' 决定了，打印出来的名字
    # Point = namedtuple('Point', ('x', 'y'))
    # 或传入字符串, 参数之间用空格分开
    Point = namedtuple('Point', 'x y')
    p = Point(1, 2)
    print(p)

    # 两种取值方式
    print(p.x, p.y)
    print(p[0], p[1])

    # 返回 Point 拥有的字段，是一个元组
    print(Point._fields)

    # 转换成字典，`collections.OrderedDict` 类型
    print(p._asdict())

    # 替换一个属性值，非原地，会返回一个新命名元组
    p2 = p._replace(x=100)
    print(p2.x, p2.y)


if __name__ == '__main__':
    main()
