"""打印函数运行时间。

Create:   2018-11-14
Modified:
"""

import time
import functools


def finished(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            pass
        finally:
            print('\n[Finished in %.8fs]\n' % (time.perf_counter() - start))
    return wrapper
