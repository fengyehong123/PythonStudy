import time
"""
    pathlib 是 Python 3.4+ 提供的一个现代化模块
    它使文件和路径操作更加直观、面向对象，取代了传统的 os.path 方式。
"""
from pathlib import Path

"""
    Path(__file__).parent 代表当前 Python 文件所在的目录
    这种写法适用于Python3, 更加推荐
    可兼容winwows和linux的路径
"""
file_path = Path(__file__).parent / "test1.txt"
print(type(file_path))  # <class 'pathlib.WindowsPath'>

# 判断文件是否存在
if not file_path.exists():
    file_content = """我是默认内容的第一行,
    我是默认内容的第二行"""
    file_path.write_text(file_content, encoding="utf-8")

# 读取文件的内容
with file_path.open("r", encoding="utf-8") as f:
    print(f.read())

# 如果文件存在的话
if file_path.exists():
    # 2秒之后就删除文件
    time.sleep(2)
    file_path.unlink()

# 直接通过w+的方式创建文件，当文件不存在的话，会自动进行创建
# 如果文件本身就存在的话，会被覆盖
with file_path.open("w+", encoding="utf-8") as f:
    f.write("hello world!")

# 2秒之后就删除文件
time.sleep(2)
file_path.unlink()