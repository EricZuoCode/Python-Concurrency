import time
import multiprocessing

def work():
    for i in range(10):
        print("子进程开始工作...")
        time.sleep(0.2)

if __name__ == "__main__":
    work_process = multiprocessing.Process(target=work)
    # work_process.daemon = True  # 设置为守护进程，主进程结束，子进程也会结束
    work_process.start()        # 子进程执行需要2秒

    time.sleep(1)  # 主进程休眠1秒
    print("主进程结束工作...")
