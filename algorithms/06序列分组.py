#!/usr/bin/env python3
# coding: utf-8

"""给定输入值列表 inputs 和正整数 n，
编写一个将 inputs 拆分为长度为 n 的组的函数。
"""

from itertools import zip_longest


def grouper(inputs, n, fillvalue=None):

    # 巧妙利用了迭代器
    iters = [iter(inputs)] * n

    # 使用 `zip` 或 `zip_longest` 来决定
    # 长度不满 n 的剩余部分，是用 fillvalue 来填充，
    # 还是丢弃
    # return zip(*iters)
    return zip_longest(*iters, fillvalue=fillvalue)


def main():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    print(list(grouper(nums, 4)))


if __name__ == '__main__':
    main()
