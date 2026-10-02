import time
import threading

def sing():
    for i in range(3):
        print("唱歌中...")
        time.sleep(1)


def dance():
    for i in range(3):
        print("跳舞中...")
        time.sleep(1)


if __name__ == "__main__":
    # 创建线程
    sing_thread = threading.Thread(target=sing)
    dance_thread = threading.Thread(target=dance)
    # 启动线程
    sing_thread.start()
    dance_thread.start()
