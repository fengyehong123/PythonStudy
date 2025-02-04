# Python中的单行注释
"""
Python中的多行注释
"""

# 最基本的Hello world
print('Hello Wolrd!')

# Python中的布尔值，注意,一定要是大写的 True 和 False
FLAG1 = True
FLAG2 = False

# Python允许为多个变量赋值
a = b = c = 1
print(a, b, c)  # 1 1 1

e, f, g = 10, 20, "测试"
print(e, f, g)  # 10 20 测试


# Python中的布尔值运算
print(FLAG1 and FLAG2)  # False
print(FLAG1 or FLAG2)  # True
print(not FLAG1)  # False

# Python中的常量使用大写来表示，但Python中的常量其实也是可以被修改的
# 只是约定俗称使用大写表示常量而已
AGE = 20

# 导入模块
from typing import Final

# Python 3.8 引入了 typing.Final，可以用于标记变量为 常量
# 如果尝试重新赋值，静态类型检查工具会提示报错，但是代码运行时不会报错，因为Python语言并不强制常量
MAX_COUNT: Final = 5
print(MAX_COUNT)

# Python中没有 {} ，使用缩进来代替
if AGE >= 18:
    print('年龄 >= 18 岁')
else:
    print('年龄 < 18岁')

# 可以使用del来删除对象的引用
del AGE

# 可以使用 globals() 来检查全局变量是否存在
# 可以使用 locals() 来检查局部变量是否存在
if "AGE" in globals():
    print("变量 AGE 仍然存在")
else:
    print("变量 AGE 已被删除")

# Python中使用 None 来表示空，而不是使用 null
HOUSE = None
if HOUSE is None:
    print('AGE变量为None...')