"""
    shutil 是 Python 内置的 高级文件操作模块
        用于复制、移动、删除文件和文件夹。
        它比 os 模块功能更强大，支持递归删除、复制整个目录等操作。

    shutil 模块从 Python 1.3 就已经存在了！它是 Python 早期标准库 的一部分，最初用于处理文件和目录的高级操作。
    不过，后续版本不断改进，添加了新功能。例如: 
        Python 2.3: 
            添加 shutil.copytree()（递归复制文件夹）。
        Python 3.3: 
            添加 shutil.which()（查找可执行文件）。
        Python 3.8: 
            shutil.copytree() 添加 dirs_exist_ok=True 参数，允许目标目录已存在。
        Python 3.10: 
            shutil.copytree() 添加 copy_function=shutil.copy2, 增强复制策略。
"""
import time
import shutil
from pathlib import Path

# 复制文件(文件的创建时间,修改时间等原数据不会保留)
shutil.copy("README.md", "README_bk.md")
# 复制文件(文件的创建时间,修改时间等原数据会被保留下来)
shutil.copy2("README.md", "README_bk_1.md")

# .copy()方法的参数除了字符串之外还支持 Path 对象
srcPath = Path.home() / "Desktop" / "常用英文词汇.txt"
shutil.copy(srcPath, "haha.txt")

# 复制文件夹(如果目标文件夹已经存在的话，会报错)
shutil.copytree("01-基础语法", "测试文件夹")
time.sleep(1)

# 文件夹移动到桌面上
deskTopFolder = Path.home() / "Desktop"
shutil.move(Path("测试文件夹"), deskTopFolder)

# 遍历桌面上的测试文件夹中
for txt_file in (deskTopFolder / "测试文件夹").rglob("*"):
    print(txt_file)
print('\033[91m-----------------------------------------------\033[0m')

"""
    shutil 没有删除文件的功能，但是有删除文件夹的功能
"""
time.sleep(2)
shutil.rmtree(deskTopFolder / "测试文件夹")

# 删除文件
pathList = [
    Path("README_bk.md")
    , Path("README_bk_1.md")
    , Path("haha.txt")
]
for pathObj in pathList:
    # 文件删除
    pathObj.unlink()

"""
    shutil.copyfileobj() 
        直接拷贝二进制数据，比 read() + write() 方式更快，减少 I/O 负担。
"""
def merge_csv_files(output_file, temp_files):

    with open(output_file, mode='wb') as out_f:
        # 将临时文件排序后循环打开，然后依次写入
        for temp_file in sorted(temp_files):
            with open(temp_file, mode='rb') as temp_f:
                shutil.copyfileobj(temp_f, out_f)

