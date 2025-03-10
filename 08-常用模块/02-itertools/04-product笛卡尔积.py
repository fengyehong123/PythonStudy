from itertools import product

colors = ["红", "蓝"]
sizes = ["S", "M", "L"]

# 通过 product 来获取两个list的笛卡尔积
list1 = [pair for pair in product(colors, sizes)]
print(list1)  # [('红', 'S'), ('红', 'M'), ('红', 'L'), ('蓝', 'S'), ('蓝', 'M'), ('蓝', 'L')]