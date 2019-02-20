from queue import Queue
from threading import Thread


class Worker(Thread):

    def __init__(self, queue):
        super().__init__(daemon=True)
        self._q = queue
        self.start()

    def run(self):
        while True:
            func, args, kwargs = self._q.get()
            try:
                print(func(*args, **kwargs))
            except Exception as e:
                print(e)
                self._q.task_done()


class ThreadPool:
    def __init__(self, num_t=5):
        self._q = Queue(num_t)

        # Create Worker Thread
        for _ in range(num_t):
            Worker(self._q)

    def add_task(self, func, *args, **kwargs):
        self._q.put((func, args, kwargs))

    def wait_complete(self):
        self._q.join()


def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)


def main() -> None:
    pool = ThreadPool()
    for _ in range(3):
        pool.add_task(fib, 35)
    pool.wait_complete()


if __name__ == '__main__':
    main()
