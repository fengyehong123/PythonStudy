from itertools import count

# 从 10 开始，每次递增 2
for i in count(10, 2):
    if i > 25:
        break
    print(i, end=" ")  # 10 12 14 16 18 20 22 24