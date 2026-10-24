"""
协程基础与并发实验

【实验目的】
1. 理解 async def 定义协程，await 挂起等待。
2. 对比 "串行 await" 与 "并发 create_task + gather" 的耗时差异。
3. 理解事件循环是如何调度多个任务的。

【核心结论】
- 串行耗时 = 所有任务耗时之和 (1s + 2s = 3s)
- 并发耗时 = 最长任务的耗时 (max(1s, 2s) = 2s)
"""

import asyncio
import time

from loguru import logger


async def do_task(name: str, delay: int):
    logger.info(f"任务 {name} 开始...")
    await asyncio.sleep(delay)
    # await asyncio.to_thread(time.sleep, delay)
    logger.info(f"任务 {name} 完成.")
    return {"TASK": name}


async def main_serial():
    """直接 await，必须等上一个跑完，才跑下一个"""
    logger.info("--- 串行执行（预期总耗时 1s + 2s = 3s）---")
    await do_task("A", 1)
    await do_task("B", 2)


def test_serial():
    start_time = time.perf_counter()
    asyncio.run(main_serial(), debug=True)
    logger.info(f"串行总耗时: {time.perf_counter() - start_time:.2f} 秒\n")


# ------------------------------------------------------------------------


async def main_concurrent():
    """使用 create_task 包装。包装完它立刻就在后台开始跑了，不会卡在这里"""
    logger.info("--- 并发执行（预期总耗时 max(1s, 2s) = 2s）---")
    task_A = asyncio.create_task(do_task("A", 1))
    task_B = asyncio.create_task(do_task("B", 2))
    results = await asyncio.gather(task_A, task_B)
    print(results)


def test_concurrent():
    start_time = time.perf_counter()
    asyncio.run(main_concurrent(), debug=True)
    logger.info(f"并发总耗时: {time.perf_counter() - start_time:.2f} 秒")


if __name__ == "__main__":
    test_serial()
    print("_" * 95, end="\n\n")
    test_concurrent()
