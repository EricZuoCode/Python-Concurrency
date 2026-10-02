import threading
import time

count = 0
lock = threading.Lock()          # 创建一把互斥锁

def add():
    global count
    for _ in range(200000):
        lock.acquire()           # 加锁，进入临界区
        try:
            tmp = count
            time.sleep(0)
            count = tmp + 1      # 临界区：共享数据的修改
        finally:
            lock.release()       # 释放锁

if __name__ == "__main__":
    threads = []
    for _ in range(8):
        t = threading.Thread(target=add)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"最终 count = {count} , 预期 count = {8 * 200000}")