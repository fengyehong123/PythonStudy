"""
    Pandas 核心的数据类型是
        1. Series(数据系列)
        2. DataFrame(数据窗/数据框)
    分别用于处理一维和二维的数据
    除此之外, 还有一个名为Index的类型及其子类型, 它们为Series和DataFrame提供了索引功能。
    
    日常工作中DataFrame使用得最为广泛, 因为二维的数据结构刚好可以对应有行有列的表格。
    Series和DataFrame都提供了大量的处理数据的方法, 数据分析师以此为基础
    可以实现对数据的筛选、合并、拼接、清洗、预处理、聚合、透视和可视化等各种操作。

    ⏹Series介绍
    Series 是 Pandas 中的一个核心数据结构, 类似于一个一维的数组, 具有数据和索引。
    Series 可以存储任何数据类型（整数、浮点数、字符串等）, 并通过标签（索引）来访问元素。
    Series 的数据结构是非常有用的, 因为它可以处理各种数据类型, 同时保持了高效的数据操作能力, 比如可以通过标签来快速访问和操作数据。

    ⏹Series 特点: 
        1. 一维数组: Series 中的每个元素都有一个对应的索引值。
        2. 索引: 每个数据元素都可以通过标签（索引）来访问, 默认情况下索引是从 0 开始的整数, 但你也可以自定义索引。
        3. 数据类型:  Series 可以容纳不同数据类型的元素, 包括整数、浮点数、字符串、Python 对象等。
        4. 大小不变性: Series 的大小在创建后是不变的, 但可以通过某些操作 (如 append 或 delete) 来改变。
        5. 操作: Series 支持各种操作, 如数学运算、统计分析、字符串处理等。
        6. 缺失数据: Series 可以包含缺失数据, Pandas 使用NaN (Not a Number) 来表示缺失或无值。
        7. 自动对齐: 当对多个 Series 进行运算时, Pandas 会自动根据索引对齐数据, 这使得数据处理更加高效。
    
    ⏹pandas 需要 numpy 来处理数据，例如：
        1. DataFrame 和 Series 的底层数据存储使用 numpy 数组。
        2. 许多数学运算都依赖 numpy 进行高效计算。
        3. 当我们安装 pandas 的时候，作为依赖的 numpy 也会被一并安装
"""
import pandas as pd

"""
    创建一个 Series 对象, 指定名称为A, 指定值为【1, 2, 3, 4】
    由于没有指定索引, 因此默认索引为【0, 1, 2, 3】
"""
series1 = pd.Series([1, 2, 3, 4], name='A')
print(series1)
"""
0    1
1    2
2    3
3    4
Name: A, dtype: int64
"""

# 还可以自定义索引
series2 = pd.Series(data=[120, 380, 250, 360], index=['一季度', '二季度', '三季度', '四季度'])
print(series2)
"""
一季度    120
二季度    380
三季度    250
四季度    360
dtype: int64
"""
print(f"第3个季度的值是: {series2["三季度"]}")  # 第3个季度的值是: 250

# 还可以通过字典来创建
dict1 = {
    'A季度': "320元",
    'B季度': "180元",
    'C季度': "300元",
    'D季度': "405元"
}
series3 = pd.Series(dict1)
print(series3)
"""
A季度    320元
B季度    180元
C季度    300元
D季度    405元
dtype: object
"""
