import time
import threading

def work():
    for i in range(10):
        print("子线程开始工作...")
        time.sleep(0.2)

if __name__ == "__main__":
    work_thread = threading.Thread(target=work, daemon=True)    # 方法一： 设置为守护线程，主进程结束，子线程也会结束
    # work_thread.daemon = True                                 # 方法二： 设置为守护线程，主进程结束，子线程也会结束
    work_thread.start()        # 子线程执行需要2秒

    time.sleep(1)  # 主进程休眠1秒
    print("主进程结束工作...")
