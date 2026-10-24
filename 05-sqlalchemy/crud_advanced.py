"""
数据库高级操作：修改、删除与查询 (Unit 3.6 & 3.7)

【实验目的】
1. 掌握修改数据（直接改属性 + commit）。
2. 掌握删除数据（db.delete + commit）。
3. 掌握常见查询：过滤 filter、逻辑运算 and_/or_、表连接 join、预加载 joinedload。
"""

from database import SessionLocal
from loguru import logger
from models import Department, Employee
from sqlalchemy import and_, or_
from sqlalchemy.orm import joinedload


def update_data():
    """修改数据"""
    db = SessionLocal()
    try:
        # 1. 先查出来
        emp = db.query(Employee).filter(Employee.name == "张三").first()
        if emp:
            # 2. 直接修改属性
            emp.age = 31
            # 3. 提交更改
            db.commit()
            logger.info(f"修改成功：张三的年龄更新为 {emp.age}")
    finally:
        db.close()


def delete_data():
    """删除数据"""
    db = SessionLocal()
    try:
        # 1. 查出来（比如删除李四）
        emp = db.query(Employee).filter(Employee.name == "李四").first()
        if emp:
            # 2. 从数据库会话中删除
            db.delete(emp)
            db.commit()
            logger.info("删除成功：李四已被移除")
    finally:
        db.close()


def read_data():
    """各种查询姿势"""
    db = SessionLocal()
    try:
        logger.info("--- 1. 基础过滤 filter ---")
        # 查询研发部（department_id=1）的所有员工
        rd_emps = db.query(Employee).filter(Employee.department_id == 1).all()
        logger.info(f"研发部员工: {[e.name for e in rd_emps]}")

        logger.info("--- 2. 逻辑运算 (and_ / or_) ---")
        # 查询年龄在 25 到 35 之间，且属于研发部的员工
        emp_and = (
            db.query(Employee)
            .filter(and_(Employee.age.between(25, 35), Employee.department_id == 1))
            .first()
        )
        if emp_and:
            logger.info(f"符合 and 条件的员工: {emp_and.name}")

        logger.info("--- 3. 表连接 join ---")
        # 查询员工及其部门名称（显式 join）
        results = (
            db.query(Employee, Department)
            .join(Department, Employee.department_id == Department.id)
            .all()
        )
        for emp, dept in results:
            logger.info(f"员工 {emp.name} 属于 {dept.name}")

        logger.info("--- 4. 预加载 joinedload (解决 N+1 问题) ---")
        # 一次性把员工和部门数据全部查出来，避免循环查库
        emps = db.query(Employee).options(joinedload(Employee.department)).all()
        for e in emps:
            # 此时访问 e.department 不会触发新的 SQL 查询
            logger.info(f"预加载查询: {e.name} -> {e.department.name}")

    finally:
        db.close()


if __name__ == "__main__":
    logger.info("=== 开始执行修改 ===")
    update_data()

    logger.info("=== 开始执行删除 ===")
    delete_data()

    logger.info("=== 开始执行查询 ===")
    read_data()
