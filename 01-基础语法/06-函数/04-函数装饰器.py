"""
    装饰器 (decorators) 是 Python 中的一种高级功能，它允许你动态地修改函数或类的行为。
    装饰器是一种函数，它接受一个函数作为参数，并返回一个新的函数或修改原来的函数。
    装饰器的语法使用 @decorator_name 来应用在函数或方法上。
"""

# 自定义一个装饰器，用来给目标函数增强功能
def msgControl(func):
    def wrapper(*args, **kwargs):
        print("执行之前...")
        func(*args, **kwargs)
        print("执行之后...")
    return wrapper

# 使用自定义装饰器来增强目标函数
@msgControl
def printInfo(info):
    print(f"Hello World, {info}")

# 调用被装饰器修饰之后的函数
printInfo("哈哈哈")

"""
    装饰器中函数也可以接受参数
"""
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("发送骚扰短信")
greet()

"""
    可以使用装饰器统计函数的执行时间
"""
import time
# 导入wraps的作用是保持被装饰函数的原始信息，防止装饰器修改其中的 __name__ 和 __doc__ 等属性
from functools import wraps

def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()
        # 调用传入的函数，获取执行结果
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{func.__name__} 执行时间: {end - start:.5f} 秒")
        return result

    return wrapper

# 使用装饰器, 统计函数的执行时间
@timer
def getUserInfo(userId):
    # 让程序睡眠2秒
    time.sleep(2)
    return {
        "id": userId
        , "name": '贾飞天'
        , "age": 20
    }
print(getUserInfo(10))

"""
    可以使用装饰器进行访问控制
"""
def checkAuth(func):

    @wraps(func)
    def wrapper(user):
        if user != "admin":
            print(f"{user}用户无权限访问...")
            return
        return func(user)
    return wrapper

# 使用装饰器, 记性权限校验
@checkAuth
def accessSecretInfo(userName):
    print(f"{userName} 访问了机密信息...")
accessSecretInfo("guest")  # guest用户无权限访问...
accessSecretInfo("admin")  # admin 访问了机密信息...

print('\033[91m-----------------------------------------------\033[0m')

"""
    定义一个类装饰器，用来计数
"""
class MailSendCounter:

    def __init__(self, func):
        self.func = func
        # 记录邮件发送次数
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} 发送 {self.count} 次")
        return self.func(*args, **kwargs)

@MailSendCounter
def sendMail():
    print("发送一封邮件...")

import random

# 生成0到4的随机数
for _ in range(random.randint(1, 4)):
    sendMail()