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
from importlib import util as packageUtil

# 要自动安装的模块名称
package_name_list = [
    "aiohttp",
    "asyncio",
    "requests"
]

# 过滤出未安装的模块
missing_packages = [package_name for package_name in package_name_list if packageUtil.find_spec(package_name) is None]

if missing_packages:
    print(f"🔍 检测到未安装的模块: {', '.join(missing_packages)}，正在安装...")
    
    """
        sys.executable 是 Python 的 sys 模块中的一个属性，它返回当前 Python 解释器的完整路径。

        这样写的好处是
            无论 Python 以何种方式启动 (如虚拟环境、不同版本等),
            sys.executable 都能准确获取当前运行的 Python 解释器路径。

        sys.executable 适用于 Windows、Linux 和 macOS,
        而直接调用 python 可能会因为系统默认 Python 版本不同而出错。
    """
    subprocess.run([sys.executable, "-m", "pip", "install", *missing_packages], check=True)
    
    print(f"✅ 所有模块安装完成！")
else:
    print("✅ 所有模块已安装。")

# 现在可以安全导入 aiohttp
import aiohttp

# 打印 pandas 版本，确认安装成功
print(f"当前的 aiohttp 版本为: {aiohttp.__version__}")