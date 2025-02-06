"""
⏹Python3 中常见的数据类型有:
    Number(数字)
    String(字符串)
    bool(布尔类型)
    List(列表)
    Tuple(元组)
    Set(集合)
    Dictionary(字典)

⏹Python3 的六个标准数据类型中:
    不可变数据(3 个):
        Number(数字)、String(字符串)、Tuple(元组)
    可变数据(3 个):
        List(列表)、Dictionary(字典)、Set(集合)
"""

# ⏹Python中的数字
# Python3 支持 int、float、bool、complex（复数）

# 定义若干个变量并赋值
a, b, c, d = 20, 5.5, True, 4+3j

# ⭕type() 函数可以用来查询变量所指的对象类型
print(a, type(a))  # 20 <class 'int'>
print(b, type(b))  # 5.5 <class 'float'>
print(c, type(c))  # True <class 'bool'>
print(d, type(d))  # (4+3j) <class 'complex'>

# ⭕也可以使用 isinstance 来进行判断
# isinstance 和 type 的区别在于
#   type()不会认为子类是一种父类类型。
#   isinstance()会认为子类是一种父类类型。
num1 = 100
if isinstance(num1, int):
    print('num1变量是一个int类型的数据')