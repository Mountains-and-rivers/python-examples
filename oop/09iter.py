"""`__iter__()` 与 `__next__()`

对比 `Fib` 类和 `Iter` 类，可以得出结论，
`__iter__()` 要返回一个实现了 `__next__()` 对象。
这个对象可以是自身（要实现 `__next__()`），也可以是别的，
如下面的 `iter(self._list)`。

`Count` 这样的定义也是可以的，因为带有 `yield` 关键字，
所以 `__iter__()` 本身是个迭代器。
"""


class Fib:
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        print('__iter__')
        return self  # 实例本身就是迭代器，因为实现了 `__next__()`

    def __next__(self):
        print('__next__')
        # 注意这里会改变实例的值，我觉得不太好，可以放到临时变量上
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000:  # 退出循环的条件
            raise StopIteration
        return self.a  # 返回下一个值


class Iter:
    def __init__(self, list_):
        self._list = list_

    def __iter__(self):
        return iter(self._list)


class Count:
    def __init__(self, n):
        self._n = n

    def __iter__(self):
        """带 `yield` 关键字，成了生成器（迭代器的一种），
        不再需要实现 `__next__()`。
        """

        n = self._n
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self._n:
            yield n
            n += 1


def main() -> None:
    fib = Fib()
    print(f'>>> {fib.a}')

    # 可以看到先调用 `__iter__()`，返回一个 generator
    # 然后不停调用 `__next__()` 方法
    # 不实现 `__iter__()`，实现`__getitem__()`，也能用 for 迭代
    for i in fib:
        print(i)

    # 但是 a 的值也变了
    print(f'>>> {fib.a}')

    print('*'*50)
    it = Iter([1, 2, 3])
    for i in it:
        print(i)

    print('*'*50)
    for x in Count(5):
        print(x)


if __name__ == '__main__':
    main()
