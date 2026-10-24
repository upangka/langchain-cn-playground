"""
在协程中：asyncio.gather(*任务生成器) 是你以后并发跑多个协程最常用的标准姿势。
* 的作用：把列表、元组、生成器拆成独立的位置参数。

公式：函数(*可迭代对象) 等价于 函数(元素1, 元素2, 元素3...)
"""

import asyncio


async def hi(): ...


task = asyncio.create_task(hi())
print(type(task), task)
