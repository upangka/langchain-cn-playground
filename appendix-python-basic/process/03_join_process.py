"""
join 方法的作用：阻塞当前进程，等 join 前面的进程执行完，再继续往下执行。
join(timeout)，其中 timeout 是可选参数，表示等多久，单位是秒。

注意点：
  1.p.join() 不是让进程 p 等，而是让“执行这行 join 代码的那个进程”去等，等的是 p 这个进程。
  2.当达到了 timeout 所指定的时间后，进程并不会终止，只是“不再等”了。
  3.join 必须在 start 之后



2026-10-23 13:18:01.647 | INFO     | __main__:<module>:22 - 【主进程开始】
2026-10-23 13:18:03.829 | INFO     | __mp_main__:do_some_work:18 - Process-1 finished work total: seconds=2
2026-10-23 13:18:03.870 | INFO     | __main__:<module>:27 - 【准备启动第二个进程】
2026-10-23 13:18:06.880 | INFO     | __main__:<module>:30 - 【主进程结束】
2026-10-23 13:18:09.057 | INFO     | __mp_main__:do_some_work:18 - Process-2 finished work total: seconds=5
"""

import time
from multiprocessing import Process, current_process

from loguru import logger


def do_some_work(seconds: int):
    time.sleep(seconds)
    logger.info(f"{current_process().name} finished work total: {seconds=}")


if __name__ == "__main__":
    logger.info("【主进程开始】")
    p1 = Process(target=do_some_work, args=(2,))
    p2 = Process(target=do_some_work, args=(5,))
    p1.start()
    p1.join(3)
    logger.info("【准备启动第二个进程】")
    p2.start()
    p2.join(3)
    logger.info("【主进程结束】")
