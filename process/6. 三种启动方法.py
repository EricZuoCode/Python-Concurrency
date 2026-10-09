import multiprocessing

count = 0   # 全局变量初始值

def task():
    # fork：子进程复制父进程内存，能看到父进程改过的 count
    # spawn：子进程是全新解释器，count 是模块初始值 0
    print(f"子进程看到的 count = {count}")

if __name__ == "__main__":
    count = 100   # 父进程修改全局变量

    # fork 方式
    ctx_fork = multiprocessing.get_context('fork')
    p1 = ctx_fork.Process(target=task, name="fork进程")
    p1.start()
    p1.join()

    # spawn 方式
    ctx_spawn = multiprocessing.get_context('spawn')
    p2 = ctx_spawn.Process(target=task, name="spawn进程")
    p2.start()
    p2.join()
