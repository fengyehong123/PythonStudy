"""
    functools.partial 主要用于 创建偏函数(partial function)
    即固定某些参数值的函数。
    可以简化回调函数，减少重复代码
"""
from functools import partial

def power(base, exponent):
    return base ** exponent

# 创建一个固定了 base=2 的函数，即计算 2 的 n 次方
square = partial(power, 2)

# 相当于获取2的3次方(2^3)
print(square(3))  # 8
# 相当于获取2的4次方(2^3)
print(square(4))  # 16

"""
    sorted() 允许传入 key 参数
    使用 partial 可以更方便地指定排序方式。
"""
data = ["Banana", "cherry", "apple"]

# 第2个参数来指定忽略大小写来排序
sorted_case_insensitive = partial(sorted, key=str.lower)
print(sorted_case_insensitive(data))  # ['apple', 'Banana', 'cherry']
print('\033[91m-----------------------------------------------\033[0m')

"""
    某些 API (如 map()、GUI 事件处理、线程池等) 要求传入回调函数
    而这个回调可能需要额外的参数，使用 partial 绑定参数可以避免定义额外的包装函数。
"""
import sys
import multiprocessing

def worker(task_name, num):
    """
        在某些情况下, 直接 print() 可能不会立即刷新到终端, 导致你看不到任何输出, 或者输出顺序混乱。
        修正方式 「使用 sys.stdout.write() 手动刷新」
    """
    sys.stdout.write(f"Processing {task_name}: {num}\n")
    sys.stdout.flush()

"""
    在 Windows 上, multiprocessing 不能 直接在顶层运行，它必须放在 
        if __name__ == "__main__": 
    结构中，否则会抛出异常
"""
if __name__ == "__main__":

    # 固定参数
    task_func = partial(worker, "Download Task")

    """
        multiprocessing.Pool(3) 
            创建了一个 包含3个worker进程的进程池, 意味着最多会同时运行 3 个任务
        with ... as
            确保 进程池会自动关闭, 避免资源泄漏, 不需要手动调用 pool.close() 和 pool.join()
    """
    with multiprocessing.Pool(3) as pool:
        """
            pool.map(task_func, range(5))
                1. 启动 3 个子进程（因为 Pool(3)）。
                2. 分配任务：
                    进程 1 处理 task_func(0)
                    进程 2 处理 task_func(1)
                    进程 3 处理 task_func(2)
                3. 等待其中某个进程完成后，继续分配任务：
                    3.1 假设 进程 1 先完成了 task_func(0)，它会立即被重新分配去处理 task_func(3)。
                    3.2 然后等进程 2 或 3 释放时，再分配 task_func(4)。
                4. 所有任务完成后，进程池自动关闭。
        """
        pool.map(task_func, range(100))

