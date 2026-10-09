import multiprocessing

def increment(counter, lock):
    for _ in range(50000):
        with lock:               # 加锁保护"读-改-写"
            counter.value += 1

if __name__ == "__main__":
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    processes = [multiprocessing.Process(target=increment, args=(counter, lock)) for _ in range(4)]
    for p in processes: p.start()
    for p in processes: p.join()
    print(f"counter = {counter.value}（期望 200000）")
