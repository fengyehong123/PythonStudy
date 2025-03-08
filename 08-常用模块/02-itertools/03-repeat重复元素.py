from itertools import repeat

# 重复 → 三次
for num in repeat("→", 3):
    print(num, end=" ")  # → → →
print("\n")

# 列表推导式
list1 = [num for num in repeat("→", 3)]
print(list1)  # ['→', '→', '→']