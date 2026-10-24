"""
新增数据操作 (Unit 3.5)

【实验目的】
1. 掌握 Session 的创建与关闭。
2. 掌握 db.add() / db.add_all() / db.commit() / db.refresh() 的用法。
3. 体验 relationship 在插入数据时的“双向绑定”魔法。
"""

from datetime import date

from database import SessionLocal
from loguru import logger
from models import Department, Employee


def insert_data():
    # 1. 获取数据库会话
    db = SessionLocal()

    try:
        # ==========================================
        # 第一步：新增部门
        # ==========================================
        new_dept = Department(name="研发部", location="北京总部")
        db.add(new_dept)
        db.commit()  # 提交到数据库执行 INSERT
        db.refresh(
            new_dept
        )  # 刷新对象，从数据库拿回自增的 id（此时 new_dept.id 就有值了）
        logger.info(f"新增部门：ID={new_dept.id}, 名称={new_dept.name}")

        # ==========================================
        # 第二步：新增员工（关联部门）
        # ==========================================
        # 方法 A：通过 department_id 显式指定外键
        emp1 = Employee(
            name="张三", age=30, hire_date=date(2023, 1, 1), department_id=new_dept.id
        )

        # 方法 B：使用 relationship 魔法（直接把部门对象赋给 department）
        # 因为配置了 back_populates，SQLAlchemy 会自动帮你把 department_id 填好
        emp2 = Employee(
            name="李四", age=28, hire_date=date(2023, 3, 15), department=new_dept
        )

        # 批量添加员工
        db.add_all([emp1, emp2])
        db.commit()

        # 刷新员工对象，获取自增 ID
        db.refresh(emp1)
        db.refresh(emp2)
        logger.info(f"新增员工 1：ID={emp1.id}, 姓名={emp1.name}")
        logger.info(f"新增员工 2：ID={emp2.id}, 姓名={emp2.name}")

        # ==========================================
        # 第三步：验证 relationship 的双向魔法
        # ==========================================
        logger.info("--- 验证关联关系 ---")

        # 从员工查部门
        logger.info(f"员工 {emp1.name} 的部门是: {emp1.department.name}")

        # 从部门查员工（注意：此时内存里的 new_dept.employees 可能是空的，
        # 因为之前的查询没有触发加载，我们重新查一次数据库看看）
        db.refresh(new_dept)
        logger.info(
            f"部门 {new_dept.name} 的员工列表: {[emp.name for emp in new_dept.employees]}"
        )

    except Exception as e:
        db.rollback()  # 出错则回滚事务
        logger.error(f"新增失败: {e}")
    finally:
        db.close()  # 无论如何，最后关闭会话


if __name__ == "__main__":
    insert_data()
