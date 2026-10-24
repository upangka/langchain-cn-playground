"""
商品模块路由 (Unit 2.7)

使用 APIRouter 创建独立的路由集合。
"""

from fastapi import APIRouter

# 实例化 APIRouter
# prefix 会给该文件下所有路由自动加上前缀 /items
# tags 会在 /docs 文档中把接口归类到「商品管理」
goods_router = APIRouter(prefix="/items", tags=["商品管理"])


@goods_router.get("/")
async def get_all_items():
    return {"message": "获取所有商品列表"}


@goods_router.get("/{item_id}")
async def get_item(item_id: int):
    return {"message": f"获取 ID 为 {item_id} 的商品信息"}
