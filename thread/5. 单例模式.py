import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance:   
            return cls._instance           # 如果实例存在，直接返回实例，这个用于提高性能，避免每次都加锁
      
        with cls._lock:                    # 加锁，同一时刻只有一个线程创建实例
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

def test():
    s = Singleton()
    print(f"{threading.current_thread().name}: 实例地址 {id(s)}")

if __name__ == "__main__":
    threads = [threading.Thread(target=test, name=f"线程{i}") for i in range(5)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()