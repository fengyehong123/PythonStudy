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

"""
    元组 (tuple) 与列表类似，用法基本相同。
    不同之处在于元组的元素不能修改。
    元组写在小括号 () 里，元素之间用逗号隔开。
    元组中的元素类型也可以不相同。
"""

# ⭕定义一个元组
tuple1 = (1, 2, "3", [1, 2, 3], True)

# ⭕元组内的元素是不可修改的
try:
    tuple1[0] = 111
except Exception as e:
    print(e)  # 'tuple' object does not support item assignment

# ⭕元组的元素不可变，但是元组内包含的可变元素内部可变
print(tuple1[3])  # [1, 2, 3]
tuple1[3][0] = 1100
print(tuple1[3])  # [1100, 2, 3]

# ⭕定义一个空元组
tuple2 = ()

# ⭕定义一个只有一个元组的元组
# 注意，只有一个元组的元组后面一定要有一个 ,
# 否则python会将其解释为一个普通的值
tuple3 = (10,)
print(type(tuple3))  # <class 'tuple'>
tuple3_1 = (10)
print(type(tuple3_1))  # <class 'int'>

# ⭕元组和列表的用法基本类似，因此元组也可以通过 + 进行拼接
tuple4 = tuple1 + (100, 200, 300)
print(tuple4)  # (1, 2, '3', [1100, 2, 3], True, 100, 200, 300)