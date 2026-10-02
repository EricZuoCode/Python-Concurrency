import threading

count = 0
lock = threading.Lock()

def add():
    global count
    for _ in range(200000):
        with lock:               # 进入时自动 acquire，退出时（含异常）自动 release
            count += 1

if __name__ == '__main__':
    threads = []
    for _ in range(8):
        t = threading.Thread(target=add)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print(f"最终 count = {count} , 预期 count = {8 * 200000}")