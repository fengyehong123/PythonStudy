# 使用字典来优化if else
colorCodesDict = {
    'blue': '#2196F3',
    'green': '#4CAF50',
    'orange': '#FF9800',
    'pink': '#E91E63',
    'default': '#F44336'
}
print(colorCodesDict['blue'])  # #2196F3

# 创建发送邮件的方法
mail163 = lambda userName : f"用户{userName}发送了163邮件"
mailQQ = lambda userName : f"用户{userName}发送了QQ邮件"
mailGmail = lambda userName : f"用户{userName}发送了Gmail邮件"

# 使用字典来进行映射
mailSendDict = {
    '163': mail163,
    'QQ': mailQQ,
    'Gmail': mailGmail
}
sendMethod = mailSendDict['QQ']
print(sendMethod('张三'))

# 导入指定的模块
import re
import random

def send_mail(identity, status, userName):

    """
        列表中的元素是元组
        元组配合正则表达式进行ifelse优化
    """
    actionList = [
        (re.compile(r'^guest_[1-4]$'), mail163),
        (re.compile(r'^guest_5$'), mailQQ),
        (re.compile(r'^guest_.*$'), mailGmail),
    ]

    # 获取用户的身份的状态的key
    key = f"{identity}_{status}"

    # 遍历列表解构元组，得到正则表达式的和对应的方法
    for pattern, sendMailMethod in actionList:
        if pattern.match(key):
            return sendMailMethod(userName)

# 获取随机数，表示用的当前状态
random_status = random.randint(1, 7)
print(send_mail('guest', random_status, '张三'))