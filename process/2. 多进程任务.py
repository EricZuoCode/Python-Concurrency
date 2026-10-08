import time
import multiprocessing

def sing():
    for i in range(5):
        print("唱歌中...")
        time.sleep(1)


def dance():
    for i in range(5):
        print("跳舞中...")
        time.sleep(1)


if __name__ == "__main__":
    multiprocessing.set_start_method('spawn')  # 设置启动方式为spawn，避免在Windows上出现RuntimeError
    # 创建进程
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    # 启动进程
    sing_process.start()
    dance_process.start()
