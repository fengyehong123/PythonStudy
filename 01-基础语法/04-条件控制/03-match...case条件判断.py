"""
    Python 3.10 增加了 match...case 的条件判断
"""

# 定义一个函数
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "418状态码..."
        case 500|501|502:
            return "500~502的状态码"
        case _:
            return "其他的状态码"

print(http_error(404))  # Not found
print(http_error(501))  # 500~502的状态码
print(http_error(605))  # 其他的状态码

"""
    match case可以匹配数据结构
"""
# ⭕匹配元组
def parse_tuple(data):
    match data:
        # 相当于解构元组, *_ 表示忽略剩余的元素
        case (x, y, *_):
            return f"匹配到元组: x={x}, y={y}"
        case _:
            return "不是元组"

print(parse_tuple((10, 20, 30)))  # 匹配到元组: x=10, y=20
print(parse_tuple("Hello World"))  # 不是元组

# ⭕匹配列表
def parse_list(lst):
    match lst:
        case [first, second, *_]:
            return f"前两个元素: {first}, {second}"
        case []:
            return "空列表"
        case _:
            return "其他情况"

print(parse_list([1, 2, 3, 4]))  # 前两个元素: 1, 2
print(parse_list([]))  # 空列表

# ⭕匹配字典
def parse_dict(dict):
    match dict:
        case {"name": name, "age": age}:
            return f"名字: {name}, 年龄: {age}"
        case _:
            return "不是期望的字典结构"

dict1 = {
    "name": "张三"
    , "age": 25
}
print(parse_dict(dict1))  # 名字: 张三, 年龄: 25
