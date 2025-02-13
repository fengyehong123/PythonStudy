# 可以在 my_package2 包被导入的时候，进行一些初始化操作
print("my_package2 这个包被导入了...")

# 限制 from my_package2 import * 时，导入的模块
__all__ = [
    "Info1"
    , "Info3"
]