"""
    Python 3.7+之后版本的dataclasses 模块 提供了 @dataclass 装饰器
    可以自动生成 __init__、__repr__、__eq__ 等方法，让类更简洁。

    @dataclass 只是自动生成 __init__ 等方法，但它不会改变 Python 类的本质。
    实例方法 仍然需要 self 来访问和修改实例属性。
"""
from dataclasses import dataclass, field

@dataclass
class User:

    name: str
    age: int
    address: str = field(default="地球")
    """
        default_factory
            用于设置可变类型的默认值(如 list, dict, set)
            防止多个实例共享同一个可变对象。
    """
    tags: list = field(default_factory=list)
    """
        如果要设置可变类型的默认值的话, 需要使用函数
        从而保证每一个实例对象的可变值属性都是唯一的
    """
    hobby: list = field(default_factory=lambda: ["开车", "游泳", "编程"])

    # 类的方法仍然需要 self 来获取类的属性
    def printInfo(self):
        print(f"用户的名字是: {self.name}, 年龄是: {self.age}")


user1 = User("贾飞天", 18)
print(user1)  # User(name='贾飞天', age=18, address='地球', tags=[], hobby=['开车', '游泳', '编程'])

# 调用类实例的方法
user1.printInfo()  # 用户的名字是: 贾飞天, 年龄是: 18

user2 = User("枫叶红", 28, ['吃饭', '睡觉', '打豆豆'])
print(user2)  # User(name='枫叶红', age=28, address=['吃饭', '睡觉', '打豆豆'], tags=[], hobby=['开车', '游泳', '编程'])


