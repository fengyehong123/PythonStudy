"""
    ⏹配合 matplotlib 库生成图表
    Series对象有一个名为plot的方法可以用来生成图表, 如果选择生成折线图、饼图、柱状图等
    默认会使用Series对象的索引作为横坐标, 使用Series对象的数据作为纵坐标。
"""
import time
import pandas as pd
import matplotlib.pyplot as plt

serie1 = pd.Series({'Q1': 400, 'Q2': 520, 'Q3': 180, 'Q4': 380})

fig1, ax1 = plt.subplots()

# 通过plot方法的kind指定图表类型为柱状图
serie1.plot(kind='bar', ax=ax1)
# 定制纵轴的取值范围
plt.ylim(0, 600)
# 定制横轴刻度（旋转到0度）
plt.xticks(rotation=0)

# 为柱子增加数据标签
for i in range(serie1.size):
    plt.text(i, serie1[i] + 5, serie1[i], ha='center')

# plt.show(block=False) 允许 plt.show() 立即返回，程序不会被阻塞
plt.show(block=False)
# 让图表显示 2 秒
plt.pause(2)
# 关闭指定图表
plt.close(fig1)

"""
    plot方法的kind参数指定了图表类型为饼图
    autopct会自动计算并显示百分比
    pctdistance用来控制百分比到圆心的距离
"""
serie1.plot(kind='pie', autopct='%.1f%%', pctdistance=0.65)
plt.show()