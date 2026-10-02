import threading
import time

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.lock = threading.Lock()     # 每个账户配一把锁

    def withdraw(self, amount):
        with self.lock:                  # 用锁保护「判断+扣款」整个临界区
            if self.balance >= amount:
                time.sleep(0.01)
                self.balance -= amount
                print(f"取款 {amount} 成功，余额 {self.balance}")
            else:
                print(f"余额不足，取款 {amount} 失败，余额 {self.balance}")

account = Account(1000)

if __name__ == "__main__":
    t1 = threading.Thread(target=account.withdraw, args=(800,))
    t2 = threading.Thread(target=account.withdraw, args=(800,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"最终余额 = {account.balance}")