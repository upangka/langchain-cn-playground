"""
FastAPI 请求体与参数混合使用 (Unit 2.6)

【实验目的】
1. 学会使用 Pydantic BaseModel 定义请求体（类似 Java 的 DTO）。
2. 掌握路径参数与请求体（JSON）在同一个接口中混合使用。
3. 理解 FastAPI 是如何自动区分参数的（路径 vs 请求体）。

【FastAPI 参数匹配潜规则】
1. 名字出现在 URL 装饰器 `{}` 里的 -> 路径参数（如 user_id）。
2. 类型是 Pydantic 模型（BaseModel 子类） -> 请求体 Body JSON（如 item）。
3. 既不在 URL 里，也不是 Pydantic 模型的普通基础类型 -> 查询参数（URL 后 ? 里的参数）。
"""

import uvicorn
from fastapi import FastAPI
from loguru import logger
from pydantic import BaseModel

app = FastAPI()


# 定义数据模型类，继承 BaseModel
class Item(BaseModel):
    name: str  # 必填
    desc: str | None = None  # 选填，默认 None
    price: float  # 必填
    tax: float | None = None  # 选填


@app.post("/users/{user_id}/items/")
async def create_item(user_id: int, item: Item):
    """给指定用户创建商品接口

    注意：这是一个 POST 请求，包含路径参数（user_id）和请求体（item JSON）。

    请求示例: POST http://127.0.0.1:8000/users/100/items/
    Body: {"name": "iphone", "price": 999.9, "tax": 0.1}
    """
    # 打印路径参数和请求体数据
    logger.info(f"接收到用户ID: {user_id}")
    logger.info(f"接收到商品数据: name={item.name}, price={item.price}, tax={item.tax}")

    # 如果有税，计算最终价格
    if item.tax is not None:
        total_price = item.price + item.tax
    else:
        total_price = item.price

    return {
        "user_id": user_id,  # 把路径参数也返回去
        "item_name": item.name,
        "total_price": total_price,
        "message": "创建成功",
    }


if __name__ == "__main__":
    uvicorn.run(app="04_request_body:app", host="127.0.0.1", port=8000, reload=True)
