# 定义最简单的异常, 只继承Exception, 并不做额外的处理
class CustomException1(Exception):
    pass

try:
    if 3 > 2:
        # 抛出自定义的异常
        raise CustomException1("自定义的CustomException1异常")
except CustomException1 as e1:
    print(f"消息打印1: {e1}")  # 消息打印1: 自定义的CustomException1异常
except Exception as e:
    print(f"消息打印2: {e}")

# 自定义的异常可以定义 __init__ 方法, 让异常支持更多的消息
class CustomException2(Exception):

    # 类的初始化方法
    def __init__(self, message, code):
        # 调用父类构造方法
        super().__init__(message)
        # 显式创建 self.message
        self.message = message
        # 自定义异常类的额外属性
        self.code = code

    # 重写 __str__ 方法, 修改打印异常类时显示在控制台上的字符串
    def __str__(self):
        return f"[错误码 {self.code}] → {self.message}"

try:
    if 5 > 4:
        # 抛出自定义的异常
        raise CustomException2("资源找不到", 404)
except CustomException2 as e:

    # 因为自定义异常类中重写了 __str__() 方法, 因此打印时的输出被改变
    print(e)  # [错误码 404] → 资源找不到

    # 获取自定义异常类中的属性
    print(e.message)  # 资源找不到
    print(e.code)  # 404
    
except Exception as e:
    raise e