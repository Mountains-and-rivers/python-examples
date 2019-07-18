"""
base64 编码将 8 位的单字节转换成 ASCII 范围内可打印的字符值，
来兼容那些只支持 ASCII 编码数据的系统，
代价是使用更多的位来表示数据，比如 SMTP 。
base 的值表示每个字母在编码中所需要的相应的长度。
一些使用略有不同的字母表，但仍然是 URL - 安全的原编码系统的变种也是存在的。
"""

import base64


def main() -> None:
    s = '你好'.encode()
    print(s)
    # 编码成 base64
    s_b64 = base64.b64encode(s)
    print(s_b64)
    # 解码
    print(base64.b64decode(s_b64))


if __name__ == '__main__':
    main()
