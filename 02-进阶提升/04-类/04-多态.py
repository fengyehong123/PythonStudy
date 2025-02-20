class Mail:
    def sendMail(self):
        print("邮件已经发送...")

class Mail163(Mail):

    def __init__(self, address):
        self.address = address

    def sendMail(self):
        print(f"163邮件{self.address}已经发送...")

class MailQQ(Mail):

    def __init__(self, address):
        self.address = address
        
    def sendMail(self):
        print(f"QQ邮件{self.address}已经发送...")

"""
    Python中的多态
    同一个接口（方法或属性）在不同的类中具有不同的实现。
    多态可以提高代码的灵活性和可扩展性，使得代码更加通用。
"""
def mailSend(mail: Mail):
    # Mail163类 和 MailQQ类都继承了 Mail类
    mail.sendMail()

mailSend(Mail163("test1@163.com"))  # 163邮件test1@163.com已经发送...
mailSend(MailQQ("test1@qq.com"))  # QQ邮件test1@qq.com已经发送...

for mail in [Mail163("aaa@163.com"), MailQQ("bbb@qq.com")]:
    mailSend(mail)
    # 163邮件aaa@163.com已经发送...
    # QQ邮件bbb@qq.com已经发送...