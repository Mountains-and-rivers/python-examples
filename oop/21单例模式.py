#!/usr/bin/env python3
# coding: utf-8

"""仔细比较这两种创建单例模式的方法，它们是有区别的。

进行调试可以更好理解。
"""


class Singleton:
    """普通单例模式，不够好，因为：
    `__init__()` 会多次执行，虽然是同一个实例，如：

    A = Singleton(1)
    B = Singleton(2)

    虽然它们的参数不同，但是是同一个实例。
    可以借助这个方法，修改实例的属性。
    """

    _instance = None

    # 这里的 `__new__()` 要传入 cls，*args, **kwargs 三个参数
    # *args, **kwargs 中的内容，会传入 `__init__()` 中
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # **注意：**`super().__new__()` 中不能传入 cls 以外的参数
            # 因为 Singleton 的父类 Object 的 `__new__()`只有 cls 一个参数
            # 注意不要把上面 `__new__()` 中的参数传进来
            # 否则出现 TypeError: object() takes no parameters 错误
            cls._instance = super().__new__(cls)
        # 这里返回时，实例的 `__init__()` 尚未调用，
        # 所以每次调用类时，会再执行一次 `__init__()`
        return cls._instance

    def __init__(self, n):
        self.n = n
        print('Creating Singleton', self.n)


class SingletonMeta(type):
    """这个元类，可以把所有使用它的类变成单例模式。"""

    def __init__(cls, *args, **kwargs):
        cls._instance = None  # 会变成元类创建的类的类属性
        super().__init__(*args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            # `__call__()` 会调用 `__new__()` 和 `__init__()`,
            # 所以以后再创建实例时，`__init__()` 不会再执行
            cls._instance = super().__call__(*args, **kwargs)
        # 这里返回的实例和 Singleton2 中 `__new__()` 返回的是不同的
        # 这里返回的是调用了 `__init__()` 的实例，
        # Singleton2 的 `__new__()` 中返回的是没调用 `__init__()` 的实例
        return cls._instance


class Spam(metaclass=SingletonMeta):
    """利用元类创建单例方法。

    注意与 Singleton 对比，`__init__()` 不会多次执行，
    原因出在元类的 `__call__()` 返回的是执行了 `__init__()` 的实例。
    """

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self, n):
        self.n = n
        print('Creating Spam', self.n)


def main():
    print('='*50)
    s1 = Singleton(1)  # 会打印内容
    s2 = Singleton(2)  # 会打印内容
    print(s1 is s2)
    print(s1.n)  # s1 属性被修改
    print('='*50)
    s3 = Spam(1)  # 会打印内容
    s4 = Spam(2)  # 不会打印内容
    print(s3 is s4)
    print(s3.n)  # s1 属性未被修改
    print('='*50)


if __name__ == '__main__':
    main()
