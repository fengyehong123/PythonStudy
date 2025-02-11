"""
    Python 推导式是一种独特的数据处理方式，可以从一个数据序列构建另一个新的数据序列的结构体。
    Python 推导式是一种强大且简洁的语法，适用于生成列表、字典、集合和生成器。
    在使用推导式时，需要注意可读性，尽量保持表达式简洁，以免影响代码的可读性和可维护性。

    Python 支持各种数据结构的推导式：
        列表(list)推导式
        字典(dict)推导式
        集合(set)推导式
        元组(tuple)推导式
"""

names = ['Bob','Tom','alice','Jerry','Wendy','Smith']

# 使用推导式之前
new_names1 = []
for name in names:
    if len(name) > 3:
        new_names1.append(name.upper())
print(new_names1)  # ['ALICE', 'JERRY', 'WENDY', 'SMITH']

# 使用列表推导式之后，语法更加简洁
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)  # ['ALICE', 'JERRY', 'WENDY', 'SMITH']

# 字典推导式
listCompany = ['Google','Baidu', 'Taobao']
dictCompany = {company: len(company) for company in listCompany}
print(dictCompany)  # {'Google': 6, 'Baidu': 5, 'Taobao': 6}

# 集合推导式，判断不是 abc 的字母并输出
set1 = {x for x in 'abracadabra' if x not in 'abc'}
print(set1)

# 元组的推导式返回的是一个生成器
tmp = (x.upper() for x in listCompany)
print(type(tmp))  # <class 'generator'>
# 可以使用 tuple() 函数，可以直接将生成器对象转换成元组
tuple1 = tuple(tmp)
print(tuple1)  # ('GOOGLE', 'BAIDU', 'TAOBAO')