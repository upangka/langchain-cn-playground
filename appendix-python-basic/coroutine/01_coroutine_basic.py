"""
协程基础与同步阻塞验证

【实验目的】
1. 理解 async def 定义的是协程函数，调用它不会立即执行，而是返回一个协程对象 (coroutine)。
2. 理解必须把协程对象交给事件循环（asyncio.run）才能真正执行。
3. 理解 await 的作用：遇到 await 时挂起当前协程，让出 CPU 控制权。
4. 观察 asyncio.run() 的阻塞特性。

【核心结论】
- 直接调用 hello() 只会返回 <class 'coroutine'>，内部代码一行都不会执行。
- 如果漏写 await（写成 asyncio.sleep），程序不会等待，并抛出 RuntimeWarning。
- asyncio.run() 会阻塞主线程，直到传入的协程完全执行结束才继续往下走。
"""

import asyncio

from loguru import logger


async def hello():
    logger.info("START hello")
    await asyncio.sleep(2)
    logger.info("END hello")


if __name__ == "__main__":
    coro_obj = hello()
    print(type(coro_obj))
    asyncio.run(coro_obj, debug=True)
    logger.info("MAIN END")
