# Python 基础进阶：并发编程与高级特性 (Appendix Python Basic)

本项目主要记录了 Python 基础进阶阶段的核心知识点，重点涵盖了**进程 (Process)**、**线程 (Thread)**、**协程 (Coroutine)** 三大并发编程模型，以及 Python 中的高级语法特性。


# 进程Process

| 核心知识点 | 文件名 |
| :--- | :--- |
| **创建进程的基础** | [01_create_process.py](./process/01_create_process.py) |
| **进程同步（锁）** | [02_process_lock.py](./process/02_process_lock.py) |
| **父子进程join** | [03_join_process.py](./process/03_join_process.py) |
| **Queue通信** | [04_queue_process.py](./process/04_queue_process.py) |
| **管道Pipe通信基础** | [05_pipe_process.py](./process/05_pipe_process.py) |
| **继承 Process 类** | [06_inherit_process.py](./process/06_inherit_process.py) |
| **进程池** | [07_pool_process.py](./process/07_pool_process.py) |


# 线程Thread

| 核心知识点 | 文件名 |
| :--- | :--- |
| **创建线程的基础** | [01_create_thread.py](./threads/01_create_thread.py) |
| **线程池** | [02_thread_pool.py](./threads/02_thread_pool.py) |
| **GIL 锁原理与验证** | [03_GIL锁.ipynb](./threads/03_GIL锁.ipynb) |


# 协程Coroutine

| 核心知识点 | 文件名 |
| :--- | :--- |
| **协程基础概念** | [01_coroutine_basic.py](./coroutine/01_coroutine_basic.py) |
| **协程并发执行** | [02_concurrent.py](./coroutine/02_concurrent.py) |
| **同步 vs 异步 HTTP 请求 (Notebook)** | [03_sync_vs_async_http.ipynb](./coroutine/03_sync_vs_async_http.ipynb) |
| **同步 vs 异步 HTTP 请求** | [03_sync_vs_async_http.py](./coroutine/03_sync_vs_async_http.py) |