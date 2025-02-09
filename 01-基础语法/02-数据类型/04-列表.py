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

# ⏹在Python中，列表中元素的类型可以不相同，它支持数字，字符串甚至可以包含列表（所谓嵌套）。

# 定义两个列表
list1 = ['abcd', 786 , 2.23, 'runoob', [1, 3, 5]]
list2 = [3, 3, 6, 8]

# 打印列表的第一个元素
print(list1[0])  # abcd
# 打印列表第二到第四个元素（不包含第四个元素）
print(list1[1:3])  # [786, 2.23]
# 打印列表从第三个元素开始到末尾
print(list1[2:])  # [2.23, 'runoob', [1, 3, 5]]

# ⭕两个列表拼接,合并为一个列表
list3 = list1 + list2
print(list3)  # ['abcd', 786, 2.23, 'runoob', [1, 3, 5], 3, 3, 6, 8]

# ⭕修改列表的元素
list1[0] = '贾飞天'
print(list1[0])  # 贾飞天

# ⭕批量修改列表的第2到第4个元素
list1[1:4] = ['张三', '李四', '王五']
print(list1)  # ['贾飞天', '张三', '李四', '王五', [1, 3, 5]]

print('\033[91m----------------------------------------------------------------------------------------------\033[0m')

list3 = [11, 12, 12]

# 向列表中添加元素
list3.append(13)
print(list3)  # [11, 12, 12, 13]

# 统计列表的元素数量
print(len(list3))  # 4

# 统计某个元素在列表中出现的次数
print(list3.count(12))  # 2

# 向列表的末尾一次性追加多个值
list3.extend(list(range(99, 101)))
print(list3)  # [11, 12, 12, 13, 99, 100]

# 查找对应元素的下标
print(list3.index(99))  # 4

# 向第1个下标插入数据
list3.insert(0, {"name": '你好'})
print(list3)  # [{'name': '你好'}, 11, 12, 12, 13, 99, 100]

# 移除列表的一个值，并返回(默认移除最后一个值)
res1 = list3.pop()
print(list3)  # [{'name': '你好'}, 11, 12, 12, 13, 99]
print(res1)  # 100

# 移除列表的下标为0的元素，并返回值
res2 = list3.pop(0)
print(list3)  # [11, 12, 12, 13, 99]
print(res2)  # {'name': '你好'}

list4 = ['百度', '谷歌', '百度', '必应', '搜狗']

# remove只会移除第一个被匹配到的值
list4.remove('百度')
print(list4)

# 列表的复制
print(list4.copy())  # ['谷歌', '百度', '必应', '搜狗']
print(list4[:])  # ['谷歌', '百度', '必应', '搜狗']

# 清空列表
list4.clear()
print(len(list4))  # 0

# 引入比较模块
import operator

lia = [1, 2, 3]
lib = [1, 2, 3]
lic = ['1', '2', '3']

# 列表的比较
print(operator.eq(lia, lib))  # True
print(operator.eq(lia, lic))  # False