"""struct 处理字节类型。

非常适合解析文件头。

struct 的 pack 函数把任意数据类型变成 bytes：
struct.unpack(fmt, data)

unpack 把 bytes 变成相应的数据类型，返回元组：
struct.pack(fmt, data)

Character	Byte order
@	        native
=	        native
<	        little-endian
>	        big-endian
!	        network (= big-endian)

默认小端（little-endian），`<`。

Format	C Type	        Python type	        Standard size
x	    pad byte	    no value
c	    char	        bytes of length 1	    1
b	    signed char	    integer	                1
B	    unsigned char	integer	                1
?	    _Bool	        bool	                1
h	    short	        integer	                2
H	    unsigned short	integer	                2
i	    int	            integer	                4
I	    unsigned int	integer	                4
l	    long            integer             	4
L	    unsigned long	integer             	4
q	    long long	    integer	                8
Q	    unsigned ll 	integer	                8
n	    ssize_t	        integer                 8
N	    size_t	        integer                 8
f	    float	        float	                4
d	    double	        float	                8
s	    char[]	        bytes                   1
p	    char[]	        bytes                   1
P	    void *	        integer                 8

符号前可加数字代表多少个。
"""

import struct


def main() -> None:
    # struct 的 pack 函数把任意数据类型变成 bytes
    # 长度要一致
    b = struct.pack('I', 10240099)
    print(b)

    # 可以创建一个对象
    s = struct.Struct('<B')
    print(s.pack(0xff))
    print(s.unpack(b'a'))


if __name__ == '__main__':
    main()
