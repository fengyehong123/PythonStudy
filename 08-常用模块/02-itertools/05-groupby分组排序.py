from itertools import groupby

# 有如下数据
data = [('A', 1), ('A', 2), ('B', 3), ('B', 4), ('B', 5), ('C', 6)]

# 定义一个获取key的匿名函数
keyItem = lambda x: x[0]

# 在 groupby 之前必须要先排序, 指定使用key进行排序
data.sort(key=keyItem)

# 通过key进行分组
for key, group in groupby(data, key=keyItem):
    print(f"Key: {key} → Value: {list(group)}")
    # Key: A → Value: [('A', 1), ('A', 2)]
    # Key: B → Value: [('B', 3), ('B', 4), ('B', 5)]
    # Key: C → Value: [('C', 6)]