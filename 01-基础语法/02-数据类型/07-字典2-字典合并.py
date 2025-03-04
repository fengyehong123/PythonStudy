"""
    字典的合并
"""

# 定义两个字典
personDict1 = {
    "id": "110",
    "name": "贾飞天",
    "address": "第一宇宙银河系太阳系地球"
}
personDict2 = {
    "id": "120",
    "name": "贾飞天",
    "age": 18
}

# Python 3.9+ 的语法, 如果key相同, 以第2个为主
merged_dict1 = personDict1 | personDict2
print(merged_dict1)  # {'id': '120', 'name': '贾飞天', 'address': '第一宇宙银河系太阳系地球', 'age': 18}

# 兼容 Python 3.5+ 的写法
merged_dict2 = {**personDict2, **personDict1}
print(merged_dict2)  # {'id': '110', 'name': '贾飞天', 'age': 18, 'address': '第一宇宙银河系太阳系地球'}