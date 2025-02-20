# 定义一个比较大小的函数
def custom_max(a, b):
    if a > b:
        return a
    return b
print(custom_max(10, 20))  # 20

a = 20
b = [1, 2, 3]

# 参数传递，不可变类型
def change1(a):
    a = 10
    return

# 数字是不可变类型，因此函数内部对a的修改相当于重新生成了一个a，和外部的a没有任何关系
change1(a)
print(a)  # 20

# 参数传递，可变类型
def change2(b):
    b.append(1000)
    return

# 列表是可变类型，因此函数内部对b的修改会影响到外部
change2(b)
print(b)  # [1, 2, 3, 1000]

# 定义一个带参数的函数
def fun1(a):
    print("hello world...")

try:
    # 和Js不同，在Python中如果函数定义了参数，那就一定要传入，否则会报错
    fun1()
except Exception as e:
    print(e)
# 传一个 None，可避免函数报错
fun1(None)

# 关键字参数和默认参数
def printInfo(name, age = 20):
    print(f"姓名是: {name},年龄是: {age}")

# 因为有了默认参数，所以只传入一个参数也是可以的
printInfo("贾飞天")  # 姓名是: 贾飞天,年龄是: 20

# 也可以像下面这样，指定函数的名称进行传入，这样的话就不用在意函数参数的位置了
printInfo(age = 100, name = '张三')  # 姓名是: 张三,年龄是: 100

"""
    不定长参数，添加了 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
"""
def printInfo1(info1, info2, *tupleInfo):
    print(f"参数info1的值为: {info1}")  # 参数info1的值为: 你好
    print(f"参数info2的值为: {info2}")  # 参数info2的值为: 我好
    print(f"参数tupleInfo的值为: {tupleInfo}")  # 参数tupleInfo的值为: (123, 'ppp', [4, 5, 6])
printInfo1("你好", "我好", 123, "ppp", [4, 5, 6])

"""
    不定长参数，添加了 ** 的参数会以字典的形式导入。
"""
def printInfo2(info1, info2, **dictInfo):
    print(f"参数info1的值为: {info1}")  # 参数info1的值为: 你好
    print(f"参数info2的值为: {info2}")  # 参数info2的值为: 我好
    print(f"参数dictInfo的值为: {dictInfo}")  # 参数dictInfo的值为: {'key1': 123, 'key2': 'ppp', 'key3': [4, 5, 6]}
printInfo2("你好", "我好", key1 = 123, key2 = "ppp", key3 = [4, 5, 6])
print('\033[91m-----------------------------------------------\033[0m')

# 🔴当函数返回多个值的时候，会自动封装为元组的形式返回
def getInfoList():
    return {"name": "贾飞天"}, 20, "你好"
result1 = getInfoList()

print(type(result1))  # <class 'tuple'>
print(result1)  # ({'name': '贾飞天'}, 20, '你好')