import time
import functools


def finished(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        except KeyboardInterrupt:
            pass
        finally:
            end = time.time()
            print('\n[Finished in %.8fs]\n' % (end - start))
    return wrapper
