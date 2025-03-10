"""
    combinations
        组合（顺序无关）
"""

from itertools import combinations

# 列表元素
items = ["A", "B", "C"]

# 取 2 个元素的所有组合
for comb in combinations(items, 2):
    print(comb, end=" ")  # ('A', 'B') ('A', 'C') ('B', 'C')
print("\n")

# 取 3 个元素的所有组合
for comb in combinations(items, 3):
    print(comb, end=" ")  # ('A', 'B', 'C')