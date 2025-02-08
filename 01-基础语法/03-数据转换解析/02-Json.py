# 导入json模块
import json

# 定义一个字典类型
dict1 = {
    "name": '贾飞天',
    "age": 18,
    'hobby': ['吃饭', '睡觉', '唱歌']
}

# 转换为json字符串
json_str1 = json.dumps(dict1)
# json.dumps() 默认参数 ensure_ascii=True，会将所有非 ASCII 字符转换成 \uXXXX 形式。
print(json_str1)  # {"name": "\u8d3e\u98de\u5929", "age": 18, "hobby": ["\u5403\u996d", "\u7761\u89c9", "\u5531\u6b4c"]}

# 通过指定 ensure_ascii=False 来保证中文正常显示
json_str2 = json.dumps(dict1, ensure_ascii=False)
print(type(json_str2), json_str2)  # <class 'str'> {"name": "贾飞天", "age": 18, "hobby": ["吃饭", "睡觉", "唱歌"]}

# 将Json字符串转换为Python对象
dict2 = json.loads('{"name": "贾飞天", "age": 18, "hobby": ["吃饭", "睡觉", "唱歌"]}')
print(type(dict2), dict2)  # <class 'dict'> {'name': '贾飞天', 'age': 18, 'hobby': ['吃饭', '睡觉', '唱歌']}