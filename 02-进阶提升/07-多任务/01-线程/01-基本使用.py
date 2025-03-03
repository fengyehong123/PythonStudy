"""
    参考资料
        https://github.com/jackfrued/Python-100-Days/blob/master/Day61-65/63.Python%E4%B8%AD%E7%9A%84%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-1.md
"""
import time
import random
# 导入线程模块
from threading import Thread

def download(*, filename):

    start = time.time()
    print(f'开始下载 {filename}.')

    # 模拟网络下载消耗时间
    time.sleep(random.randint(3, 6))
    print(f'{filename} 下载完成.')

    end = time.time()
    print(f'下载耗时: {end - start:.3f}秒.')

# 继承原生Thread线程对象, 重写了其中的run方法
class DownloadThread(Thread):

    def __init__(self, filename):
        self.filename = filename
        super().__init__()

    # 重写了原生Thread线程对象的run()方法
    def run(self):

        start = time.time()
        print(f'开始下载 {self.filename}.')

        # 模拟网络下载消耗时间
        time.sleep(random.randint(3, 6))
        print(f'{self.filename} 下载完成.')

        end = time.time()
        print(f'下载耗时: {end - start:.3f}秒.')

def main(custom_thread_flag = False):

    # 线程任务list
    threads = []

    # 判断是否是自定义线程对象的flag
    if custom_thread_flag:
        print('\033[91m-----------------------------------------------\033[0m')
        threads = [
             # 使用继承了原生线程对象的自定义线程来进行下载
            DownloadThread('Python从入门到住院.pdf'),
            DownloadThread('MySQL从删库到跑路.avi'),
            DownloadThread('Linux从精通到放弃.mp4')
        ]
        print('\033[91m-----------------------------------------------\033[0m')
    else:
        threads = [
            # 使用原生的线程来进行下载
            Thread(target=download, kwargs={'filename': 'Python从入门到住院.pdf'}),
            Thread(target=download, kwargs={'filename': 'MySQL从删库到跑路.avi'}),
            Thread(target=download, kwargs={'filename': 'Linux从精通到放弃.mp4'})
        ]
    
    start = time.time()

    # 启动三个线程
    for thread in threads:
        thread.start()

    # 等待线程结束
    for thread in threads:
        thread.join()

    # 计算总耗时
    end = time.time()
    print(f'总耗时: {end - start:.3f}秒.')
    """
        1. 通过上面的运行结果可以发现，整个程序的执行时间几乎等于耗时最长的一个下载任务的执行时间，这也就意味着，三个下载任务是并发执行的，
        不存在一个等待另一个的情况，这样做很显然提高了程序的执行效率。

        2. 简单的说，如果程序中有非常耗时的执行单元，而这些耗时的执行单元之间又没有逻辑上的因果关系，即 B 单元的执行不依赖于 A 单元的执行结果，
        那么 A 和 B 两个单元就可以放到两个不同的线程中，让他们并发的执行。

        3. 这样做的好处除了减少程序执行的等待时间，还可以带来更好的用户体验，
        因为一个单元的阻塞不会造成程序的“假死”，因为程序中还有其他的单元是可以运转的。
    """

if __name__ == '__main__':
    main(custom_thread_flag = True)