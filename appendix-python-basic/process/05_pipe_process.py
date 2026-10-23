"""
在 AI Agent 开发中，主 Agent（Main Agent）通常负责接收用户请求、分发任务、汇总结果；
子 Agent（Sub Agent）负责具体执行耗时的工具调用或子任务。

利用 Pipe 把这个过程模拟出来： 一个“主 Agent 派发任务给 2 个子 Agent 并收集结果”
"""

import random
import time
from multiprocessing import Pipe, Process
from multiprocessing.connection import Connection

from loguru import logger


def sub_agent(agent_name: str, conn: Connection):
    """
    子 Agent：负责接收主 Agent 的任务，并返回执行结果
    """
    logger.info(f"spawn {agent_name}成功")

    while True:
        task = conn.recv()
        if task is None:
            break
        logger.info(f"[{agent_name}] 收到任务: 正在处理 -> {task}")
        # 模拟执行时间
        time.sleep(random.uniform(3, 7))
        conn.send(f"【{agent_name} 汇报】任务 '{task}' 已完成，结果数据正常。")

    conn.close()
    logger.info(f"{agent_name} exist success")


def main_agent():
    logger.info("【主agent已经启动】")

    main_conn_1, child_conn_1 = Pipe()
    main_conn_2, child_conn_2 = Pipe()

    sub_agent_1 = Process(target=sub_agent, args=("Sub-Agent (数据分析)", child_conn_1))
    sub_agent_2 = Process(target=sub_agent, args=("Sub-Agent (网络搜索)", child_conn_2))
    sub_agent_1.start()
    sub_agent_2.start()

    main_conn_1.send("分析最近一周的销售数据")
    main_conn_2.send("搜索一下最新的 Python 3.13 特性")

    result_1 = main_conn_1.recv()
    logger.info(f"[Main Agent] 收到报告: {result_1}")
    result_2 = main_conn_2.recv()
    logger.info(f"[Main Agent] 收到报告: {result_2}")

    main_conn_1.send(None)
    main_conn_2.send(None)

    sub_agent_1.join()
    sub_agent_2.join()

    main_conn_1.close()
    main_conn_2.close()
    logger.info("【主agent结束】")


if __name__ == "__main__":
    main_agent()
