import time 


def task1():
    time.sleep(5)
    return 1

def task2():
    time.sleep(3)
    return 2

def main():
    start = time.time()
    result1 = task1()
    result2 = task2()
    end = time.time()
    print('总耗时:', end - start, '结果:', result1 + result2)

if __name__ == '__main__':
    main()
