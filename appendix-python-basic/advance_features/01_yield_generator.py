"""
生成器
"""

from loguru import logger


def my_generator():
    logger.info("1. 准备数据（打开连接）")
    yield "给你用的数据"  # 挂起，把值交出去
    logger.info("3. 收尾清理（关闭连接）")


if __name__ == "__main__":
    # 获取生成器对象（此时函数还没执行）
    gen = my_generator()

    # 第一次调用 next()，执行到 yield 暂停
    data = next(gen)
    logger.info(f"2. 拿到数据并处理: {data}")

    # 再次调用 next()，函数从 yield 处恢复，执行后面的清理代码
    try:
        next(gen)
    except StopIteration:
        logger.info("4. 函数执行完毕")
