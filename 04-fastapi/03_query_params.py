"""
FastAPI 查询参数与 Pydantic 对象封装

【实验目的】
1. 区分路径参数（URL 的一部分）和查询参数（URL ? 后面的键值对）。
2. 掌握查询参数的默认值设置。
3. 掌握可选查询参数（设置默认值为 None）。
4. 对比传统写法（参数散落）与优雅写法（Pydantic 对象封装 + Annotated）。
"""

from typing import Annotated

import uvicorn
from fastapi import FastAPI, Query
from loguru import logger
from pydantic import BaseModel


class ItemQuery(BaseModel):
    q: str | None = Query(None, description="搜索关键词")
    short: bool = Query(False, description="是否简短")


app = FastAPI()

# 模拟一个商品列表
items_list = [{"item1": "Foo"}, {"item2": "Bar"}, {"item3": "Baz"}, {"item4": "Qux"}]


@app.get("/items/")
async def read_items(start: int = 0, limit: int = 10):
    """带默认值的查询参数

    请求示例: http://127.0.0.1:8000/items/?start=1&limit=2
    """
    logger.info(f"收到查询参数请求: start={start}, limit={limit}")

    # 利用 Python 切片，根据 start 和 limit 返回数据
    result = items_list[start : start + limit]
    logger.debug(f"切片返回结果: {result}")
    return result


@app.get("/users/{user_id}/items/{item_id}/v1")
async def read_user_item_v1(
    item_id: str,
    user_id: int,
    q: str | None = None,
    short: bool = False,
):
    """混合路径参数和查询参数

    请求示例: http://127.0.0.1:8000/users/100/items/500/v1?q=test&short=true
    """
    logger.info(
        f"收到混合参数请求: user_id={user_id}, item_id={item_id}, q={q}, short={short}"
    )

    item = {"item_id": item_id, "owner_id": user_id}

    # 如果传了 q，就加到返回值里
    if q:
        item.update({"q": q})

    # 如果 short 是 False（默认），就加上描述信息
    if not short:
        item.update({"description": "这是一个很长很长的商品描述信息..."})

    logger.debug(f"最终返回的数据: {item}")
    return item


@app.get("/users/{user_id}/items/{item_id}/v2")
async def read_user_item_v2(
    user_id: int, item_id: str, query: Annotated[ItemQuery, Query()]
):
    """混合路径参数和查询参数 (Pydantic 对象封装写法)

    请求示例: http://127.0.0.1:8000/users/100/items/500/v2?q=test&short=true
    """
    # 打印接收到的路径参数
    logger.info(f"接收到路径参数: user_id={user_id}, item_id={item_id}")

    # 打印组装好的查询参数对象，你可以直观看到 FastAPI 是怎么把 URL 变成对象的
    logger.debug(f"组装好的查询参数对象: {query}")

    # 你可以把 query 当成一个对象来用
    item = {"item_id": item_id, "owner_id": user_id}
    if query.q:
        item.update({"q": query.q})
    if not query.short:
        item.update({"description": "详细描述"})
    return item


if __name__ == "__main__":
    uvicorn.run(app="03_query_params:app", host="127.0.0.1", port=8000, reload=True)
