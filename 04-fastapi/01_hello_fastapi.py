import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/", summary="Welcome to FastAPI")
async def hello():
    return {"msg": "hello world from FastAPI"}


@app.get("/list")
async def lst_result():
    return ["hello", "world"]


@app.get("/str")
async def str_result():
    return "hello world".upper()


class User(BaseModel):
    username: str
    msg: str


@app.get("/pydantic")
async def pydantic_result():
    return User(username="鲨鱼のBlue", msg="Hello World")


if __name__ == "__main__":
    uvicorn.run(
        app="01_hello_fastapi:app",  # 模块名:实例名
        host="127.0.0.1",
        port=8000,
        reload=True,  # 开启热重载，修改代码后自动重启
    )
