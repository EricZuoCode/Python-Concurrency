import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def worker1():
    with lock_a:
        print("worker1 拿到 A，等待 B...")
        with lock_b:
            print("worker1 拿到 B")

def worker2():
    with lock_b:
        print("worker2 拿到 B，等待 A...")
        with lock_a:
            print("worker2 拿到 A")

if __name__ == "__main__":
    t1 = threading.Thread(target=worker1)
    t2 = threading.Thread(target=worker2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()