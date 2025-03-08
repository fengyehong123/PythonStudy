from itertools import cycle

# 设置计数器
counter = 0

for item in cycle(["A", "B", "C"]):

    # 一共循环了10次, 输出了10个字符
    print(item, end=" ")  # A B C A B C A B C A
    counter += 1

    # 设置退出条件
    if counter == 10:
        break