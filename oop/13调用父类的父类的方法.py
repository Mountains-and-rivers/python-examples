"""测试实例方法的继承与调用父类的父类的方法。"""


class A:

    def hello(self):
        print('A: hello, world!')


class B(A):

    def hello(self):
        print('B: hello, world!')


class C(B):

    def hello(self):
        print('C: hello, world!')


class D(C):

    def hello(self):
        print('D: hello, world!')
        super().hello()
        super(C, self).hello()
        super(B, self).hello()


def test():
    D().hello()


if __name__ == '__main__':
    test()
