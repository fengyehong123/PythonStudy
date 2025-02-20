"""
    Python 3.8 引入了 typing.Protocol, 可以用于定义接口, 而不要求显式继承。
"""
from typing import Protocol

class MailSender(Protocol):

    # 指定返回类型是 字符串类型
    def mailSend(self) -> str:
        pass

"""
    Mail163类 并没有继承 MailSender类,
    但是类中的 mailSend 方法名和 MailSender类中的方法名相同,
    相当于遵守了 Protocol 协议
    因此不需要显示的继承 MailSender类
"""
class Mail163:

    def mailSend(self) -> str:
        return "163邮件发送..."

class MailQQ:

    def mailSend(self) -> str:
        return "QQ邮件发送..."

# 只要实现了 mailSend 方法，就符合协议
def playMail(mail: MailSender):  
    print(mail.mailSend())

for mail in [Mail163(), MailQQ()]:
    print(mail.mailSend())
    # 163邮件发送...
    # QQ邮件发送...
