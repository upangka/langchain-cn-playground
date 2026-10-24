"""
同步 requests 与 异步 aiohttp 网络请求对比实战 (Unit 1.7)

【实验目的】
1. 直观对比同步阻塞和异步非阻塞在网络 I/O 上的耗时差异。
2. 体验 asyncio.gather 并发发起多个网络请求。

【实验结论】（基于 Bilibili 进行 10 次连续请求）
- 同步 (requests): 总耗时约 1.21 秒。请求严格串行，一个接一个阻塞执行。
- 异步 (aiohttp) : 总耗时约 0.17 秒。10 个请求瞬间全部发出，并发执行。

【核心启示】
在 I/O 密集型任务（如网络请求、数据库查询）中，异步能带来十倍甚至百倍的性能提升。
这也是现代大模型应用（如 FastAPI 调用大模型 API）必须使用异步的核心原因。
"""

import asyncio
import time

import aiohttp
import requests
from loguru import logger


def fetch_sync(urls: list[str]) -> list[int]:
    """同步阻塞版请求，使用 requests 库依次请求 URL。

    Args:
        urls: 待请求的 URL 列表。

    Returns:
        包含每个网页响应内容长度的列表。
    """
    results = []
    for index, url in enumerate(urls):
        index += 1
        logger.debug(f"[同步] 开始请求: {index}")
        start = time.perf_counter()
        # 同步请求会死等，直到服务器响应
        response = requests.get(url)
        results.append(len(response.text))
        cost = time.perf_counter() - start
        logger.debug(f"[同步] 完成请求: {index} (耗时 {cost:.2f}秒)")
    return results


async def fetch_async(session: aiohttp.ClientSession, url: str, index: int) -> int:
    """异步非阻塞版请求，使用 aiohttp 库请求单个 URL。

    Args:
        session: 共享的 aiohttp 会话对象。
        url: 待请求的 URL。
        index: 序列

    Returns:
        网页响应内容的长度。
    """
    logger.debug(f"[异步] 开始请求: {index}")
    start = time.perf_counter()
    async with session.get(url) as response:
        text = await response.text()
    cost = time.perf_counter() - start
    logger.debug(f"[异步] 完成请求: {index} (耗时 {cost:.2f}秒)")
    return len(text)


def main_sync(target_url):
    """同步测试"""
    start_sync = time.perf_counter()
    try:
        fetch_sync([target_url] * 10)
    except Exception as e:
        logger.error(f"同步请求失败（可能是网络问题）: {e}")
    cost_sync = time.perf_counter() - start_sync
    logger.info(f">>>>> 【同步请求】总耗时: {cost_sync:.2f} 秒 <<<<<")


async def main_async(target_url):
    """异步测试"""
    start_async = time.perf_counter()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_async(session, target_url, i + 1) for i in range(10)]
        await asyncio.gather(*tasks)
    cost_async = time.perf_counter() - start_async
    logger.info(f">>>>> 【异步请求】总耗时: {cost_async:.2f} 秒 <<<<<")


if __name__ == "__main__":
    # target_url = "https://httpbin.org/anything"
    target_url = "https://www.bilibili.com/"
    main_sync(target_url)
    print("_" * 100, end="\n\n")
    asyncio.run(main_async(target_url))
