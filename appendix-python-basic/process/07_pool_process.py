import os
import random
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor, as_completed

from loguru import logger


def worker(task_id: int) -> tuple[int, int]:
    time.sleep(random.uniform(0.5, 2))
    pid = os.getpid()
    logger.info(f"task-{task_id} 被分配到 {pid} 执行")
    return pid, task_id


def done_cb(f):
    # print(type(f), f.result())
    pid, task_id = f.result()
    logger.info(f"进程[{pid}] 完成task-{task_id}")


def demo1():
    """演示
    1. 进程池ProcessPoolExecutor
    2. Future
    3. as_completed
    4. call back function: add_done_callback
    """
    process_pool = ProcessPoolExecutor(max_workers=3)
    futures = []
    for i in range(1, 11):
        f = process_pool.submit(worker, i)
        f.add_done_callback(done_cb)
        futures.append(f)

    # 统计每个pid都执行了哪些task
    pid_stats = defaultdict(list)
    for future in as_completed(futures):
        pid, task_id = future.result()
        pid_stats[pid].append(task_id)

    process_pool.shutdown(wait=True)
    # 打印统计结果
    logger.info("=== 任务统计结果 ===")
    for pid, task_ids in pid_stats.items():
        logger.info(f"PID: {pid} -> 处理任务: {task_ids}")

    logger.info("DEMO1 OVER")


def demo2():
    """演示
    1. map
    2. 得到的结果是严格按照顺序的
    [(8384, 1), (5960, 2), (16524, 3), (8384, 4), (16524, 5), (5960, 6), (8384, 7), (5960, 8), (8384, 9), (16524, 10)]
    """
    process_pool = ProcessPoolExecutor(max_workers=3)

    results = process_pool.map(worker, [i for i in range(1, 11)])
    logger.info(f"{results=}")

    # 遍历生成器获得真实的结果
    final_data = list(results)
    logger.info(f"最终的结果: {final_data}")

    process_pool.shutdown(wait=True)
    logger.info("DEMO2 OVER")


def demo3():
    """演示
    1. with block 优化demo2
    """
    with ProcessPoolExecutor(max_workers=3) as process_pool:
        results = process_pool.map(worker, [i for i in range(1, 11)])
        logger.info(f"{results=}")

        # 遍历生成器获得真实的结果
        final_data = list(results)
        logger.info(f"最终的结果: {final_data}")

    logger.info("DEMO3 OVER")


if __name__ == "__main__":
    # demo1()
    # demo2()
    demo3()
