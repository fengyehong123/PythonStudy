# Series对象的属性和方法非常多，此处仅列出常用的
import pandas as pd

# 创建Series对象
series1 = pd.Series(data=[120, 380, 250, 360], index=['一季度', '二季度', '三季度', '四季度'])

# 获取数据类型
print(series1.dtype)  # int64

# 判断是否有空值
print(series1.hasnans)  # False

# 获取索引
print(series1.index)  # Index(['一季度', '二季度', '三季度', '四季度'], dtype='object')

# 获取值
print(series1.values)  # [120 380 250 360]

# 判断是否单调递增
print(series1.is_monotonic_increasing)  # False

# 判断是值是否唯一
print(series1.is_unique)  # True
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹Series对象支持各种获取描述性统计信息的方法。
"""
# 计数
print(series1.count())  # 4
# 求和
print(series1.sum())  # 1110
# 求平均
print(series1.mean())  # 277.5
# 找中位数
print(series1.median())  # 305.0
# 找最大
print(series1.max())  # 380
# 找最小
print(series1.min())  #  120
# 求标准差
print(series1.std())  # 119.54775893619531
# 求方差
print(series1.var())  # 14291.666666666666
print('\033[91m-----------------------------------------------\033[0m')

# 可以通过 describe() 方法, 一次性获取上述所有的描述性统计信息
print(series1.describe())
"""
count      4.000000
mean     277.500000
std      119.547759
min      120.000000
25%      217.500000
50%      305.000000
75%      365.000000
max      380.000000
dtype: float64
"""
print('\033[91m-----------------------------------------------\033[0m')

# 因为 .describe() 的返回值也是一个 Series对象, 所以也可以像下面这样来获取统计信息
print(series1.describe()['count'])  # 4.0
print(series1.describe()[['max', 'min']])
"""
max    380.0
min    120.0
dtype: float64
"""
print('\033[91m-----------------------------------------------\033[0m')

# 创建有重复值的 Series
series2 = pd.Series(data=['apple', 'banana', 'apple', 'pitaya', 'apple', 'pitaya', 'durian'])
# 获取唯一值的数组
print(series2.unique())  # ['apple' 'banana' 'pitaya' 'durian']
# 获取不重复值的数量
print(series2.nunique())  # 4
"""
    ⏹可以使用value_counts()方法, 统计每个值重复的次数
        方法会返回一个Series对象, 它的索引就是原来的Series对象中的值
        而每个值出现的次数就是返回的Series对象中的数据, 
        在默认情况下会按照出现次数做降序排列
"""
print(series2.value_counts())
"""
apple     3
pitaya    2
banana    1
durian    1
Name: count, dtype: int64
"""
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹空值的判断
        Series对象的 isna() 和 isnull() 方法可以用于空值的判断
        notna() 和 notnull() 方法可以用于非空值的判断
"""
series3 = pd.Series(data=[10, 20, None, 30, None])
# 判断空值
print(series3.isna())
print(series3.isnull())
"""
0    False
1    False
2     True
3    False
4     True
dtype: bool
"""
print('\033[91m===================================================\033[0m')

# 判断非空值
print(series3.notna())
print(series3.notnull())
"""
0     True
1     True
2    False
3     True
4    False
dtype: bool
"""
print('\033[91m===================================================\033[0m')

"""
    ⏹Series对象的 dropna() 和 fillna() 方法分别用来删除空值和填充空值
        dropna()和fillna()方法都有一个名为inplace的参数, 它的默认值是False, 表示删除空值或填充空值不会修改原来的Series对象, 而是返回一个新的Series对象。
        如果将inplace参数的值修改为True, 那么删除或填充空值会就地操作, 直接修改原来的Series对象
"""
# 删除空值【不改变原先的 Series】
print(series3.dropna())
"""
0    10.0
1    20.0
3    30.0
dtype: float64
"""
# 将空值填充为指定的值【不改变原先的 Series】
print(series3.fillna(value=999))
"""
0     10.0
1     20.0
2    999.0
3     30.0
4    999.0
dtype: float64
"""
print('\033[91m===================================================\033[0m')

"""
    ⏹Series对象的
        where() 方法: 将不满足条件的数据替换为指定的值
        mask() 方法: 将满足条件的数据替换为指定的值
"""
series4 = pd.Series(range(5))
# 筛选 > 0 的数据, 将不满足条件的数据 替换为 NaN(默认值)
print(series4.where(series4 > 0))
"""
0    NaN
1    1.0
2    2.0
3    3.0
4    4.0
dtype: float64
"""
print('\033[91m===================================================\033[0m')

# 筛选 > 1 的数据, 不满足条件的数据会被替换为 0
print(series4.where(series4 > 1, 0))
"""
0    0
1    0
2    2
3    3
4    4
dtype: int64
"""
print('\033[91m===================================================\033[0m')

# 筛选 > 2 的数据, 满足条件的数据会被替换为 999
print(series4.mask(series4 > 2, 999))
"""
0      0
1      1
2      2
3    999
4    999
dtype: int64
"""
print('\033[91m===================================================\033[0m')

"""
    ⏹Series对象的
        duplicated() 方法: 可以帮助我们找出重复的数据
        drop_duplicates() 方法: 可以帮我们删除重复数据。
"""
# series2 = pd.Series(data=['apple', 'banana', 'apple', 'pitaya', 'apple', 'pitaya', 'durian'])
print(series2.duplicated())
"""
0    False
1    False
2     True
3    False
4     True
5     True
6    False
dtype: bool
"""
print('\033[91m===================================================\033[0m')

# 通过 .value_counts() 统计重复的次数，然后过滤出 > 1 的数据，然后就可以得到重复的数据重复的次数
print(series2.value_counts()[series2.value_counts() > 1])
"""
apple     3
pitaya    2
Name: count, dtype: int64
"""
print('\033[91m===================================================\033[0m')

# 删除重复的部分之后得到的结果
print(series2.drop_duplicates())
"""
0     apple
1    banana
3    pitaya
6    durian
dtype: object
"""