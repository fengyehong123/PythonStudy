"""
    subprocess 模块是 Python 用于执行系统命令的标准库，提供了创建和管理子进程的接口。
    它比 os.system() 更强大，可以获取标准输出、标准错误并进行更复杂的交互。

    ⏹subprocess.run()
        适用于简单的命令执行，默认会等待进程完成。
"""
import shlex
import subprocess

"""
    ⏹因为我们的Python安装在Windows环境下, 且安装了Git
    所以可以通过 bash -c 在Windows环境中执行linux命令

    text=True
        返回字符串【Python 3.7+】
    check=True
        如果命令返回非0退出码, 则抛出异常 subprocess.CalledProcessError
"""
result1 = subprocess.run(["bash", "-c", "ls -l | grep md"], capture_output=True, text=True, encoding="utf-8")
print(result1.stdout)
# 返回命令执行后的状态码
print(result1.returncode)

# 命令拆分为列表的方式太麻烦，可以通过 shlex 模块来将一整行命令拆分为列表
linuxCmd = "bash -c ls -l | grep md | wc -l"
linuxCmdArgs = shlex.split(linuxCmd)

result2 = subprocess.run(linuxCmdArgs, capture_output=True, text=True, encoding="utf-8")
print(result2.stdout)

# 也支持PowerShell命令
psCmd = "powershell -Command Get-ChildItem | Measure-Object | Select-Object -Property Count"
psCmdArgs = shlex.split(psCmd)
print(psCmdArgs)  # ['powershell', '-Command', 'Get-ChildItem', '|', 'Measure-Object', '|', 'Select-Object', '-Property', 'Count']
result3 = subprocess.run(psCmdArgs, capture_output=True, text=True)
print(result3.stdout)

"""
    shell=True 让命令通过 shell 解析
    如果执行外部输入的话, 可能存在 安全风险, 一定要避免
"""
result4 = subprocess.run("powershell -Command Get-ChildItem", capture_output=True, text=True, shell=True)
print(result4.stdout)