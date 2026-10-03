import time 
import asyncio


async def task1():          # 创建协程任务，使用 asyncio 代表任务是由 asyncio 管理的，而不是由人工调用
    # time.sleep(5)  # 不能使用 time.sleep()，因为 time.sleep() 是阻塞的，会阻塞整个事件循环，导致其他协程任务无法执行
    print("task1 start")
    await asyncio.sleep(5)  # 通过 await 关键字挂起协程任务，等待 5 秒钟，await 后面必须是一个 awaitable 对象，asyncio.sleep() 就是一个 awaitable 对象
    print("task1 end")
    return 1

async def task2():
    print("task2 start")
    await asyncio.sleep(3)
    print("task2 end")
    return 2

async def main():
    print("main start")
    # 1. 创建协程任务
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())
    # 2. 使用 await 关键字挂起协程任务，等待协程任务执行完成，并获取返回值
    result1 = await t1
    result2 = await t2
    print('结果:', result1 + result2)
    print("main end")

if __name__ == '__main__':
    start = time.time()
    # 3. 启动事件循环并运行协程任务（asyncio.run 会自动创建并管理事件循环）
    asyncio.run(main())
    end = time.time()
    print('总耗时:', end - start)
