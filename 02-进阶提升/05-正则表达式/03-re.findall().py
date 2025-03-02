"""
    re.findall()
        获取所有匹配项（返回列表）
        如果没有匹配项的话, 则返回一个空列表
"""
import re

# 匹配数字的正则表达式
pattern = r"\d+"
text = "abc123def456ghi789"

matches = re.findall(pattern, text)
if len(matches) > 0:
    print(matches)  # ['123', '456', '789']