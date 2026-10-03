import asyncio

async def task1():
    print("task1 start")
    await asyncio.sleep(2)
    print("task1 end")
    return 1

async def task2():
    print("task2 start")
    await asyncio.sleep(1)
    print("task2 end")
    return 2

async def main():
    # create_task 把协程包装成 Task，创建后立即被事件循环调度
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    # await 后面跟 Task 对象
    result1 = await t1
    result2 = await t2
    print('结果:', result1 + result2)

asyncio.run(main())