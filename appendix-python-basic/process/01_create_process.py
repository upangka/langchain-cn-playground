"""
创建进程的方式
"""

import os
from multiprocessing import Process, current_process

from loguru import logger


def learning_and_coding(username: str, course: str, **kwargs):
    logger.info(f"当前PID: {os.getpid()} {current_process()}")
    logger.info(f"{username} learning {course} {kwargs}")


if __name__ == "__main__":
    logger.info(f"启动进程 {os.getpid()}")
    p1 = Process(
        target=learning_and_coding,
        args=("鲨鱼のBlue", "Python"),
        kwargs={"year": 2026, "website": "Bilibili"},
    )
    p2 = Process(
        target=learning_and_coding,
        args=("Pkmer", "Java"),
        kwargs={"year": 2026, "website": "Bilibili"},
    )
    p1.start()
    p2.start()
