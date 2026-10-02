'''
线程的执行顺序是无序的
'''

import time
import threading


def task():
    time.sleep(1)                           # 模拟任务执行时间，否则线程执行太快，无法体现线程的无序性
    thread = threading.current_thread()     # 获取当前线程对象
    print(f"{thread.name} 开始执行任务")

if __name__ == "__main__":
    for i in range(5):
        thread = threading.Thread(target=task)
        thread.start()

'''
执行结果：
Thread-1 (task) 开始执行任务
Thread-2 (task) 开始执行任务
Thread-5 (task) 开始执行任务
Thread-3 (task) 开始执行任务
Thread-4 (task) 开始执行任务
'''