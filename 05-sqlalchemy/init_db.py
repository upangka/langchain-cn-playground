"""
一键建表脚本 (Unit 3.4)
"""

from base import Base
from database import engine
from loguru import logger

# ⚠️ 重点：必须导入模型类，否则 Base.metadata 不知道有哪些表要建！
from models import Department, Employee


def init_db():
    logger.info("正在向数据库发送建表指令...")
    # 故意打印一下，告诉 Ruff 我确实用到了这两个类
    logger.info(f"准备创建的表: {Department.__tablename__}, {Employee.__tablename__}")
    Base.metadata.create_all(bind=engine)
    logger.info("🎉 表创建成功！请去你的 MySQL 里看看 fastapi_db 库。")


if __name__ == "__main__":
    init_db()
