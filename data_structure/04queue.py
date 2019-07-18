"""Queue 常用于线程间共享数据，或作为任务队列。

可以设置 Queue 的最大大小。

一般情况下，
当 Queue 满时，`put()` 会阻塞等待，而不是覆盖，覆盖是 deque 的特性；
当 Queue 空时，`get()` 会阻塞等待。

`put()` 和 `get()` 可以通过属性 block 设置非阻塞，
非阻塞情况下，
`put()` 为满，则抛出 Full 异常；
`get()` 为空，则抛出 Empty 异常。
"""

from queue import Queue, Full, Empty


def main():
    q = Queue(maxsize=5)
    for i in range(10):
        try:
            # `block=False` 不阻塞等待
            q.put(i, block=False)
        except Full:
            print('Full')
            break

    print('*' * 50)

    while True:
        try:
            i = q.get(block=False)
            print(i)
        except Empty:
            print('Empty')
            break


if __name__ == '__main__':
    main()
