import time
import multiprocessing

def sing(num, name):
    for i in range(num):
        print(f"{name}唱歌中...")
        time.sleep(1)


def dance(num, name):
    for i in range(num):
        print(f"{name}跳舞中...")
        time.sleep(1)


if __name__ == "__main__":
    # 创建进程
    sing_process = multiprocessing.Process(target=sing, args=(5, "张三"))                       # 使用 args 元祖类型传递参数给 sing 函数
    dance_process = multiprocessing.Process(target=dance, kwargs={'num': 5, 'name': '李四'})    # 使用 kwargs 字典类型传递参数给 dance 函数，字典的 key 必须和函数参数名一致但没有顺序
    # 启动进程
    sing_process.start()
    dance_process.start()
