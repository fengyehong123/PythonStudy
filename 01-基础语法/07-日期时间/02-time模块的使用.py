"""
    time 模块用于处理时间相关的低级操作
    如获取当前时间戳、暂停程序执行等。
"""
import time

# 获取当前的时间戳
timestamp = time.time()
print(timestamp)  # 1740308511.717338

# 获取localtime对象
localtime1 = time.localtime()
print(localtime1)  # time.struct_time(tm_year=2025, tm_mon=2, tm_mday=23, tm_hour=20, tm_min=10, tm_sec=18, tm_wday=6, tm_yday=54, tm_isdst=0)
# 年
print(localtime1.tm_year)  # 2025
# 月
print(localtime1.tm_mon)  # 2
# 日
print(localtime1.tm_mday)  # 23
# 时
print(localtime1.tm_hour)  # 20
# 分
print(localtime1.tm_min)  # 10
# 秒
print(localtime1.tm_sec)  # 18
# 星期(周一: 0, 周日: 6)
print(localtime1.tm_wday)  # 6
# 一年中的第几天
print(localtime1.tm_yday)  # 54

# 通过解包赋值来获取前3个字段（年, 月, 日）的值, 其他字段的值忽略
tm_year, tm_mon, tm_mday, *_ = time.localtime()
print(tm_year, tm_mon, tm_mday)  # 2025 2 23
print('\033[91m-----------------------------------------------\033[0m')

# 将localtime对象格式化为字符串日期
strTime1 = time.strftime("%Y/%m/%d %H:%M:%S", localtime1)
print(strTime1)  # 2025/02/23 20:15:34

# 将字符串转换为localtime对象
localtime2 = time.strptime("2025/02/23 20:15:34", "%Y/%m/%d %H:%M:%S")
print(localtime2)  # time.struct_time(tm_year=2025, tm_mon=2, tm_mday=23, tm_hour=20, tm_min=15, tm_sec=34, tm_wday=6, tm_yday=54, tm_isdst=-1)
print('\033[91m-----------------------------------------------\033[0m')

# 计算程序的执行时间
startTime = time.perf_counter()
time.sleep(2)
endTime = time.perf_counter()
print(f"耗时: {endTime - startTime:.6f} 秒")  # 耗时: 2.000732 秒