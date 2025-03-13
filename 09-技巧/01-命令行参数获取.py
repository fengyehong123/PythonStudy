"""
    使用 sys.argv 方式来获取命令行参数
    sys.argv 是一个列表，包含命令行参数：
        1. sys.argv[0] 是脚本本身的文件名。
        2. sys.argv[1:] 是传递给脚本的参数。
"""
# 导入sys模块
import sys

# 可以看到 sys.argv 是一个list
print(type(sys.argv))  # <class 'list'>

# 获取脚本文件的名称
print(sys.argv[0])  # e:\My_Project\PythonStudy\09-技巧\01-命令行参数获取.py

"""
    获取命令行参数
    假设通过如下方式进行调用
        python 01-命令行参数获取.py 10 20 30
"""
print(sys.argv[1:])  # ['10', '20', '30']

# 导入参数解析模块
import argparse

"""
    推荐使用 argparse
    支持选项解析、类型转换、默认值等。
    假设通过如下方式进行调用
        python 01-命令行参数获取.py 贾飞天 -a 25 --verbose
"""
parser = argparse.ArgumentParser()
# 添加要解析的参数
parser.add_argument("name", help="你的名字")
parser.add_argument("-a", "--age", type=int, help="你的年龄", default=18)
parser.add_argument("-v", "--verbose", action="store_true", help="是否启用详细模式")

# 获取解析到的参数对象
args = parser.parse_args()
print('\033[91m-----------------------------------------------\033[0m')
print(args)  # Namespace(name='贾飞天', age=25, verbose=True)
print(args.name)  # 贾飞天
print(args.age)  # 25
print(args.verbose)  # True
print('\033[91m-----------------------------------------------\033[0m')