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