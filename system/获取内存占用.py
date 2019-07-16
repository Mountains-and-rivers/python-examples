#!/usr/bin/env python3

import resource
import platform
import functools


def profile_mem(func):
    @functools.wraps(func)
    def wrapper(*a, **k):
        s = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        ret = func(*a, **k)
        e = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

        uname = platform.system()
        if uname == "Linux":
            print(f"mem usage: {e - s} kByte")
        elif uname == "Darwin":
            print(f"mem usage: {e - s} Byte")
        else:
            raise Exception("not support")
        return ret
    return wrapper


class S(object):
    __slots__ = ['attr1', 'attr2', 'attr3']

    def __init__(self):
        self.attr1 = "Foo"
        self.attr2 = "Bar"
        self.attr3 = "Baz"


class D(object):

    def __init__(self):
        self.attr1 = "Foo"
        self.attr2 = "Bar"
        self.attr3 = "Baz"


@profile_mem
def alloc(cls):
    _ = [cls() for _ in range(1000000)]


def main() -> None:
    alloc(S)
    alloc(D)


if __name__ == '__main__':
    main()
