import asyncio

async def main():
    lock = asyncio.Lock()      # 异步锁
    async with lock:           # async with：进入时 acquire，退出时 release
        print('持有异步锁')
        await asyncio.sleep(1)
    print('异步锁已释放')

asyncio.run(main())
