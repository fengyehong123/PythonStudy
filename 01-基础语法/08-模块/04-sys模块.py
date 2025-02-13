"""
    Python 会在 sys.path 指定的路径中查找模块
"""

import sys
print(sys.path)
"""
    ['e:\\My_Project\\PythonStudy\\01-基础语法\\08-模块', 'C:\\python\\python3.12\\python312.zip', 'C:\\python\\python3.12\\DLLs'
    , 'C:\\python\\python3.12\\Lib', 'C:\\python\\python3.12', 'C:\\python-virtualenv\\PythonStudy'
    , 'C:\\python-virtualenv\\PythonStudy\\Lib\\site-packages']
"""

try:
    # 由于我们的模块不在Python指定的路径中，所以Python找不到模块，因此报错
    from Test_Module import printToken1
except Exception as e:
    print('\033[91m-----------------------------------------------\033[0m')
    print(e)  # No module named 'Test_Module'
    print('\033[91m-----------------------------------------------\033[0m')

# 通过指定包名和模块名的方式来导入执行的方法
from my_package1.Test_Module import printToken1
printToken1()  # printToken1执行了...

# 我们可以将指定路径添加到模块查找的路径中
## 这种做法会影响可移植性，不推荐这么做 ##
sys.path.append("E:\\My_Project\\PythonStudy\\01-基础语法\\08-模块\\my_package1")

# 这样就可以在导入时直接写模块名称，不用写模块路径了
from Test_Module import printToken2
printToken2()  # printToken2执行了...
