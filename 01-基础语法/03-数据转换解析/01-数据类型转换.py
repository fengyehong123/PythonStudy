# 在隐式类型转换中，Python 会自动将一种数据类型转换为另一种数据类型，不需要我们去干预。
num_int = 123
num_float = 1.23

# 较低数据类型（整数）就会转换为较高数据类型（浮点数）
result1 = num_int + num_float
print(type(result1))  # <class 'float'>
print(result1)  # 124.23

num_int = 123
num_str = "456"

try:
    # 在JS中下面这种写法可以，但是在Python中无法使用这种运算，无法使用隐式转换
    num_int + num_str
except Exception as e:
    print(e)  # unsupported operand type(s) for +: 'int' and 'str'

# 使用int()将字符串数字强制转换为整数类型
result2 = num_int + int(num_str)
print(result2)  # 579

# 使用str()将数字转换为字符串类型
result3 = str(num_int) + num_str
print(result3)  # 123456

# 定义一个字典类型的数据
dict1 = {'runoob': 'runoob.com', 'google': 'google.com'}
# 通过 repr 函数将字典转换为 字符串格式
res1 = repr(dict1)
print(type(res1), res1)  # <class 'str'> {'runoob': 'runoob.com', 'google': 'google.com'}

# ⭕可以通过eval将字符串字典还原为字典类型的数据
dict2 = eval(res1)
print(type(dict2), dict2)  # <class 'dict'> {'runoob': 'runoob.com', 'google': 'google.com'}

import ast

# ⭕ast.literal_eval() 只解析字面量（如字典、列表、字符串、数字等），比 eval() 更安全。
dict3 = ast.literal_eval(res1)
print(type(dict3), dict3)  # <class 'dict'> {'runoob': 'runoob.com', 'google': 'google.com'}

# 将字符串转换为列表
list1 = list('hello world')
print(list1)  # ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# 将元组转换为list
list2 = list((10, 20, 30))
print(list2)  # [10, 20, 30]

# 字符串转换为集合
set1 = set('hello world')
print(set1)  # {' ', 'w', 'h', 'd', 'e', 'r', 'o', 'l'}

# list转换为集合，自动完成去重
set2 = set(['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'])
print(set2)  # {'l', ' ', 'd', 'e', 'o', 'r', 'h', 'w'}