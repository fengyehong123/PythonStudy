import re

"""
    re.VERBOSE
        允许在模式中使用换行和注释，提高可读性。
"""
pattern = re.compile(r"""
    (\d{4})    # 年
    -          # 分隔符
    (?:\d{2})  # 月
    -          # 分隔符
    (\d{2})    # 日
""", re.VERBOSE)

text = "2024-02-24"
result = re.search(pattern, text)
print(result.groups())  # ('2024', '24')