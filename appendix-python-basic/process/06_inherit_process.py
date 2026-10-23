"""
通过继承的方式实现process
"""

from multiprocessing import Process

from loguru import logger


class SubAgent(Process):
    def __init__(
        self, group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None
    ):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)

    def run(self):
        logger.info(f"{self.name}")


if __name__ == "__main__":
    sub_agent = SubAgent(name="RAG检索智能体")
    sub_agent.start()
