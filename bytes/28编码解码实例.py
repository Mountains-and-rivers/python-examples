#!/usr/bin/env python3
# coding: utf-8

"""多种编码的应对方式"""

import json
import re
import struct


def example1():
    """utf-8 编码解码，可变长，英文占一个字节，中文都是占三个字节"""

    # 无法显示为 ascii 的字符都以 \x## 显示
    b = b'\xe5\x92\x95\xe5\x92\x95\xe5\xa4\xaa\xe7\xa1\xac\xe4\xba\x86'
    # 默认使用 utf-8
    print(b.decode())

    # 注意单引号前少了 b，这时先转成 bytes 类型再处理
    s2 = '\xe5\x92\x95\xe5\x92\x95\xe5\xa4\xaa\xe7\xa1\xac\xe4\xba\x86'
    b2 = struct.pack(f'{len(s2)}B', *[ord(c) for c in s2])
    print(b2)
    print(b2.decode())


def example2():
    """unicode 编码解码，长度固定，所有字符都占两个字节。

    unicode 编码是内存中字符的编码，跟文本中的编码不一样，
    以 Litte-Endian 形式存放，
    即 A 的 unicode 的编号虽然是00000000 01000001，
    但在内存中从小地址到大地址是这样存放的 01000001 00000000，
    数字也是如此，即超过一字节的数字都以 Litte-Endian 形式存放。
    """

    print(hex(ord('咕')))  # 0x5495
    # 能解析成可见字符时，会自动解析
    print('\u5495')

    print('\u5495\u5495\u592a\u786c\u4e86')


def example3():
    """把十六进制数字组成的字符串转换成 utf-8"""

    # s 是 wireshark 中用 Hex Stream 复制出来的一段十六进制数字组成的字符串
    s = 'a0000000a0000000b202000074797065403d636861746d' \
        '73672f726964403d3233313535342f756964403d393731' \
        '373239372f6e6e403d323731323336306162632f74787440' \
        '3de59295e59295e5a4aae7a1ace4ba862f636964403d32' \
        '6265666432393665383035346364346630303630623030303030' \
        '30303030302f6963403d61766174617240' \
        '5364656661756c74405330362f6c6576656c403d332f656c403d2f00'

    # 两种转换方式
    # b = int(s, 16).to_bytes(len(s) // 2, 'big')
    b = bytes.fromhex(s)  # 显然更好

    # 提取出信息
    pattern = re.compile(b'type@=chatmsg/.+?/nn@=(.+?)/txt@=(.+?)/.+?/level@=(.+?)/')
    for nn, txt, level in pattern.findall(b):
        print('[lv.{:0<2}][{}]: {}'.format(level.decode(), nn.decode(), txt.decode().strip()))


def example4():
    """处理'\\uxxxx'形式的字符串"""

    # 一段非常规的 unicode 字符串
    s = '\\u5495\\u5495\\u592a\\u786c\\u4e86'
    pattern = re.compile(r'\\u\w{4}')
    s2 = pattern.sub(lambda x: chr(int(x.group(0).replace('\\u', ''), 16)), s)
    # 另一种，使用 `json.loads()`，更好
    s2 = json.loads(f'"{s2}"')
    print(s2)

    # 另一种形式，多两个单引号
    s = ascii('咕咕太硬了')  # "'\\u5495\\u5495\\u592a\\u786c\\u4e86'"
    print(s)
    print(eval(s))


if __name__ == '__main__':
    example1()
    print('*' * 50)
    example2()
    print('*' * 50)
    example3()
    print('*' * 50)
    example4()
    print('*' * 50)
