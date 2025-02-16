"""
    菜鸟教程资料
    1. https://www.runoob.com/pandas/pandas-csv-file.html
"""
import time
import pandas as pd
from csv import QUOTE_ALL
from pathlib import Path

# csv文件名称
csvFileName = "output.csv"

# 创建一个示例 DataFrame
data = {
    # csv文件的表头和表头对应的数据
    "Name": ["Alice", "Bob", "贾飞天"],
    "Age": [25, 30, 32],
    "City": ["New York", "Los Angeles", "地球"]
}
dataFrame = pd.DataFrame(data)

"""
    ⏹写入CSV文件
    index=False
        用于防止将 DataFrame 的索引写入csv文件
    quotechar='"'
        csv的分隔符
    quoting=QUOTE_ALL
        对所有的字段都添加双引号
"""
dataFrame.to_csv(csvFileName, index=False, encoding="utf-8", quotechar='"', quoting=QUOTE_ALL)
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹读取csv文件
    header=None
        如果csv文件没有表头的话, 使用该参数后, pandas 会为每列自动分配默认列名
"""
df = pd.read_csv(csvFileName, encoding="utf-8", header=None)
print(df)
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹如果没有表头或者需要指定自定义的列名, 可以使用 names 参数
"""
columns = ["列1", "列2", "列3"]
df = pd.read_csv(csvFileName, names=columns, header=None)
print(df)
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹筛选出 Age > 25 岁的人的数据
"""
dataFrame = pd.read_csv(csvFileName, encoding="utf-8")
result1 = dataFrame[dataFrame['Age'] > 25]
print(result1)
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹只获取出csv文件的指定的列
"""
dataFrame = pd.read_csv(csvFileName, usecols=["Name", "City"])
print(dataFrame)
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹只读取csv文件的前5行
"""
dataFrame = pd.read_csv(csvFileName, nrows=5)
print(dataFrame)
print('\033[91m-----------------------------------------------\033[0m')

"""
    ⏹跳过csv文件的前2行
"""
print(pd.read_csv(csvFileName, skiprows=2))
print('\033[91m-----------------------------------------------\033[0m')

time.sleep(2)
csvPath = Path(csvFileName)
if csvPath.exists():
    csvPath.unlink()
    print("csv文件删除成功")
