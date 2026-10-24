import os
from threading import Thread, current_thread, get_native_id

from loguru import logger


def do_something():
    logger.info(
        f"当前线程{current_thread().name} tid={get_native_id()} pid={os.getpid()}"
    )


if __name__ == "__main__":
    for i in range(10):
        Thread(target=do_something, name=f"thread-{i}").start()

"""
2026-10-23 18:07:13.925 | INFO     | __main__:do_something:8 - 当前线程thread-0 tid=17956 pid=12404
2026-10-23 18:07:13.926 | INFO     | __main__:do_something:8 - 当前线程thread-1 tid=8040 pid=12404
2026-10-23 18:07:13.926 | INFO     | __main__:do_something:8 - 当前线程thread-2 tid=4796 pid=12404
2026-10-23 18:07:13.926 | INFO     | __main__:do_something:8 - 当前线程thread-3 tid=19292 pid=12404
2026-10-23 18:07:13.926 | INFO     | __main__:do_something:8 - 当前线程thread-4 tid=14384 pid=12404
2026-10-23 18:07:13.927 | INFO     | __main__:do_something:8 - 当前线程thread-5 tid=18124 pid=12404
2026-10-23 18:07:13.927 | INFO     | __main__:do_something:8 - 当前线程thread-6 tid=15044 pid=12404
2026-10-23 18:07:13.927 | INFO     | __main__:do_something:8 - 当前线程thread-7 tid=10500 pid=12404
2026-10-23 18:07:13.927 | INFO     | __main__:do_something:8 - 当前线程thread-8 tid=15848 pid=12404
2026-10-23 18:07:13.928 | INFO     | __main__:do_something:8 - 当前线程thread-9 tid=3920 pid=12404
"""
