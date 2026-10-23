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


if __name__ == "__main__":
    process_pool = ProcessPoolExecutor(max_workers=3)
    futures = []
    for i in range(1, 11):
        futures += [process_pool.submit(worker, i)]

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

    logger.info("MAIN OVER")


"""
15:29:36| INFO | __mp_main__:worker:13 - task-1 被分配到 17996 执行
15:29:36| INFO | __mp_main__:worker:13 - task-2 被分配到 788 执行
15:29:37| INFO | __mp_main__:worker:13 - task-4 被分配到 17996 执行
15:29:37| INFO | __mp_main__:worker:13 - task-3 被分配到 16572 执行
15:29:37| INFO | __mp_main__:worker:13 - task-5 被分配到 788 执行
15:29:38| INFO | __mp_main__:worker:13 - task-6 被分配到 17996 执行
15:29:38| INFO | __mp_main__:worker:13 - task-8 被分配到 788 执行
15:29:38| INFO | __mp_main__:worker:13 - task-9 被分配到 17996 执行
15:29:38| INFO | __mp_main__:worker:13 - task-7 被分配到 16572 执行
15:29:39| INFO | __mp_main__:worker:13 - task-10 被分配到 788 执行
15:29:39| INFO | __main__:<module>:31 - === 任务统计结果 ===
15:29:39| INFO | __main__:<module>:33 - PID: 17996 -> 处理任务: [1, 4, 6, 9]
15:29:39| INFO | __main__:<module>:33 - PID: 788 -> 处理任务: [2, 5, 8, 10]
15:29:39| INFO | __main__:<module>:33 - PID: 16572 -> 处理任务: [3, 7]
15:29:39| INFO | __main__:<module>:34 - MAIN OVER
"""
