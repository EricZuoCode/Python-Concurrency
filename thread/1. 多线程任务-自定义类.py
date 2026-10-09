import time
import threading

class MyThread(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)   # 调用父类构造，设置线程名

    def run(self):                    # 重写 run 方法，定义线程要执行的逻辑
        print(f"{self.name} 开始执行")
        time.sleep(2)
        print(f"{self.name} 执行完成")

if __name__ == "__main__":
    t1 = MyThread(name="线程1")
    t2 = MyThread(name="线程2")
    t1.start()   # start() 会自动调用 run()
    t2.start()
    t1.join()
    t2.join()
