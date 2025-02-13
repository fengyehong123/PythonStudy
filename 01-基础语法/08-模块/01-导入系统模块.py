"""
    语法
    1. import module1[, module2[,... moduleN]
        导入整个模块对象
    2. from modname import name1[, name2[, ... nameN]]
        导出模块中的指定部分
    3. from modname import *
        导入模块中的所有部分
"""
# ⭕导入整个模块对象
import random

for _ in range(random.randint(1, 4)):
    print("hello world...")

# ⭕引入比较模块中的eq函数
from operator import eq

lia = [1, 2, 3]
lib = [1, 2, 3]
"""
    如果我们 import operator 的话
    那么需要 operator.eq(lia, lib) 进行比较
"""
print(eq(lia, lib))  # True

# ⭕导入模块中的指定函数并取一个别名
from random import choice as haha

result1 = haha(range(100))
print(result1)  # 11

