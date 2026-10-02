import threading
import time

count = 0

def add():
    global count
    for _ in range(200000):
        tmp = count        # 1. 读
        time.sleep(0)      # 主动让出 GIL，制造线程切换
        count = tmp + 1    # 2. 写

if __name__ == "__main__":
    threads = []
    for _ in range(8):
        t = threading.Thread(target=add)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()           # 等待所有线程结束

    print(f"最终 count = {count} , 预期 count = {8 * 200000}")