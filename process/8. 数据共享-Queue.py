import multiprocessing

def producer(queue):
    for i in range(5):
        queue.put(f"数据{i}")
        print(f"生产了 数据{i}")

def consumer(queue):
    for _ in range(5):
        data = queue.get()
        print(f"消费了 {data}")

if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
