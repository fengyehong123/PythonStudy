"""
    re.sub()
        替换匹配项
    语法
        re.sub(pattern, 替换内容, 目标文本)
"""
import re

pattern = r"\d+"
text = "abc123def456"

# 将所有的数字给替换为 # 符号
result = re.sub(pattern, "#", text)
print(result)  # abc#def#