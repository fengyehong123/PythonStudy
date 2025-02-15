import time
from pathlib import Path

# 获取当前用户桌面上的文件夹对象
p1 = Path.home() / "Desktop"

# 遍历所有的文件和文件夹(非递归的方式)
for item in p1.iterdir():
    print(item)
print('\033[91m-----------------------------------------------\033[0m')

# 遍历所有桌面上的所有 .txt 文件
for txt_file in p1.glob("*.txt"):
    print(txt_file)
print('\033[91m-----------------------------------------------\033[0m')

# 递归遍历所有桌面上的所有 .txt 文件
for txt_file in p1.rglob("*.txt"):
    print(txt_file)
print('\033[91m-----------------------------------------------\033[0m')

# 递归创建文件夹
d1 = Path("new_folder/d1/f1")
d1.mkdir(parents=True, exist_ok=True)

if d1.exists():
    time.sleep(2)
    """
        删除文件夹(只能删除空文件夹)
        如果文件夹内还有空文件夹的话，说明该文件夹不是空文件夹
        则无法删除
    """
    d1.rmdir()

# 导入 shutil 模块
import shutil

time.sleep(2)
# 删除文件夹(即使是非空文件夹)
shutil.rmtree(Path("new_folder"))