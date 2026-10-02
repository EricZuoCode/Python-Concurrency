import time

def sing():
    for i in range(5):
        print("唱歌中...")
        time.sleep(1)


def dance():
    for i in range(5):
        print("跳舞中...")
        time.sleep(1)


if __name__ == "__main__":
    sing()
    dance()