"""
    ⏹资源竞争
        1. 在编写多线程代码时，不可避免的会遇到多个线程竞争同一个资源（对象）的情况。

        2. 在这种情况下，如果没有合理的机制来保护被竞争的资源，那么就有可能出现非预期的状况。
        下面的代码创建了100个线程向同一个银行账户 (初始余额为0元) 转账, 每个线程转账金额为1元。

        3. 在正常的情况下, 我们的银行账户最终的余额应该是100元,
        但是运行下面的代码我们并不能得到100元这个结果。
"""
import time
# 线程锁
from threading import RLock
# 线程池
from concurrent.futures import ThreadPoolExecutor

# 糟糕的银行账户
class Bad_Account:

    def __init__(self):
        # 初始账户余额为0
        self.balance = 0.0

    # 存钱
    def deposit(self, money):
        """
            💥注意💥
            由于多个线程都会同时访问并修改 【self.balance】
            由于我们并没有给 【self.balance】 加锁
            因此前一个线程对 【self.balance】的修改结果可能会被后一个前程给覆盖掉
            从而引起多个线程对同一个资源的竞争问题
        """
        new_balance = self.balance + money
        # 模拟转账时需要消耗时间
        time.sleep(0.01)
        self.balance = new_balance

# 糟糕的主函数
def bad_main():

    # 银行账户对象
    bad_account = Bad_Account()

    # 创建16个线程池，创建100个线程向银行账户中转钱
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(100):
            # 理论上每个线程都会向银行账户中转入1元钱
            pool.submit(bad_account.deposit, 1)
    
    # 100个线程的任务执行完毕之后，查看银行账户的余额
    print(f"当前银行账户的余额为: {bad_account.balance}")  # 当前银行账户的余额为: 7.0

# 正常的银行账户
class Account:

    def __init__(self):
        # 初始账户余额为0
        self.balance = 0.0
        # 线程锁对象
        self.lock = RLock()
    
    # 比较老式的线程加锁解锁的写法
    def _deposit(self, money):

        # 获得锁, 防止多个线程同时竞争 【self.balance】 资源
        self.lock.acquire()
        try:
            new_balance = self.balance + money
            time.sleep(0.01)
            self.balance = new_balance
        finally:
            # 释放锁
            self.lock.release()

    """更推荐下面这种通过上下文来获得线程锁和释放锁的写法"""
    def deposit(self, money):

        # 通过上下文语法获得锁和释放锁，保证同一个时间只能有一个线程对资源进行修改
        with self.lock:
            new_balance = self.balance + money
            # 模拟转账时需要消耗时间
            time.sleep(0.01)
            self.balance = new_balance

"""主函数"""
def main():

    # 银行账户对象
    account = Account()

    # 创建16个线程池，创建100个线程向银行账户中转钱
    with ThreadPoolExecutor(max_workers=16) as pool:
        for _ in range(100):
            # 每个线程都会向银行账户中转入1元钱
            pool.submit(account.deposit, 1)

    # 100个线程的任务执行完毕之后，查看银行账户的余额
    print(f"当前银行账户的余额为: {account.balance}")  # 当前银行账户的余额为: 100.0

if __name__ == '__main__':
    bad_main()
    main()