import time
from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


def main() -> None:
    s = time.time()
    print(fib(50))
    e = time.time()
    print(e - s)


if __name__ == '__main__':
    main()
