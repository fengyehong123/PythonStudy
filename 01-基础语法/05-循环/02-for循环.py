"""
    基本语法
        for 变量 in 可迭代对象:
            代码块
"""

# 遍历列表
for fruit in ["苹果", "香蕉", "橘子", "哈哈"]:
    if fruit == '香蕉':
        # for循环里面的 continue
        continue
    elif fruit == '橘子':
        print(fruit)
        # for循环里面的 break
        break
    print(fruit)

# 使用 enumerate() 获取索引
for index, fruit in enumerate(["苹果", "香蕉", "橘子"]):
    print(f"当前水果为:{fruit},当前水果对应的下标为:{index}")

# 遍历字符串
for charStr in "Python":
    print(charStr)

# 遍历 range
for num in range(2, 10, 2):
    print(num)

# 遍历字典
person = {
    "name": "张三"
    , "age": 25
    , "city": "东京"
}
for key, value in person.items():
    print(f"字典的key是:{key},字典的value是:{value}")

# 使用zip()来遍历多个序列
fruitEnglishList = ["苹果", "香蕉", "橘子"]
fruitJapanList = ["リンゴ", "バナナ", "ミカン"]
for fruitEnglish, fruitJapan in zip(fruitEnglishList, fruitJapanList):
    print(f"水果的英文名为: {fruitEnglish},水果的日文名为: {fruitJapan}")
else:
    print("该for循环执行完毕...")