"""
    ⏹lambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式。
    匿名函数不需要使用 def 关键字定义完整函数。
    lambda 函数通常用于编写简单的、单行的函数，通常在需要函数作为参数传递的情况下使用，
    例如在 map()、filter()、reduce() 等函数中。

    ⏹lambda 语法格式：
        lambda arguments: expression
"""

# 定义一个没有参数的lambda函数
fun1 = lambda : "Hello Wrold!"
print(fun1())  # Hello Wrold!

# 定义一个有参数的lambda函数
func2 = lambda info: f"传入的参数是: {info}"
print(func2("你好"))  # 传入的参数是: 你好

# 定义一个转换为大写的lambda函数
convertUpper = lambda arg: arg.upper()
# 定义一个筛选出偶数的函数
filterOdd = lambda num: num % 2 ==0

"""
    与 map()、filter() 和 reduce() 一起使用，以便在集合上执行操作
"""
# 转换为大写
list1 = ['google', 'baidu', 'taobao']
resultList1 = list(map(convertUpper, list1))
print(resultList1)  # ['GOOGLE', 'BAIDU', 'TAOBAO']

# 筛选出偶数
list2 = list(range(10))
resultList2 = list(filter(filterOdd, list2))
print(resultList2)  # [0, 2, 4, 6, 8]

"""
    可以配合字典进行if else 的优化
"""
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
print(sendMethod('张三'))  # 用户张三发送了QQ邮件
