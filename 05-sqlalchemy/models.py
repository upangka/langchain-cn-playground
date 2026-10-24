"""
ORM 模型定义 (Unit 3.4)
"""

from base import Base
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class Department(Base):
    """部门模型（一对多：一个部门包含多个员工）"""

    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)  # 部门名称
    location = Column(String(100))  # 部门位置

    # 一对多关联员工：返回员工列表
    employees = relationship("Employee", back_populates="department")


class Employee(Base):
    """员工模型（多对一：多个员工属于一个部门）"""

    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)  # 姓名
    age = Column(Integer, comment="员工年龄")  # 年龄
    hire_date = Column(Date)  # 入职日期

    # 添加外键约束，绑定到 departments.id
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=False)

    # 多对一关联部门：返回单个部门对象
    department = relationship("Department", back_populates="employees")
