"""
FastAPI 路由分发主应用 (Unit 2.7)

【实验目的】
1. 掌握 APIRouter 的使用，将不同业务的路由拆分到不同文件中。
2. 掌握 app.include_router() 进行路由挂载。
3. 观察自动生成的 /docs 文档是如何按 tags 归类的。
"""

import uvicorn
from fastapi import FastAPI
from routers.items import goods_router
from routers.users import user_router

app = FastAPI(title="路由分发示例")

# 挂载路由
app.include_router(goods_router)
app.include_router(user_router)


# 主应用自身依然可以保留一些全局路由
@app.get("/")
async def root():
    return {"message": "欢迎访问主页面"}


if __name__ == "__main__":
    # 注意这里 app 的路径变成了 main:app（因为你的启动文件叫 main.py）
    uvicorn.run(app="main:app", host="127.0.0.1", port=8000, reload=True)
