import time
import asyncio

async def download(name, seconds):
    print(f"{name} 开始下载...")
    await asyncio.sleep(seconds)   # 模拟下载耗时
    print(f"{name} 下载完成！")

async def main():
    start = time.time()
    await asyncio.gather(
        download("文件A", 2),
        download("文件B", 1),
        download("文件C", 3),
    )
    print(f"总耗时：{time.time() - start:.1f} 秒")

if __name__ == "__main__":
    asyncio.run(main())
