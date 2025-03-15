import pandas as pd

# 通过数组和字典，并且指定索引来创建 Series 对象
series1 = pd.Series(data=[120, 380, 250, 360], index=['一季度', '二季度', '三季度', '四季度'])
series2 = pd.Series({'一季度': 320, '二季度': 180, '三季度': 300, '四季度': 405})

# ⏹给Series中的每个季度都加上10
series2 = series2 + 10
print(series2)
"""
一季度    330
二季度    190
三季度    310
四季度    415
dtype: int64
"""

# ⏹将两个Series对应的季度的数据加起来
print(series1 + series2)
"""
一季度    450
二季度    570
三季度    560
四季度    775
dtype: int64
"""
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹数据获取
        跟数组一样, Series对象也可以进行索引和切片操作, 不同的是Series对象因为内部维护了一个保存索引的数组
        所以除了可以使用整数索引检索数据外，还可以通过自己设置的索引（标签）获取对应的数据。
"""
# 明确指定通过整数索引获取数据
print(series2.iloc[1])  # 190
# 通过自定义索引获取数据
print(series2["二季度"])  # 190

"""
    ⏹切片索引
        Series对象的切片操作跟列表、数组类似, 通过给出起始和结束索引
        从原来的Series对象中取出或修改部分数据, 这里也可以使用整数索引和自定义的索引
"""
# 通过整数索引来切片二三季度的数据
print(series2.iloc[1:3])
"""
二季度    190
三季度    310
dtype: int64
"""
# 通过自定义索引来切片二三季度的数据
print(series2['二季度':'三季度'])
"""
二季度    190
三季度    310
dtype: int64
"""
# 获取第一和第四季度的数据
print(series2[['一季度', '四季度']])
print('\033[91m-----------------------------------------------\033[0m')
"""
一季度    330
四季度    415
dtype: int64
"""
# 布尔索引
print(series2[series2 > 319])
"""
一季度    330
四季度    415
dtype: int64
"""