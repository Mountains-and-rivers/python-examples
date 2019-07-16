"""LRU（Least Recently Used，最近最少使用算法）的 Python 实现。"""

import socket
import time
from urllib.request import urlopen
from collections import OrderedDict


class MyLruCache1:
    """这种在方法中判断 key 是否存在的实现并不好。"""

    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = OrderedDict()

    def __contains__(self, key):
        return key in self._cache

    def __len__(self):
        return len(self._cache)

    def __str__(self):
        return str(self._cache)

    def __repr__(self):
        return str(self._cache)

    def get(self, key):
        if key in self._cache:
            # **注意** 不要将命中缓存移到队列最后（更新顺序）
            # 这样会导致缓存永不更新
            # self._cache.move_to_end(key)
            return self._cache[key]

    def put(self, key, value):
        if key not in self._cache and len(self._cache) == self.capacity:
            # 移除最早加入（队列最前）的缓存
            self._cache.popitem(last=False)
        if key in self._cache:
            # 缓存更新后，也更新其在队列位置
            self._cache.move_to_end(key)
        self._cache[key] = value


class MyLruCache2:
    """把 key 是否已经存在的工作交给调用者，这种实现更好，
    否则 MyLruCache1 的实现方法，还得判断返回的 key 是否为 None
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self._cache = OrderedDict()

    def __contains__(self, key):
        return key in self._cache

    def __len__(self):
        return len(self._cache)

    def __str__(self):
        return str(self._cache)

    def __repr__(self):
        return str(self._cache)

    def __getitem__(self, key):
        return self._cache[key]

    def __setitem__(self, key, value):
        if len(self._cache) == self.capacity:
            # 移除最早加入（队列最前）的缓存
            self._cache.popitem(last=False)
        self._cache[key] = value

    def clear(self):
        self._cache.clear()


_dnscache = MyLruCache2(1024)

_getaddrinfo_nocache = socket.getaddrinfo


def _getaddrinfo(*args, **kwargs):
    if args in _dnscache:
        print('使用缓存。')
        return _dnscache[args]
    else:
        _dnscache[args] = _getaddrinfo_nocache(*args, **kwargs)
        print('创建缓存。')
        return _dnscache[args]


# 替换掉原有方法
socket.getaddrinfo = _getaddrinfo


def get_html(ip):
    url = f'http://m.ip138.com/ip.asp?ip={ip}'
    with urlopen(url) as response:
        return response.read().decode('utf-8')


def main():
    ip = '192.168.1.1'

    while True:
        get_html(ip)
        time.sleep(2)


if __name__ == '__main__':
    main()
