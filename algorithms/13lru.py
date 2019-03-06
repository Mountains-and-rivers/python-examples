"""lru（Least Recently Used，最近最少使用算法）的 Python 实现。"""

from collections import OrderedDict


class MyLruCache:

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
            # 将命中缓存移到队列最后（更新顺序）
            self._cache.move_to_end(key)
            return self._cache[key]

    def put(self, key, value):
        if key not in self._cache and len(self._cache) == self.capacity:
            # 移除最早加入（队列最前）的缓存
            self._cache.popitem(last=False)
        if key in self._cache:
            # 缓存更新后，也更新其在队列位置
            self._cache.move_to_end(key)
        self._cache[key] = value


def main() -> None:
    keys = ['green', 'red', 'blue', 'yellow', 'black', 'green']
    cache = MyLruCache(5)
    for i, key in enumerate(keys):
        cache.put(key, i)

    print(cache)


if __name__ == '__main__':
    main()
