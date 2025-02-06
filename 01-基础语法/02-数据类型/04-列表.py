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

