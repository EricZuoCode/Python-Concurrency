import time
import multiprocessing
import os

def sing():
    print(f"唱歌进程pid: {os.getpid()}")          # 唱歌进程pid: 62127
    print(f"唱歌进程父进程pid: {os.getppid()}")    # 唱歌进程父进程pid: 62123

    for i in range(5):
        print("唱歌中...")
        time.sleep(1)


def dance():
    print(f"跳舞进程pid: {os.getpid()}")           # 跳舞进程pid: 62128
    print(f"跳舞进程父进程pid: {os.getppid()}")     # 跳舞进程父进程pid: 62123
    for i in range(5):  
        print("跳舞中...")
        time.sleep(1)


if __name__ == "__main__":
    # 获取主进程pid
    print(f"主进程pid: {os.getpid()}")              # 主进程pid: 62123
    # 因此可以看出 sing 和 dance 进程的父进程pid都是主进程pid，因此他们是主进程的子进程

    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)

    sing_process.start()
    dance_process.start()
