"""
    importlib.util 模块的作用
    ✅ 检测模块是否已安装 如 find_spec()
    ✅ 动态加载模块, 如 import_module()
    ✅ 从文件路径加载 .py 文件 如 spec_from_file_location()
    ✅ 避免直接修改 sys.path, 比 sys.path.append() 更安全
    importlib.util 从 Python 3.4 开始 就有了。
"""
import sys
import subprocess
import importlib.util

# 要自动安装的模块名称
package_name = "pandas"

# 检查 pandas 是否已安装
if importlib.util.find_spec(package_name) is None:
    print(f"🔍 检测到 {package_name} 未安装，正在安装...")
    # 自动安装 pandas 模块
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
    print(f"✅ {package_name} 安装完成！")
else:
    print(f"✅ {package_name} 已安装。")

# 现在可以安全导入 pandas
import pandas as pd

# 打印 pandas 版本，确认安装成功
print(f"当前的pandas版本为: {pd.__version__}")