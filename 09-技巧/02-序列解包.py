import tempfile

"""
    ⏹字典
"""
# 将参数放入字典进行封装
temp_file_params = {
    'mode': 'w+',
    'encoding': 'utf-8',
    'prefix': 'my_temp_',
    'suffix': '.txt',
    'delete': False
}
# 通过 kwargs 的方式对字典进行解包，简化代码
with tempfile.NamedTemporaryFile(**temp_file_params) as temp_file:

    # 获取临时文件的路径
    filePath = temp_file.name
    print(f"临时文件名：{filePath}")

    # 写入数据之后,将文件的指针放到文件的开头
    temp_file.write(f"我是 → {filePath} 文件中的临时数据")
    temp_file.seek(0)

    # 读取数据
    print(temp_file.read())

dict1 = {
    "name": "贾飞天",
    "age": 18,
    "hobby": ["吃饭", "睡觉", "打豆豆"]
}
# 进行解包
name, age, hobby = dict1.values()
print(name)  # 贾飞天
print(age)  # 18
print(hobby)  # ['吃饭', '睡觉', '打豆豆']

# 🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴

"""
    ⏹列表
"""
arr1 = [10, 20, 30]

# 类似于JS中的解构赋值
num1, num2, num3 = arr1
print(num1, num2, num3)  # 10 20 30

# 可以通过 _ 来忽略某些不需要的值
num4, _, num5 = arr1
print(num4, num5)  # 10 30

# 剩余变量
num6, *resut = arr1
print(num6)  # 10
print(*resut)  # 20 30

img_url_list = [
    "www.cc1.jpg",
    "www.cc2.jpg",
    "www.cc3.jpg"
]
print(*img_url_list, sep='\n')
# www.cc1.jpg
# www.cc2.jpg
# www.cc3.jpg

# 🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴

"""
    ⏹函数
"""
def getInfo(name, age, hobby):
    print(name)  # 枫叶红
    print(age)  # 100
    print(hobby)  # ['学习', '看书', '写代码']

paramList = ["枫叶红", 100, ["学习", "看书", "写代码"]]
getInfo(*paramList)