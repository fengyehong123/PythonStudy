"""
    re.search()
        全文搜索第一个匹配项
"""
import re

pattern = r"\d+"
text = "abc456def789"

"""
    只匹配 第一个符合的部分, 和match不同
    即使不在开头, 也会被匹配到
"""
result = re.search(pattern, text)
if result:
    print(result.group())  # 456