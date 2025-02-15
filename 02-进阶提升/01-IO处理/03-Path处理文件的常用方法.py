"""
    pathlib 是 Python 3.4+ 提供的一个现代化模块
    它使文件和路径操作更加直观、面向对象，取代了传统的 os.path 方式。

    pathlib 模块不仅有 Path, 还提供了其他有用的类
        比如
            PurePath
            PosixPath
            WindowsPath
            以及一些与路径相关的操作函数
    其中最常用的就是 Path  
"""
from pathlib import Path

# 获取运行当前Python文件的路径
print(Path.cwd())  # E:\My_Project\PythonStudy
print(Path(".").resolve())  # E:\My_Project\PythonStudy
# 获取当前用户的Home路径
print(Path.home())  # C:\Users\Admin
# 获取当前Python文件的目录
print(Path(__file__).parent)  # e:\My_Project\PythonStudy\02-进阶提升\01-IO处理

# 读取指定的文件
p2 = Path("E:\My_Project\PythonStudy\README.md")

# 检查文件是否存在
print(p2.exists())  # True
# 检查是否为文件
print(p2.is_file())  # True
# 检查是否为文件夹
print(p2.is_dir())  # False

# 获取文件名(包含后缀)
print(p2.name)  # README.md
# 获取不包含后缀的文件名
print(p2.stem)  # README
# 获取文件的后缀
print(p2.suffix)  # .md
# 获取文件名之外的部分
print(p2.parent)  # E:\My_Project\PythonStudy

# 将绝对路径进行拆解
path_parts = p2.parts
# 拆解之后是一个元组
print(type(path_parts))  # <class 'tuple'>
print(path_parts)  # ('E:\\', 'My_Project', 'PythonStudy', 'README.md')

# 🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴🔴

# 创建一个Path对象,由于没有指定目录，默认文件会创建在工作目录下
p1 = Path("example.txt")
# 如果对应的文件不存在的话
if not p1.exists():
    # 创建文件
    p1.touch()
    # 获取创建成功的文件的绝对路径
    print(f"文件创建成功,文件的绝对路径是 → {p1.resolve()}")  # 文件创建成功,文件的绝对路径是 → E:\My_Project\PythonStudy\example.txt
    # 删除文件
    p1.unlink()
    print("文件删除成功...")

print('\033[91m-----------------------------------------------\033[0m')

# 拼接路径创建Path对象
p3 = Path(__file__).parent / "content.txt"

# 将内容写入文件(这种方式不会导致文件句柄泄漏), 相比于open()方式更加简洁, 适用于小文件
p3.write_text("Hello, World!", encoding="utf-8")
# 读取文件中的内容
print(p3.read_text(encoding="utf-8"))  # Hello, World!

"""
    读取文件
"""
with p3.open("r", encoding="utf-8") as f:
    # 读取指定文件的一行
    print(f.readline())  # Hello, World!

# 删除文件
p3.unlink()