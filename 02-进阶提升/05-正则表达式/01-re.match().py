"""
    re.match()
        从字符串开头匹配
"""
import re

pattern = r"\d+"
text = "123abc456"

# 因为字符串的开头正好就是数字, 所以被匹配到
result = re.match(pattern, text)
if result:
    print(result.group())  # 123

# 字符串中虽然有数字, 但是因为并不在开头, 所以返回None
print(re.match(pattern, "ABC123abc456"))  # None