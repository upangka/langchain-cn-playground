"""
FastAPI 路径参数与类型校验 (Unit 2.4)

【实验目的】
1. 体验路径参数的类型转换（将浏览器传的字符串自动转为 int）。
2. 体验 FastAPI 自动进行类型校验并返回 422 错误。
3. 踩坑：理解路由顺序对匹配的影响。
"""

import uvicorn
from fastapi import FastAPI

app = FastAPI()


# 1. 路径参数类型声明
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # 如果传的不是数字，FastAPI 会直接拦截并报错，不会进入这个函数
    return {"item_id": item_id, "type": str(type(item_id))}


# 2. 经典坑：固定路径 vs 动态路径
# 注意：/users/me 必须写在 /users/{user_id} 之前！
@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


if __name__ == "__main__":
    uvicorn.run(app="02_path_params:app", host="127.0.0.1", port=8000, reload=True)
