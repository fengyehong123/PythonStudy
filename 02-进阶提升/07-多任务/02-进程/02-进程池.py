"""
    对于爬虫这类 I/O 密集型任务来说，使用多进程并没有什么优势；
    但是对于 计算密集型任务 来说，多进程相比多线程，在效率上会有显著的提升，我们可以通过下面的代码来加以证明。

    下面的代码会通过 多线程 和 多进程 两种方式来判断一组大整数是不是质数，
    很显然这是一个 计算密集型任务，我们将任务分别放到 多个线程 和 多个进程 中来加速代码的执行，
    让我们看看多线程和多进程的代码具体表现有何不同。
"""
import time
# 需要通过 【pip install psutil】 命令安装
import psutil
import concurrent.futures

PRIMES = [
    1116281,
    1297337,
    104395303,
    472882027,
    533000389,
    817504243,
    982451653,
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419
] * 5

def is_prime(n):
    """判断素数"""
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n != 1

# ⏹多线程的方式
def main_thread():

    process = psutil.Process()
    start_time = time.time()

    # 线程池
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    
    end_time = time.time()
    cpu_times = process.cpu_times()

    print('\033[91m-------------------多线程----------------------------\033[0m')
    print(f"{cpu_times.user:.2f}s user {cpu_times.system:.2f}s system {end_time - start_time:.3f}s total")  # 25.31s user 0.05s system 25.357s total

# ⏹多进程的方式
def main_process():

    process = psutil.Process()
    start_time = time.time()

    # 进程池
    with concurrent.futures.ProcessPoolExecutor(max_workers=16) as executor:
        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (number, prime))
    
    end_time = time.time()
    cpu_times = process.cpu_times()

    print('\033[91m-------------------多进程----------------------------\033[0m')
    # 💥可以看到当 计算密集型任务 时，多进程的速度显著高于多线程，相对应的 CPU等资源消耗也更高💥
    print(f"{cpu_times.user:.2f}s user {cpu_times.system:.2f}s system {end_time - start_time:.3f}s total")  # 0.06s user 0.17s system 7.102s total

if __name__ == '__main__':

    # 多进程的方式
    main_process()

    # 多线程的方式
    # main_thread()

"""
    综上所述，多进程可以突破 GIL 的限制，充分利用 CPU 多核特性，对于计算密集型任务，这一点是相当重要的。
    常见的计算密集型任务包括科学计算、图像处理、音视频编解码等，
    如果这些计算密集型任务本身是可以并行的，那么使用多进程应该是更好的选择。
"""