"""
    permutations
        排列（顺序有关）
"""
from itertools import permutations

# 列表元素
items = ["A", "B", "C"]

# 取 2 个元素的所有排列
for perm in permutations(items, 2):
    print(perm, end=" ")  # ('A', 'B') ('A', 'C') ('B', 'A') ('B', 'C') ('C', 'A') ('C', 'B')
print("\n")

# 取 3 个元素的所有排列
for perm in permutations(items, 3):
    print(perm, end=" ")  # ('A', 'B', 'C') ('A', 'C', 'B') ('B', 'A', 'C') ('B', 'C', 'A') ('C', 'A', 'B') ('C', 'B', 'A')