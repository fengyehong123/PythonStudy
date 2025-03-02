"""
    若不需要捕获某些匹配项
    只想使用 () 进行分组匹配，此时可以用 (?:...)
"""
import re

text = "2024-02-24"
# 我想让中间的数字有两位数, 并且我只想匹配前后两块区域的数字
match = re.search(r"(\d{4})-(?:\d{2})-(\d{2})", text)
result = match.groups()

print(type(result))  # <class 'tuple'>
print(result)  # ('2024', '24')