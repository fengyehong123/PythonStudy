import time
import asyncio

"""
    Python 中的asyncio模块提供了对异步 I/O 的支持。
    下面的代码中, 首先在 getInfo函数 前面加上了【async关键字】使其变成一个异步函数, 调用异步函数不会执行函数体而是获得一个协程对象。
    我们将 getInfo函数 中的time.sleep(1) 修改为 await asyncio.sleep(1)
    二者的区别在于, 后者不会让整个代码陷入阻塞, 因为await操作会让其他协作的子程序有获得 CPU 资源而得以运转的机会。
"""
async def getInfo(num):
    await asyncio.sleep(1)
    print(num)

"""
    数字并不是按照从1到9的顺序打印输出的, 这正是我们想要的结果, 说明它们是异步执行的。
    对于爬虫这样的 I/O 密集型任务来说，这种协作式并发在很多场景下是比使用多线程更好的选择，
    因为这种做法减少了管理和维护多个线程以及多个线程切换所带来的开销。
"""
async def main():

    start = time.time()
    

    # 创建job列表
    objs = [getInfo(i) for i in range(1, 10)]
    # gather 直接并行执行所有协程, 然后通过 await 等待所有协程任务执行完成
    await asyncio.gather(*objs)

    end = time.time()
    print(f'{end - start:.3f}秒')

if __name__ == '__main__':
    """
        asyncio.run() 是 Python 3.7+ 提供的更安全的方式来运行异步代码
        它会自动管理事件循环的生命周期，避免手动创建 loop 可能带来的问题。
    """
    # 使用 asyncio.run() 代替手动管理 loop
    asyncio.run(main())