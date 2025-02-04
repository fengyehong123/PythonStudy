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

# ⏹Python中的布尔值
# Python3 中，bool 是 int 的子类，True 和 False 可以和数字相加， 
# True==1、False==0 会返回 True，但可以通过 is 来判断类型。
print(True == 1 and False == 0)  # True
print(issubclass(bool, int))  # True

# ⏹Python中的字符串
str1 = 'wuy.cctv.com'

# 打印字符串的第一个字符
print(str1[0])  # w
# 打印字符串的第3到第5个字符
print(str1[2:5])  # y.c
# 打印从第3个字符开始到末尾
print(str1[2:])  # y.cctv.com
# 打印字符串第1个到倒数第2个字符（不包含倒数第1个字符）
print(str1[0:-1])  # wuy.cctv.co

# Python中的字符串不能被改变
try:
    str1[0] = "U"
except Exception as e:
    print(e)  # 'str' object does not support item assignment

# Python中使用 """ 表示多行字符串
str2 = """你好
这个世界
哈哈哈
"""
print(str2)

# \ 表示转义符
str3 = "你好\",这个世界!"
print(str3)  # 你好",这个世界!

# 如果不想让字符串发生转义，可以在字符串前面添加一个 r ,用来表示原始字符串
print(r"你好\",这个世界!")  # 你好\",这个世界!

name1 = "贾飞天"
age1 = 100

# ⭕str.format()方法进行字符串格式化
str4 = "我的名字叫{},我今年{}岁了".format(name1, age1)
print(str4)  # 我的名字叫贾飞天,我今年100岁了
# 支持位置参数
print("我的名字叫{1},我今年{0}岁了".format(80, "张三"))  # 我的名字叫张三,我今年80岁了
# 支持关键词参数
print("我的名字叫{name_1},我今年{age_1}岁了".format(name_1 = "李四", age_1 = "60"))  # 我的名字叫李四,我今年60岁了
# 支持格式化
print("我现在的余额还有{:.2f}元".format(25.5687))  # 我现在的余额还有25.57元

# ⭕Python 3.6+之后的版本, 使用 f-string 进行格式化
# 在字符串前直接添加一个 f 即可，用法更加的简单了
print(f"我的名字叫{name1},我今年{age1}岁了")  # 我的名字叫贾飞天,我今年100岁了
# 支持使用表达式
def get_money():
    return 2 + 3
print(f"我现在的余额为: {get_money()}")  # 我现在的余额为: 5
# 同样也支持格式化
money1 = 35.5454
print(f"我现在的余额还有{money1:.2f}元")  # 我现在的余额还有35.55元

# ⭕如果使用 f-string 或 .format()，且字符串格式化的内容来自用户输入
# 攻击者可能会注入恶意代码，导致执行任意 Python 代码。
# 这种情况下，可以使用更加适用于处理用户输入的安全场景的 Template
from string import Template
# 使用 Template 构造一个模板
str5 = Template("我的名字叫$name, 我今年$age岁了")
print(str5.safe_substitute(name = "枫叶红", age = 56))