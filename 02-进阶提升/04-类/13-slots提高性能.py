"""
    Python 3.10+ 支持 __slots__ 结合 dataclass
    可以减少内存占用并提高访问速度。
    📌 优点：
        1. 自动生成 __slots__, 避免 __dict__ 存储实例属性, 减少内存占用
        2. 加快属性访问速度, 因为 Python 不再需要在 __dict__ 里查找属性
        3. 禁止动态添加新属性, 提高代码的安全性
"""
from dataclasses import dataclass

@dataclass
class Point1:

    x: int
    y: int

p1 = Point1(10, 30)

# 普通的实例对象有 __dict__ 属性
print(p1.__dict__)  # {'x': 10, 'y': 30}

# 普通的类可以自由添加属性
p1.z = 100
print(p1.z)  # 100

@dataclass(slots=True)
class Point2:

    x: int
    y: int

p2 = Point2(15, 16)

try:
    # 使用了 @dataclass(slots=True) 之后, __dict__ 属性就不存在了
    print(p2.__dict__)
except Exception as e:
    print(e)  # 'Point2' object has no attribute '__dict__'

try:
    # 使用了 @dataclass(slots=True) 之后, 无法随意添加属性了
    p2.z = 50
except Exception as e:
    print(e)  # 'Point2' object has no attribute 'z'

