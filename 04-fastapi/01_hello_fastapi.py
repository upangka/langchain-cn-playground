import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/", summary="Welcome to FastAPI")
async def hello():
    return {"msg": "hello world from FastAPI"}


if __name__ == "__main__":
    uvicorn.run(
        app="01_hello_fastapi:app",  # 模块名:实例名
        host="127.0.0.1",
        port=8000,
        reload=True,  # 开启热重载，修改代码后自动重启
    )
