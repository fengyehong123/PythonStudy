import pandas as pd

"""
    Series对象的apply()和map()方法非常重要，它们可以通过字典或者指定的函数来处理数据，
    把数据映射或转换成我们想要的样子。这两个方法在数据准备阶段非常重要
"""
series1 = pd.Series(['cat', 'dog', None, 'rabbit'])

# 通过字典给出的映射规则对数据进行处理
print(series1.map({'cat': '小猫猫', 'dog': '小狗狗'}))
"""
0    小猫猫
1    小狗狗
2    NaN
3    NaN
dtype: object
"""
print('\033[91m-----------------------------------------------\033[0m')

# 将指定字符串的format方法作用到数据系列的数据上，忽略掉所有的空值。
# 如果我们不通过 na_action='ignore' 来忽略空值的话, 【我是一个 None】也会被打印出来
print(series1.map('我是一个 {}'.format, na_action='ignore'))
"""
0       我是一个 cat
1       我是一个 dog
2           None
3    我是一个 rabbit
dtype: object
"""
print('\033[91m-----------------------------------------------\033[0m')

# 对每个元素应用平方函数
series2 = pd.Series([20, 21, 12],  index=['一季度', '二季度', '三季度'])
print(series2.apply(lambda x: x ** 2))
"""
一季度    400
二季度    441
三季度    144
dtype: int64
"""
print('\033[91m-----------------------------------------------\033[0m')

"""
    下面apply方法中的lambda函数有两个参数, 第一个参数是数据系列中的数据
    而第二个参数需要我们传入, 所以我们给apply方法增加了args参数, 用于给lambda函数的第二个参数传值。
"""
print(series2.apply(lambda x, value: x - value, args=(5, )))
"""
一季度    15
二季度    16
三季度     7
dtype: int64
"""
print('\033[91m-----------------------------------------------\033[0m')

"""
    Series对象的
        sort_index()
        sort_values()
    方法可以用于对索引和数据的排序

    排序方法中
        ascending的布尔类型参数, 该参数用于控制排序的结果是升序还是降序
        kind的参数则用来控制排序使用的算法, 默认使用了quicksort, 也可以选择mergesort或heapsort
        如果存在空值, 那么可以用 na_position 参数空值放在最前还是最后, 默认是last
"""

series3 = pd.Series(
    data=[35, 96, 12, 57, 25, 89], 
    index=['grape', 'banana', 'pitaya', 'apple', 'peach', 'orange']
)
# 按值从小到大排序
print(series3.sort_values())
"""
pitaya    12
peach     25
grape     35
apple     57
orange    89
banana    96
dtype: int64
"""
print('\033[91m-----------------------------------------------\033[0m')

"""
    如果要从Series对象中找出元素中最大或最小的 Top-N
    我们不需要对所有的值进行排序的, 可以使用
        nlargest()
        nsmallest()
"""

# 值最大的3个
print(series3.nlargest(3))
"""
banana    96
orange    89
apple     57
dtype: int64
"""

# 值最小的2个
print(series3.nsmallest(2))
"""
pitaya    12
peach     25
dtype: int64
"""