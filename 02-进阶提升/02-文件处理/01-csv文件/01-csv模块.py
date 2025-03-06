import csv
import time
from pathlib import Path

# csv数据
csvData = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"]
]

# csv文件的名称
csvFileName = 'output.csv'

# open方法参数
paramDict = {
    'file': csvFileName,
    'mode': 'w',
    'newline': "",
    'encoding': 'utf-8'
}

# ⏹向CSV文件内写入数据
with open(**paramDict) as file:
    # 给csv文件的每个字段都加上双引号
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    # 批量写入多行
    writer.writerows(csvData)

"""
    ⏹读取csv文件的数据为列表
"""
with open(csvFileName, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for rowList in reader:
        # 每行是一个列表
        print(rowList)
        # ['Name', 'Age', 'City']
        # ['Alice', '25', 'New York']
        # ['Bob', '30', 'Los Angeles']

"""
    ⏹读取csv文件的数据为字典
"""
with open(csvFileName, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for rowDict in reader:
        # 每行是一个字典
        print(rowDict)
        # {'Name': 'Alice', 'Age': '25', 'City': 'New York'}
        # {'Name': 'Bob', 'Age': '30', 'City': 'Los Angeles'}

# 睡眠2秒之后，删除刚创建好的csv文件
time.sleep(2)
csvPath = Path(csvFileName)
if csvPath.exists():
    csvPath.unlink()

