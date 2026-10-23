import time
from multiprocessing import Process, RLock
from multiprocessing.synchronize import RLock as RLockType

from loguru import logger


def study(lock: RLockType):
    for _ in range(5):
        with lock:
            logger.info("枫叶")
            logger.info("荻花")
            logger.info("秋瑟瑟")
            time.sleep(1)


def speak(lock: RLockType):
    for _ in range(5):
        with lock:
            logger.info("hello")
            logger.info("world")
            logger.info("Java")
            logger.info("Python")
            time.sleep(1)


if __name__ == "__main__":
    lock = RLock()
    p1 = Process(target=study, args=(lock,))
    p2 = Process(target=speak, args=(lock,))
    p1.start()
    p2.start()
