#!/usr/bin/env python3
# coding: utf-8

"""多种编码的应对方式"""

import re
from urllib import parse


def example1():
    """utf-8编码解码"""

    # 无法显示为 ascii 的字符都以 \x## 显示
    b = b'\xe5\x92\x95\xe5\x92\x95\xe5\xa4\xaa\xe7\xa1\xac\xe4\xba\x86'
    # 默认utf-8
    s = b.decode()
    print(s)
    # 默认utf-8
    b = s.encode()
    print(b)


def example2():
    """unicode编码解码"""

    print(hex(ord('咕')))
    # utf-8 的中文占 3 个字节，而这里的 \u5495 是 unicode，只占 2 个字节
    print('\u5495')

    # unicod 编码是内存中字符的编码，跟文本中的编码不一样，
    # unicode 所有字符在内存中占两个字节，以 Litte-Endian 形式存放，
    # 即 A 的 unicode 的编号虽然是00000000 01000001，
    # 但在内存中从小地址到大地址是这样存放的 01000001 00000000，
    # 数字也是如此，即超过一字节的数字都以 Litte-Endian 形式存放
    print('\u5495\u5495\u592a\u786c\u4e86')


def example3():
    """把十六进制数字组成的字符串转换成 utf-8"""

    # s 是 wireshark 中复制出来的一段十六进制数字组成的字符串
    s = 'a0000000a0000000b202000074797065403d636861746d' \
        '73672f726964403d3233313535342f756964403d393731' \
        '373239372f6e6e403d323731323336306162632f74787440' \
        '3de59295e59295e5a4aae7a1ace4ba862f636964403d32' \
        '6265666432393665383035346364346630303630623030303030' \
        '30303030302f6963403d61766174617240' \
        '5364656661756c74405330362f6c6576656c403d332f656c403d2f00'

    # 两种转换方式
    b = int(s, 16).to_bytes(len(s) // 2, 'big')
    b = bytes.fromhex(s)

    # 提取出信息
    pattern = re.compile(b'type@=chatmsg/.+?/nn@=(.+?)/txt@=(.+?)/.+?/level@=(.+?)/')
    for nn, txt, level in pattern.findall(b):
        print('[lv.{:0<2}][{}]: {}'.format(level.decode(), nn.decode(), txt.decode().strip()))


def example4():
    """处理'\\uxxxx'形式的字符串"""

    # 一段非常规的 unicode 字符串
    s = '\\u5495\\u5495\\u592a\\u786c\\u4e86'
    pattern = re.compile(r'\\u\w{4}')
    s = pattern.sub(lambda x: chr(int(x.group(0).replace('\\u', ''), 16)), s)
    print(s)

    # 另一种形式，多两个单引号
    s = ascii('咕咕太硬了')  # "'\\u5495\\u5495\\u592a\\u786c\\u4e86'"
    print(eval(s))


if __name__ == '__main__':
    # example1()
    # example2()
    # example3()
    # example4()
    example5()
