"""
    ⏹守护线程
        【守护线程】就是在主线程结束的时候，不值得再保留的执行线程。
        这里的不值得保留指的是 守护线程 会在其他 非守护线程 全部运行结束之后被销毁，它守护的是当前进程内所有的非守护线程。
        简单的说，守护线程会跟随主线程一起挂掉，而主线程的生命周期就是一个进程的生命周期。
    
    💥注意
        当我们使用线程池的时候, 在【ThreadPoolExecutor】中, 你无法直接设置 daemon=True 来控制线程是否为守护线程。
        线程池管理的线程默认是 非守护线程，即它们不会随主线程的结束而自动终止。
"""
import time
from threading import Thread

def display(content):
    
    # 死循环, 每隔0.1毫秒就执行一次
    while True:
        time.sleep(0.1)
        print(content, end='', flush=True)


def main(daemonFlag=False):

    # 设置线程任务，并传递参数，通过flag来控制是否通过守护线程来启动
    Thread(target=display, args=('Ping', ), daemon=daemonFlag).start()
    Thread(target=display, args=('Pong', ), daemon=daemonFlag).start()

    print('\033[91m主线程执行开始...\033[0m')
    time.sleep(5)
    
    # 若设置为线程为守护线程，则伴随着主线程的结束，各守护线程也会被强制终止
    print('\033[91m\n主线程执行结束...\033[0m')

if __name__ == '__main__':
    # 是否设置为守护线程
    main(daemonFlag=True)