"""`__slots__` 用法。

1、节约内存
2、限制实例添加变量
"""

import sys


class A:
    __slots__ = ()  # 只对当前类起作用，对继承的子类无效

    def __init__(self):
        self.a = []


class B(A):
    __slots__ = ('b',)  # 必须把继承自父类的属性也写上

    def __init__(self):
        super().__init__()
        self.b = []


def main() -> None:
    b = B()
    sys.getsizeof(b)


if __name__ == '__main__':
    main()
