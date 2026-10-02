import threading
import time

class Account:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:          # 检查余额是否足够
            time.sleep(0.01)                # 模拟取款过程中的网络/数据库延迟
            self.balance -= amount          # 扣款
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