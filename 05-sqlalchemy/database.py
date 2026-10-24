"""
数据库连接配置
"""

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv(override=True)

# 创建引擎
engine = create_engine(
    os.environ["DATABASE_URL"],
    echo=True,  # 打印执行的 SQL，方便调试
    pool_pre_ping=True,  # 连接前检查有效性
)

# 创建会话工厂
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
