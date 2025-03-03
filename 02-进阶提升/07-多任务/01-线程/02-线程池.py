"""
    ⏹线程池
    还可以通过线程池的方式将任务放到多个线程中去执行，通过 线程池 来使用线程应该是多线程编程最理想的选择。
    事实上，线程的创建和释放都会带来较大的开销，频繁的创建和释放线程通常都不是很好的选择。
    利用线程池，可以提前准备好若干个线程，在使用的过程中不需要再通过自定义的代码创建和释放线程，而是直接复用线程池中的线程。
    Python 内置的 【concurrent.futures模块】 提供了对线程池的支持
"""
import time
import random
# 导入线程对象
from threading import Thread
# 导入线程池
from concurrent.futures import ThreadPoolExecutor

def download(*, filename):

    start = time.time()
    print(f'开始下载 {filename}.')

    # 模拟网络下载文件耗时
    time.sleep(random.randint(3, 6))
    print(f'{filename} 下载完成.')

    end = time.time()
    print(f'下载耗时: {end - start:.3f}秒.')

def main():

    # 开启线程池, 指定4个线程
    with ThreadPoolExecutor(max_workers=4) as pool:

        filenames = ['Python从入门到住院.pdf', 'MySQL从删库到跑路.avi', 'Linux从精通到放弃.mp4']
        start = time.time()

        for filename in filenames:
            # 向线程池中投入下载任务
            pool.submit(download, filename=filename)

    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')

if __name__ == '__main__':
    main()