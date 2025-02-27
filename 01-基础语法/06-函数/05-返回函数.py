# 一个普通的求和函数
def calc_sum(*args):
    ax = 0
    # 循环所有的参数,将其累加
    for n in args:
        ax = ax + n
    return ax

"""
    高阶函数除了可以接受函数作为参数外
    还可以把函数作为结果值返回。
    也就是说, 我们可以将求和的函数作为结果值返回。
"""
def lazy_sum(*args):
    # 在函数内部, 定义一个求和的函数
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 尝试调用函数, 可以看到得到的值是一个函数
sum1 = lazy_sum(1, 3, 5, 7, 9)
print(type(sum1))  # <class 'function'>

# 调用返回的函数, 得到值
print(sum1())  # 25