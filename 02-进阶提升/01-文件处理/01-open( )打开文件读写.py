"""
    open() 将会返回一个 file 对象，基本语法如下:
        open(filename, mode, encoding)
"""

filePath = "02-进阶提升/01-文件处理/test.txt"
file_content = """Python 是一个非常好的语言。
是的，的确非常好!!"""

f = None
try:
    # w+ 表示写入文件，当文件不存在的时候，将自动创建
    f = open(filePath, "w+", encoding="utf-8")
    f.write(file_content)
except Exception as e:
    print(e)
finally:
    # 需要手动关闭文件对象，代码较为繁琐
    if 'f' in locals() and f:  
        # 只有 f 存在时才关闭
        f.close()

"""
    使用 with open() 来处理文件，可以自动完成文件流对象的关闭
    不需要写 f.close() 这样的代码
"""
with open(filePath, "r", encoding="utf-8") as f:
    print(f.read())

# 读取文件中的所有行
with open(filePath, "r", encoding="utf-8") as f:
    print(f.readlines())  # ['Python 是一个非常好的语言。\n', '是的，的确非常好!!']

# 通过迭代的方式进行行读取
with open(filePath, "r", encoding="utf-8") as f:
    for line in f:
        print(line, end = '')
        # Python 是一个非常好的语言。
        # 是的，的确非常好!!

"""
    删除刚创建好的文件
"""
import os
import time

# 先检查文件是否存在，避免报错
if os.path.exists(filePath):  
    # 睡眠2秒之后再删除文件
    time.sleep(2)
    os.remove(filePath)