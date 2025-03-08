from collections import Counter

# 有若干单词
words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
    'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
    'look', 'into', 'my', 'eyes', "you're", 'under'
]

"""
    统计单词出现的次数
"""
counter = Counter(words)

# 各个单词出现的次数
print(type(counter))  # <class 'collections.Counter'>
print(counter)  # Counter({'eyes': 8, 'the': 5, 'look': 4, 'into': 3, 'my': 3, 'around': 2, 'not': 1, "don't": 1, "you're": 1, 'under': 1})

# 指定单词出现的次数
print(counter['eyes'])  # 8
print(counter['the'])  # 5

# 出现次数前3的单词和次数
print(counter.most_common(3))  # [('eyes', 8), ('the', 5), ('look', 4)]