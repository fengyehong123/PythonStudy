"""
    re.finditer()
        迭代匹配（返回迭代器）
        由于是逐个处理匹配项, 因此比re.findall() 更节省内存
"""
import re

pattern = r"\d+"
text = "abc123def456ghi789"

# 可以看到, 得到的类型是一个迭代器
matches = re.finditer(pattern, text)
print(type(matches))  # <class 'callable_iterator'>

for item in matches:
    print(item.group())
    # 123
    # 456
    # 789