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