"""
    一个模块被另一个程序第一次引入时, 其主程序将运行。
    如果我们想在模块被引入时, 模块中的某一程序块不执行,
    我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
"""
from custom_moule1 import printInfo1

"""
    由于 custom_moule1.py 文件中并没有使用 if __name__ == "__main__":
    因此当我们导入 custom_moule1 的时候，该模块中的主程序将会执行，
    因此即使我们导入printInfo1这个方法并没有执行
    custom_moule1.py执行了 也会打印在控制台上

"""
# custom_moule1.py执行了

from custom_moule2 import printInfo3, printInfo4 
printInfo3()  # printInfo3执行了...
printInfo4()  # printInfo4执行了...