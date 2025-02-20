"""
    Python 中只有模块(module)，类(class)以及函数(def、lambda)才会引入新的作用域
    其它的代码块(如 if/elif/else/、try/except、for/while等)是不会引入新的作用域的
    也就是说这些语句内定义的变量，外部也可以访问
"""

if 3 > 2:
    # if 代码块没有引入新的作用域, 因此 msg 变量相当于是全局变量的
    msg = "Hello World!"
    print(msg)  # Hello World!

# 在if代码块之外可以打印if代码块内定义的变量
print(msg)  # Hello World!

def printInfo():

    print(msg)  # Hello World!
    msg1 = "你好, 世界"
    print(msg1)  # 你好, 世界

printInfo()

# 因为 msg1 这个变量是在函数内容定义的, 函数会引入新的作用域, 因此在函数外部无法访问
if "msg1" not in globals():
    print("msg1变量并不存在...")  # msg1变量并不存在...