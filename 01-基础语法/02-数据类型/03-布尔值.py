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

# ⏹Python中的布尔值
# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加
# 布尔类型可以和其他数据类型进行比较，比如数字、字符串等。
# 在比较时，Python 会将 True 视为 1，False 视为 0。
# True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(True == 1 and False == 0)  # True
print(issubclass(bool, int))  # True

print(int(True))   # 1
print(int(False))  # 0

"""
可以使用 bool() 函数将其他类型的值转换为布尔值。
以下值在转换为布尔值时为 False:
    None
    False
    零 (0、0.0、0j)
    空序列 → ''、()、[]
    空映射 → {}
其他所有值转换为布尔值时均为 True
"""
print(bool(0))         # False
print(bool(42))        # True
print(bool(''))        # False
print(bool('Python'))  # True
print(bool([]))        # False
print(bool([1, 2, 3])) # True