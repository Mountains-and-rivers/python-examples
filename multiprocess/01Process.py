#!/usr/bin/env python3
# coding: utf-8

"""multiprocessing 模块的 Process 类。

创建子进程时，只需要创建一个 Process 实例，用 `start()` 方法启动。
不要在多进程调用函数中使用全局变量，这样会报错。
"""

import time
from multiprocessing import Process

a = 10


def process1(n):
    # 无限循环
    while True:
        print('process:{}'.format(n))
        time.sleep(1)
        global a
        a += 1
        print(a)


def process2(n):
    # 非无限循环
    for i in range(4):
        print('process:{}'.format(n))
        time.sleep(2)
        global a
        a += 1
        print(a)


def main():
    # args必须是一个元组
    p1 = Process(target=process1, args=(1,))
    p2 = Process(target=process2, args=(2,))
    p1.start()  # 调用start()方法后，程序正式启动
    # p1.join()  # join()方法会等待当前子进程结束，才会继续往下执行，这里p2永远不会执行，因为p1是无限循环
    p2.start()
    p2.join()  # 不加这句，会立即执行下面的代码
    print('进程2 结束')
    # p1.close()  # 注意Process类没有close()方法，别和Pool类搞混了
    p1.terminate()  # terminate()方法可以强制终止无限循环的子进程
    print('进程1 结束')


if __name__ == '__main__':
    main()
