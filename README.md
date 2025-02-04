**参考资料**
1. https://zhuanlan.zhihu.com/p/509506199 （电脑中安装多个版本的Python）

# 虚拟环境
Python 的 虚拟环境（Virtual Environment） 用于创建一个 独立的 Python 运行环境
可以安装特定版本的库，而不会影响系统的 Python 版本或其他项目。

**虚拟环境的优点**
✅ 避免依赖冲突（不同项目需要不同的库版本）
✅ 隔离项目环境（不污染全局 Python）
✅ 更易于管理和部署（不同环境可以有不同的 Python 版本）

`安装创建虚拟环境的工具`
```shell
# 安装虚拟环境工具
pip install virtualenv

# 查看是否安装成功
virtualenv --version

# cd 到虚拟环境所在的文件夹之后，创建虚拟环境
virtualenv 虚拟环境名称
# 如果有多个Python版本的话，还可以指定虚拟环境的Python版本
virtualenv -p C:\python\python3.6\python.exe 虚拟环境名称

# 退出虚拟环境
deactivate
```


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
