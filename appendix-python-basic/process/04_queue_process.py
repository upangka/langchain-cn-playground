"""
Queue put具有等待阻塞的性质

2026-10-23 13:35:41.342 | INFO     | __main__:<module>:24 - 准备添加新元素
2026-10-23 13:35:44.608 | INFO     | __mp_main__:consume_item:13 - 取出Java
2026-10-23 13:35:44.608 | INFO     | __main__:<module>:26 - 完成添加新元素
"""

import time
from multiprocessing import Process, Queue

from loguru import logger


def consume_item(queue: Queue):
    time.sleep(3)
    logger.info(f"取出{queue.get()}")


if __name__ == "__main__":
    queue = Queue(2)
    queue.put("Java")
    queue.put("Python")
    logger.info(f"当前队列满? {queue.full()}")

    Process(target=consume_item, args=(queue,)).start()

    logger.info("准备添加新元素")
    queue.put("LangChain")
    logger.info("完成添加新元素")
