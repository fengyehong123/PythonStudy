"""
    ⭕内置的函数 dir() 可以找到模块内定义的所有名称。
    以一个字符串列表的形式返回
"""

import random

result1 = dir(random)

print(type(result1))  # <class 'list'>
print(result1)
"""
    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__'
    , '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma'
    , '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices'
    , 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed'
    , 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
"""

# 在当前python文件中定义函数和变量
def printInfo1():
    print("Hello Wrold")
def printInfo2():
    print("Hello Wrold")
CONST_VAR = 110

# ⭕如果没有给定参数，那么 dir() 函数会罗列出当前定义的所有名称:
print(dir())
"""
    ['CONST_VAR', '__annotations__', '__builtins__', '__cached__', '__doc__', '__file__'
    , '__loader__', '__name__', '__package__', '__spec__', 'printInfo1', 'printInfo2', 'random', 'result1']
"""