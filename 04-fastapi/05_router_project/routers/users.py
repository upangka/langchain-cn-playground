from fastapi import APIRouter

# 实例化 APIRouter
# prefix 会给该文件下所有路由自动加上前缀 /users
# tags 会在 /docs 文档中把接口归类到「用户管理」
user_router = APIRouter(prefix="/users", tags=["用户管理"])


@user_router.get("/")
async def get_all_users():
    return {"message": "获取所有用户列表"}


@user_router.get("/{user_id}")
async def get_user(user_id: int):
    return {"message": f"获取 ID 为 {user_id} 的用户信息"}
