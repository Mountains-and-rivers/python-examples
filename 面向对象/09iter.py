"""`__iter__()` 与 `__next__()`

对比 `Fib` 类和 `Iter` 类，可以得出结论，
`__iter__()` 要返回一个实现了 `__next__()` 对象。
这个对象可以是自身（要实现 `__next__()`），也可以是别的，
如下面的 `iter(self._list)`。
"""


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        print('__iter__')
        return self  # 实例本身就是迭代对象，因为实现了 `__next__()`

    def __next__(self):
        print('__next__')
        # 注意这里会改变实例的值，我觉得不太好，可以放到临时变量上
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100000:  # 退出循环的条件
            raise StopIteration
        return self.a  # 返回下一个值


class Iter:
    def __init__(self, list_):
        self._list = list_

    def __iter__(self):
        return iter(self._list)


def main() -> None:
    fib = Fib()
    print(f'>>> {fib.a}')

    # 可以看到先调用 `__iter__()`，返回一个 generator
    # 然后不停调用 `__next__()` 方法
    for i in fib:
        print(i)

    # 但是 a 的值也变了
    print(f'>>> {fib.a}')

    it = Iter([1, 2, 3])
    for i in it:
        print(i)


if __name__ == '__main__':
    main()
