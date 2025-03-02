# pip库管理
pip（`Package Installer for Python`）是 Python 官方推荐的包管理工具，用于安装、更新和卸载 Python 第三方库。

⏹`更新pip命令`
```shell
python -m pip install --upgrade pip
```

⏹`pip命令的基本用法`
```shell
# 列出安装的所有库
pip list

# 安装指定的库的最新版本
pip install pylint

# 安装指定库的指定版本
pip install package_name==1.2.3

# 查看已经安装的库（安装的路径和版本）
pip show pylint

# 根据 requirements.txt 文件批量安装指定的库
pip install -r requirements.txt

# 卸载指定的库
pip uninstall pylint
```

# requirements.txt 文件
[requirements.txt] 是一个 文本文件，用于记录 Python 项目的依赖库 及其 版本号。
它可以帮助团队成员、部署环境或服务器安装相同的 Python 依赖，确保项目的稳定性和可复现性。

⏹`生成 requirements.txt 文件`
```shell
pip freeze > requirements.txt
```
