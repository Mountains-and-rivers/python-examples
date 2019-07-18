"""memoryview 是一个内置类,它能让用户在不复制内容的情况下操作目标内存。"""

import array


def main() -> None:
    numbers = array.array('h', [-2, -1, 0, 1, 2])
    memv = memoryview(numbers)
    print(len(memv))
    print(memv[0])
    # 类型转换
    memv_oct = memv.cast('B')
    print(memv_oct.tolist())
    # 修改目标内存
    memv_oct[5] = 4
    print(numbers)


if __name__ == '__main__':
    main()
