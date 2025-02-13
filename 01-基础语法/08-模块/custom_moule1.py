def printInfo1():
    print("printInfo1执行了...")

def printInfo2():
    print("printInfo2执行了...")

"""
    我们在此处并没有使用 if __name__ == "__main__":
    因此当 custom_moule1.py 模块被引入时，下面的这行 print语句将会执行
"""
print("custom_moule1.py执行了")