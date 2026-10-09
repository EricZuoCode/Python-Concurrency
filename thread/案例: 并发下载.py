import time
import threading

def download(name, seconds):
    print(f"{name} 开始下载...")
    time.sleep(seconds)   # 模拟下载耗时
    print(f"{name} 下载完成！")

if __name__ == "__main__":
    start = time.time()
    tasks = [("文件A", 2), ("文件B", 1), ("文件C", 3)]
    threads = []
    for name, seconds in tasks:
        t = threading.Thread(target=download, args=(name, seconds))
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    print(f"总耗时：{time.time() - start:.1f} 秒")
