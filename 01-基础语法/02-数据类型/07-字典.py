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
    列表是有序的对象集合，字典是无序的对象集合。
    字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
    键(key)必须使用不可变类型。
    在同一个字典中，键(key)必须是唯一的。
"""

# ⭕创建一个空字典
dict1 = {}
print(type(dict1))  # <class 'dict'>
print(type(dict()))  # <class 'dict'>

# 初始化一个含有数据的字典
dict2 = {
    "name": '贾飞天',
    "age": 18,
    'address': '地球',
    'hobby': ['吃饭', '睡觉', '唱歌']
}
print(dict2)  # {'name': '贾飞天', 'age': 18, 'address': '地球', 'hobby': ['吃饭', '睡觉', '唱歌']}

# ⭕向字典内添加数据
dict2['work'] = '码农'
print(dict2['work'])  # 码农

# ⭕获取所有的key
print(dict2.keys())  # dict_keys(['name', 'age', 'address', 'hobby', 'work'])
# ⭕获取所有的value
print(dict2.values())  # dict_values(['贾飞天', 18, '地球', ['吃饭', '睡觉', '唱歌'], '码农'])

# ⭕查看字典key的数量
print(len(dict2))  # 5

# ⭕删除字典中对应的key
del dict2['work']
print(dict2)  # {'name': '贾飞天', 'age': 18, 'address': '地球', 'hobby': ['吃饭', '睡觉', '唱歌']}

# ⭕获取键对应的值，如果不存在的话，则使用默认值
val1 = dict2.get('work', '默认值...')
print(val1)  # 默认值...

# ⭕判断字典中是否含有key
if not 'work' in dict2:
    print('work这个key在字典中根本不存在')  # work这个key在字典中根本不存在

# 获取字典的key的可迭代对象
var_keys = dict2.keys()
print(var_keys)  # dict_keys(['name', 'age', 'address', 'hobby'])
print(type(var_keys))  # <class 'dict_keys'>
for key in var_keys:
    print(f"字典中的key的值为:{key}")
    # 字典中的key的值为:name
    # 字典中的key的值为:age
    # 字典中的key的值为:address
    # 字典中的key的值为:hobby

# ⭕获取可迭代对象，并转换为list
var_list = list(dict2.keys())
print(type(var_list))  # <class 'list'>
print(var_list)  # ['name', 'age', 'address', 'hobby']

# ⭕获取字典的value的可迭代对象并转换为list
print(list(dict2.values()))  # ['贾飞天', 18, '地球', ['吃饭', '睡觉', '唱歌']]

# ⭕获取整个字典的可迭代对象
var_items = dict2.items()
print(var_items)  # dict_items([('name', '贾飞天'), ('age', 18), ('address', '地球'), ('hobby', ['吃饭', '睡觉', '唱歌'])])

# ⭕遍历整个字典
for key, value in dict2.items():
    print(f"字典的key是:{key},字典的value是:{value}")
    # 字典的key是:name,字典的value是:贾飞天
    # 字典的key是:age,字典的value是:18
    # 字典的key是:address,字典的value是:地球
    # 字典的key是:hobby,字典的value是:['吃饭', '睡觉', '唱歌']

# 定义一个字典
dict3 = {
    "new_name": 'AA',
    "new_age": 28
}

# ⭕将字典2的内容更新到字典3中
dict3.update(dict2)
print(dict3)  # {'new_name': 'AA', 'new_age': 28, 'name': '贾飞天', 'age': 18, 'address': '地球', 'hobby': ['吃饭', '睡觉', '唱歌']}

# ⭕判断字典是否为空
if len(dict2) == 0:
    print('---字典为空---')

# ⭕清空字典
dict2.clear()

# ⭕判断字典是否为空
if not dict2:
    print('+++字典为空+++')  # +++字典为空+++

# 彩色打印内容到控制台
print('\033[91m-----------------------------------------------\033[0m')

dict4 = {
    "name": '贾飞天',
    "age": 18,
    'hobby': ['吃饭', '睡觉', '唱歌']
}

# ⭕通过字典的copy方法复制一个对象
dict5 = dict4.copy()
# 原先的字典修改不可变类型的数据
dict4['name'] = '枫叶红'
# 原先的字典修改可变类型的数据
dict4['hobby'][0] = '进食'

print(dict4)  # {'name': '枫叶红', 'age': 18, 'hobby': ['进食', '睡觉', '唱歌']}
# 可以看到复制之后的对象中不可变类型的数据并不受原对象的修改的影响，但是可变类型的数据会受到其影响
print(dict5)  # {'name': '贾飞天', 'age': 18, 'hobby': ['进食', '睡觉', '唱歌']}

# 引入Python的copy模块
import copy

# ⭕通过Python的copy模块进行深拷贝
dict5 = copy.deepcopy(dict4)
print(dict5)  # {'name': '枫叶红', 'age': 18, 'hobby': ['进食', '睡觉', '唱歌']}

dict4['age'] = 100
dict4['hobby'][0] = '开车'
print(dict4)  # {'name': '枫叶红', 'age': 100, 'hobby': ['开车', '睡觉', '唱歌']}

# 可以看到深拷贝之后的字典对象并不受原先对象的影响
print(dict5)  # {'name': '枫叶红', 'age': 18, 'hobby': ['进食', '睡觉', '唱歌']}

print('\033[91m-----------------------------------------------\033[0m')

# 通过传入关键字创建字典
print(dict(name = '张三', age = 100))  # {'name': '张三', 'age': 100}

# 创建两个list
listA = ['one', 'two', 'three']
listB = [1, 2, 3]

# 映射函数的方式来创建字典
dict6 = dict(zip(listA, listB))
print(dict6)  # {'one': 1, 'two': 2, 'three': 3}

# 创建3个元组
tuple1 = ('姓名', '李四')
tuple2 = ('年龄', '20')
tuple3 = ('爱好', ['吃饭', '睡觉', '爬山'])

# 通过可迭代对象的方式来创建字典
dict7 = dict([tuple1, tuple2, tuple3])
print(dict7)  # {'姓名': '李四', '年龄': '20', '爱好': ['吃饭', '睡觉', '爬山']}
