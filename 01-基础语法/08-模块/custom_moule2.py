def printInfo3():
    print("printInfo3执行了...")

def printInfo4():
    print("printInfo4执行了...")

"""
    我们在使用了 if __name__ == "__main__":
    因此当 custom_moule2.py 模块被引入时，下面的这行 print语句并不会执行
    只有当我们运行 custom_moule2.py 文件时, 下面的这行print语句才会执行
"""
if __name__ == "__main__":
    print("custom_moule2.py执行了")

