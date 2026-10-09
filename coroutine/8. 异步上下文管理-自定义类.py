import asyncio

class AsyncResource:
    """自定义异步上下文管理器"""
    async def __aenter__(self):
        print("进入：打开资源（比如建立连接）")
        return self          # 返回值给 as 后面的变量

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("退出：关闭资源")
        return False         # 返回 False 表示不吞异常

async def main():
    async with AsyncResource() as res:
        print("使用资源中...")
        await asyncio.sleep(1)

asyncio.run(main())
