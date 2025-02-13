"""
    __init__.py 文件的主要作用是 标识该目录为 Python 包(package)
    在 Python 3.3 之后, __init__.py 不是必须的

    基本作用
    1. 可以在 import 时执行初始化代码
    2. 通过 __all__ 限制导入 import * 时的 数量
"""

from my_package2 import *
print(Info1)  # <module 'my_package2.Info1' from 'e:\\My_Project\\PythonStudy\\01-基础语法\\08-模块\\my_package2\\Info1.py'>
Info1.buyApple()  # 我买了一个苹果
print(Info3)  # <module 'my_package2.Info3' from 'e:\\My_Project\\PythonStudy\\01-基础语法\\08-模块\\my_package2\\Info3.py'>
Info3.buyComputer()  # 我买了一台电脑

try:
    # 因为我们在 my_package2 包的 __init__.py 文件的 __all__ 中没有添加 Info2
    # 因此 from my_package2 import * 进行导入时，并不会把 Info2 给加进去
    print(Info2)
except Exception as e:
    print(e)  # name 'Info2' is not defined

# __init__.py 文件的 __all__ 没有办法阻止我们通过这种方式进行导入
from my_package2 import Info2
print(Info2)  # <module 'my_package2.Info2' from 'e:\\My_Project\\PythonStudy\\01-基础语法\\08-模块\\my_package2\\Info2.py'>
