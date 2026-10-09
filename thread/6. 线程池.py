import time
from concurrent.futures import ThreadPoolExecutor

def task(name, seconds):
    print(f"{name} 开始执行...")
    time.sleep(seconds)
    print(f"{name} 执行完成！")
    return f"{name} 的结果"

if __name__ == "__main__":
    start = time.time()
    # 创建线程池，最多同时运行 3 个线程
    with ThreadPoolExecutor(max_workers=3) as pool:
        # 提交 5 个任务，线程池复用这 3 个线程轮流执行
        futures = [pool.submit(task, f"任务{i}", 1) for i in range(5)]
        # 逐个取回结果
        for f in futures:
            print("结果:", f.result())
    print(f"总耗时: {time.time() - start:.1f} 秒")
