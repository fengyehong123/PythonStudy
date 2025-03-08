"""
    collections.defaultdict 是 Python 标准库中的一个特殊字典，提供默认值，避免 KeyError。
    它比普通 dict 更方便，特别适用于 分组、计数、列表/集合累加 等场景。
"""
from collections import defaultdict

# ⏹指定默认值类型为 int，默认值是 0
num_dict = defaultdict(int)

# key 'a' 不存在时，默认值是 0
print(num_dict["a"])  # 0

num_dict["a"] += 1
num_dict["b"] += 2
print(num_dict)  # defaultdict(<class 'int'>, {'a': 1, 'b': 2})

# ⏹指定默认值类型为 list，默认值是 []
defaultdict1 = defaultdict(list)
print(defaultdict1["fruits"])  # []

defaultdict1["fruits"].append("apple")
defaultdict1["fruits"].append("banana")
defaultdict1["veggies"].append("carrot")
print(defaultdict1)  # defaultdict(<class 'list'>, {'fruits': ['apple', 'banana'], 'veggies': ['carrot']})

# ⏹指定默认值类型为 set，用来去重
unique_words = defaultdict(set)

# a的键有两个相同的值, 最终完成了去重
unique_words["a"].add("apple")
unique_words["a"].add("apple")
unique_words["a"].add("avocado")
unique_words["b"].add("banana")
print(unique_words)  # defaultdict(<class 'set'>, {'a': {'avocado', 'apple'}, 'b': {'banana'}})

# ⏹指定默认值类型为 lambda 表达式, 用来设置一个指定的默认值
default_score = defaultdict(lambda: "Hello World!")
print(default_score["Key"])  # Hello World!