import multiprocessing
import threading

lock = threading.Lock()   # 全局锁

def child():
    # fork 后，子进程拷贝了父进程的锁（含"已持有"状态）
    # 持有者变成了子进程主线程，所以子进程可以释放它
    lock.release()
    print("子进程释放锁成功")

if __name__ == "__main__":
    lock.acquire()   # 主进程主线程持有锁
    print("主进程主线程已持有锁")

    ctx = multiprocessing.get_context('fork')
    p = ctx.Process(target=child)
    p.start()
    p.join()

    # fork 不影响父进程：父进程这边锁仍被主线程持有
    print("父进程锁仍被持有：", lock.locked())
    lock.release()
    print("主进程释放锁成功")
