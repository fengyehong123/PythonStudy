"""
    定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
    局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。
    在函数内部声明的变量只在函数内部的作用域中有效，
    调用函数时，这些内部变量会被加入到函数内部的作用域中，并且不会影响到函数外部的同名变量，
"""

# 全局变量
num = 10

def printNum():
    # 函数内定义的局部变量和全局变量同名, 此时优先使用局部变量
    num = 10000
    print(num)

print(num)  # 10
printNum()  # 10000

"""
    当内部作用域想修改全局作用域的变量时
    需要用到 global 关键字
"""
def changeGlobalVar():
    # 声明使用全局变量的num
    global num
    # 在函数内容修改全局变量
    num = 10000
    print(num)

# 调用函数修改全局变量
changeGlobalVar()  # 10000
# 打印全局变量，可以看到我们在函数内部修改外部的全局变量成功了
print(num)  # 10000
print('\033[91m-----------------------------------------------\033[0m')

"""
    如果要修改嵌套作用域 (enclosing 作用域，外层非全局作用域) 中的变量
    则需要 nonlocal 关键字了
"""
def outer():

    # 函数内部的局部变量
    num = 10

    # 函数内的函数
    def inner():
        # nonlocal关键字声明
        nonlocal num
        # 此时修改的是不是全局变量的num，而是外部函数内的局部变量num
        num = 100
        print(num)  # 100
    
    # 在外部函数中, 调用内部函数
    inner()
    print(num)  # 100

outer()
print('\033[91m-----------------------------------------------\033[0m')

print(num)  # 10000