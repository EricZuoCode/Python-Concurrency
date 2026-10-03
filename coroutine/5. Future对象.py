import asyncio

async def main():
    loop = asyncio.get_running_loop()
    # 创建一个 Future 对象（Future 需要手动设置结果）
    future = loop.create_future()

    # 模拟异步操作：1 秒后设置 Future 的结果
    loop.call_later(1, future.set_result, "异步结果")

    print("等待 Future...")
    # await 后面跟 Future 对象
    result = await future
    print('结果:', result)

asyncio.run(main())