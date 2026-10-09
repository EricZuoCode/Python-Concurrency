import time
import multiprocessing

def download(name, seconds):
    print(f"{name} 开始下载...")
    time.sleep(seconds)   # 模拟下载耗时
    print(f"{name} 下载完成！")

if __name__ == "__main__":
    start = time.time()
    tasks = [("文件A", 2), ("文件B", 1), ("文件C", 3)]
    processes = []
    for name, seconds in tasks:
        p = multiprocessing.Process(target=download, args=(name, seconds))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(f"总耗时：{time.time() - start:.1f} 秒")
