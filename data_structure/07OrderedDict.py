"""有序字典 OrderedDict。

虽然 Python3.6 后的 dict 已经默认有序，但官方不推荐依赖这种特性。

有序字典比一般字典还多了以下方法：
`d.popitem(last=True)`
`d.move_to_end(key, last=True)`
"""

from collections import OrderedDict


def main() -> None:
    od = OrderedDict(A=1, B=2, C=3)
    print(od)

    # 新添加的元素会到结尾
    od['D'] = 4
    print(od)

    # 但已存在的 key 修改则不会移动
    od['A'] = 5
    print(od)

    # 将一个元素移动到结尾，若 last 为 False，则移动到开头
    od.move_to_end('A')  # last 默认 True
    print(od)

    od.move_to_end('A', last=False)
    print(od)

    # 默认弹出最后一个元素，若 last 为 False，则弹出开头的
    od.popitem()  # last 默认 True
    print(od)

    od.popitem(last=False)
    print(od)


if __name__ == '__main__':
    main()
