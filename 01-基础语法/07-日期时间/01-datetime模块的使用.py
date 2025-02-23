"""
    Python 内置的 datetime 模块用于处理日期和时间
    包括获取当前时间、格式化、计算时间差等。
"""
from datetime import datetime

# 🔴获取当前的时间
nowTime = datetime.now()
# 可以看到,得到的是一个日期对象
print(type(nowTime))  # <class 'datetime.datetime'>
print(nowTime)  # 2025-02-22 14:28:40.201978

# 🔴日期对象转换为日期字符串
date1 = nowTime.strftime("%Y-%m-%d %H:%M:%S")
print(date1)  # 2025-02-22 14:30:21
# YYYYMMDD
print(nowTime.strftime("%Y%m%d%H"))  # 2025022214

# 🔴YYYYMMDD格式的字符串转换为日期对象
dt = datetime.strptime("20250221", "%Y%m%d")
print(type(dt))  # <class 'datetime.datetime'>
print(dt)  # 2025-02-21 00:00:00

# 🔴获取当前的时间戳
timestamp1 = nowTime.timestamp()
print(type(timestamp1))  # <class 'float'>
print(f"当前的时间戳为: {timestamp1}")  # 当前的时间戳为: 1740202580.435358
print('\033[91m-----------------------------------------------\033[0m')

"""
    时间的计算
"""
from datetime import timedelta

# 🔴获取明天的日期对象
tomorrowDatetime = nowTime + timedelta(days=1)
print(tomorrowDatetime)  # 2025-02-23 14:41:27.375033

# 🔴获取1个小时之后的日期对象
one_hour_later = nowTime + timedelta(hours=1)
print(one_hour_later)  # 2025-02-22 15:43:09.025499