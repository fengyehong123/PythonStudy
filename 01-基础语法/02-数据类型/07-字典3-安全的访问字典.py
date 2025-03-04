# Python中有两种访问字典的方式 dict_name['key'] 和 dict_name.get('key')
from collections import defaultdict

d = {
    'name': "Python",
    'age': 27,
    'version': 3.6
}

# 当字典的键不存在的时候会报错
# print(d['nam'])

# 当字典的键不存在的时候不会报错,会报None
print(d.get('nam'))  # None

# 可以指定一个默认值,当键不存在的时候,会取出指定的默认的value
print(d.get('nam', '我是一个默认值'))  # 我是一个默认值

# 使用默认字典
e = {
    'name': "Python",
    'age': 27,
    'version': 3.6
}

new_obj = defaultdict(lambda: "我只是一个字典的默认值", e)
# 通过.get()获取存在的键
print(new_obj.get('name'))  # Python
# 通过.get()获取不存在的键
print(new_obj.get("nam"))  # None

# 通过普通的方式获取值
print(new_obj["age"])  # 27
# 通过普通方式获取不存在的键
print(new_obj["age!"])  # 我只是一个字典的默认值