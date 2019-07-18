"""使用 `bisect` 模块的相关函数时，必须保证序列有序（为空也行）。

bisect 函数其实是 bisect_right 函数的别名,后者还有个姊妹函数叫 bisect_left。
它们的区别在于,bisect_left 返回的插入位置是原序列中跟被插入元
素相等的元素的位置,也就是新元素会被放置于它相等的元素的前面,而 bisect_right
返回的则是跟它相等的元素之后的位置。这个细微的差别可能对于整数序列来讲没什么用,
但是对于那些值相等但是形式不同的数据类型来讲,结果就不一样了。比如说虽然 1
== 1.0 的返回值是 True,1 和 1.0 其实是两个不同的元素。
"""

import bisect


def example1():
    """在序列中找到位置，并插入。"""

    # 一些随机数
    values = [14, 85, 77, 26, 50, 45, 66, 79, 10, 3, 84, 77, 1]

    print('New  Pos  Contents')
    print('---  ---  --------')

    l = []
    for i in values:
        # 查找元素位置
        position = bisect.bisect(l, i)
        # 这个函数结合了查找和插入
        bisect.insort(l, i)
        print('{:3}  {:3}'.format(i, position), l)


def example2():
    """分数换算等第。很精妙。"""

    def grade(score, breakpoints=(60, 70, 80, 90), grades='FDCBA'):
        i = bisect.bisect(breakpoints, score)
        return grades[i]

    print([grade(score) for score in [33, 99, 77, 70, 89, 90, 100]])


def main() -> None:
    example1()
    print('*' * 50)
    example2()


if __name__ == '__main__':
    main()
