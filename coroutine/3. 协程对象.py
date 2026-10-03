import asyncio

async def task1():
    print("task1 start")
    await asyncio.sleep(2)
    print("task1 end")
    return 1

async def main():
    # 查看协程对象的类型：先创建，看完类型后用 close() 关闭，避免"never awaited"警告
    coro = task1()
    print('类型:', type(coro))   # <class 'coroutine'>
    coro.close()

    # await 后面跟协程对象：调用 async 函数得到的就是协程对象
    result = await task1()
    print('结果:', result)

asyncio.run(main())
