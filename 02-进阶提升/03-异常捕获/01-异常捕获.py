try:
    1 / 0
# 支持抛出多个异常
except OSError as err:
    print(err)
    # ⭕抛出异常
    raise err
except Exception as e:
    print(e)
# finally中的代码块无论什么时候都会执行
finally:
    print("finally中的代码块已经执行了...")
print('\033[91m-----------------------------------------------\033[0m')

# 自定义一个函数，如果输入的条件不符合要求，就抛出异常
def printInfo(info):
    if info != "hello world":
        print(info)
        return
    # ⭕抛出异常
    raise Exception(f"输入的值不能是：{info}")

try:
    printInfo("你好")  # 你好
    printInfo("hello world")
except Exception as e:
    print(e)  # 输入的值不能是：hello world
print('\033[91m-----------------------------------------------\033[0m')