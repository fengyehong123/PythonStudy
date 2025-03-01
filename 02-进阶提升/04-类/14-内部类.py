class School:

    def __init__(self, address):
        self.address = address
    
    # 定义一个内部类
    class Student:

        def __init__(self, outer_instance, studentName):
            # 传入外部类实例
            self.school = outer_instance
            self.name = studentName

        def printAddressInfo(self):
            print(f"我的名字叫:{self.name}, 我学校的地址是:{self.school.address}")

# 创建外部类的对象
school = School("银河系地球亚洲中国")
# 创建内部类的对象(创建的同时需要把外部类的对象也一同传入)
student = school.Student(school, "张三")
# 调用内部类的方法
student.printAddressInfo()  # 我的名字叫:张三, 我学校的地址是:银河系地球亚洲中国

"""
    Python 的内部类本质上是静态的
"""
class CommonMst:

    class ReserveTime:
        """可预约时间常量"""
        # 预约开始时间
        START = "1"
        # 预约结束时间
        END = "2"
        # 预约种类 code
        CODE = 1

    class MailInfo:
        """邮件常量"""
        # 服务器地址
        SERVER = "1"
        # 端口
        PORT = "2"  
        # 用户
        USER = "3"  
        # 密码
        PASSWORD = "4"  
        # 发信者
        FROM_ADDRESS = "5" 
        # 送信者 
        SENDER_NAME = "6"  
        # 邮件种类 code
        CODE = 2  

print(CommonMst.ReserveTime.START)  # 1
print(CommonMst.MailInfo.SENDER_NAME)  # 6


