#!/usr/bin/env python3
# coding: utf-8

"""捕获 Ctrl+c 的键盘中断"""

import time
import sys


def main():
    start = time.perf_counter()
    try:
        for i in range(6):
            print('hello world!')
            time.sleep(1)
    except KeyboardInterrupt:  # 注意每个线程都有自己的异常
        t, v, tb = sys.exc_info()
        print(t)
        exit(0)  # exit 只退出当前线程
    finally:
        end = time.perf_counter()
        finished = end - start
        print('\n[Finished in %.3fs]\n' % finished)


if __name__ == '__main__':
    main()
