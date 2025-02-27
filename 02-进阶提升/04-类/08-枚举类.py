from enum import Enum
"""
    Python 3.11 支持 StrEnum, 枚举成员可直接作为字符串使用。
"""
from enum import StrEnum

# 定义枚举类
class ColorEnum(Enum):

    RED = 1
    GREEN = 2
    BLUE = 3
    # Enum可以是任意类型
    COLORS = ['red', 'green', 'blue']

# 使用枚举成员
print(ColorEnum.RED)  # Color.RED
print(ColorEnum(2))   # Color.GREEN

print(ColorEnum.GREEN.name)  # GREEN
print(ColorEnum.BLUE.value)  # 3

# 枚举成员迭代
for color in ColorEnum:
    print(color)

# 比较枚举成员
print(ColorEnum.RED == ColorEnum.RED)  # True
print(ColorEnum.RED is ColorEnum.GREEN)  # False
print('\033[91m-----------------------------------------------\033[0m')

# 也可以这样定义一个枚举类
GenderEnum = Enum("Gender", ("Man", "Women"))
print(GenderEnum.Man.name)  # Man

# 对枚举类进行迭代
for gender, item in GenderEnum.__members__.items():
    print(f"性别: {gender} → 值: {item.value}")
    # 性别: Man → 值: 1
    # 性别: Women → 值: 2
print('\033[91m-----------------------------------------------\033[0m')

class ColorStrEnum(StrEnum):
    """
        StrEnum中的所有枚举值必须是字符串
        并且会自动继承字符串的行为。
    """
    RED = "red~~"
    GREEN = "green!!"
    BLUE = "blue**"

print(ColorStrEnum.RED)  # red~~
print(isinstance(ColorStrEnum.RED, str))  # True

# StrEnum 实例本身就是字符串，可以直接与字符串比较
print(ColorStrEnum.RED == 'red~~')  # True
print(ColorStrEnum.GREEN.upper()) # GREEN!!
