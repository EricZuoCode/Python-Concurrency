import threading

lock = threading.RLock()    # 可重入锁

def outer():
    with lock:
        print("进入外层")
        inner()

def inner():
    with lock:               # 同一线程再次加锁，RLock 允许，普通 Lock 会死锁
        print("进入内层")

if __name__ == "__main__":
    t = threading.Thread(target=outer)
    t.start()
    t.join()