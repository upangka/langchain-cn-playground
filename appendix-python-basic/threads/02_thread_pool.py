import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import current_thread, get_native_id

from loguru import logger


def dowork(task_id):
    logger.info(
        f"当前线程{current_thread().name} tid={get_native_id()} pid={os.getpid()} 执行任务{task_id=}"
    )
    return task_id


if __name__ == "__main__":
    results = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(dowork, i) for i in range(10)]

        for f in as_completed(futures):
            results.append(f.result())

    print(f"完成任务id顺序: {results}")


"""
2026-10-23 18:13:24.030 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_0 tid=17896 pid=18408 执行任务task_id=0
2026-10-23 18:13:24.030 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_0 tid=17896 pid=18408 执行任务task_id=1
2026-10-23 18:13:24.030 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_0 tid=17896 pid=18408 执行任务task_id=3
2026-10-23 18:13:24.031 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_1 tid=3508 pid=18408 执行任务task_id=2
2026-10-23 18:13:24.031 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_3 tid=18912 pid=18408 执行任务task_id=5
2026-10-23 18:13:24.031 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_3 tid=18912 pid=18408 执行任务task_id=8
2026-10-23 18:13:24.032 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_4 tid=6204 pid=18408 执行任务task_id=9
2026-10-23 18:13:24.031 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_0 tid=17896 pid=18408 执行任务task_id=6
2026-10-23 18:13:24.031 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_2 tid=16048 pid=18408 执行任务task_id=4
2026-10-23 18:13:24.031 | INFO     | __main__:dowork:9 - 当前线程ThreadPoolExecutor-0_1 tid=3508 pid=18408 执行任务task_id=7
完成任务id顺序: [3, 2, 1, 0, 5, 8, 9, 6, 4, 7]
"""
