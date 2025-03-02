"""
    re.split()
        以匹配项为分隔符
"""
import re

"""
    {n,}
        至少匹配 n 次
"""
# 至少匹配1次 :
pattern = r":{1,}"
text = "abc:def::ghi:::poi"

# 相当于以至少一个 : 作为分隔符进行元素拆分
result = re.split(pattern, text)
print(result)  # ['abc', 'def', 'ghi', 'poi']