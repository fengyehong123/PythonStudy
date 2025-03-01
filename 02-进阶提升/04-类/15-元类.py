"""
    在 Python 中, 元类 (Metaclass) 是用于控制 类的创建 过程的特殊类。
    通常, 我们创建对象时, 使用 class 关键字来定义一个类, 而元类则用于 定义类本身的行为
        1. 类是对象的模板, 元类是类的模板。
        2. 元类决定类如何创建, 修改和初始化。
    
    在 Python 中，所有的类默认都是 type 的实例。
    type 是 最基本的元类，可以直接用于创建类。
"""
# 使用 type 来创建类
Person = type(
    "Person",
    (object,),
    {
        "address": "第一宇宙银河系地球中国",
        "__init__": lambda self, age: setattr(self, "personAge", age),
        "printInfo": lambda self, name: print(f"我的名字叫: {name}, 我今年: {self.personAge}岁了, 我的地址是: {self.address}")
    }
)
# 创建实例对象的时候传参
person = Person(18)
# 使用实例方法的时候传参
person.printInfo("贾飞天")

"""
    可以自定义元类来 控制类的创建
    最常见的做法是继承 type 并重写 __new__ 或 __init__ 方法
"""
class CustomMeta(type):

    def __new__(cls, name, bases, class_dict):

        print(f"名字叫{name}的类正在被创建...")
        # 添加额外属性
        class_dict["extra_attr"] = "我是额外属性的值"
        return super().__new__(cls, name, bases, class_dict)
    
    def __init__(cls, name, bases, class_dict):
        print(f"名字叫{name}的类正在被初始化...")
        super().__init__(name, bases, class_dict)

# 自定义一个类, 指定元类
class Student(metaclass=CustomMeta):
    pass

""" 
    Student类使用了 CustomMeta 作为元类, 因此 CustomMeta 这个元类在创建 Studnet 的时候被调用
    __new__ 方法在 Student类 创建之前执行, 因此 Student类 的定义被修改(增加了新的属性)
    __new__ 主要用于 控制类的创建, 可以修改类的属性或方法
    __init__ 主要用于 初始化类, 但不会改变类的定义
"""
print(Student.extra_attr)
# 名字叫Student的类正在被创建...
# 名字叫Student的类正在被初始化...
# 我是额外属性的值
print('\033[91m-----------------------------------------------\033[0m')

class RestrictedMeta(type):

    def __new__(cls, name, bases, class_dict):
        allowed_attrs = {"name", "age"}
        for attr in class_dict:
            if not attr.startswith("__") and attr not in allowed_attrs:
                raise AttributeError(f"非法属性: {attr}")
        return super().__new__(cls, name, bases, class_dict)
    
    def __setattr__(cls, key, value):
        allowed_attrs = {"name", "age"}
        if key not in allowed_attrs:
            raise AttributeError(f"不允许添加新属性: {key}")
        super().__setattr__(key, value)

class Teacher(metaclass=RestrictedMeta):

    name = "李四"
    """
        __new__ 方法在 创建类时 运行，它只检查类定义时的属性，不会管之后动态添加的属性。
        因为我们在 RestrictedMeta元类的  __new__ 方法中做了限制
        所以无法使用 address 类属性
    """
    # address = "宇宙银河系"

    # 便于类的实例对象打印
    def __str__(self):
        return f"姓名:{self.name} → 年龄:{self.age}"

"""
    因为我们在 RestrictedMeta元类的 __setattr__ 方法中允许动态添加 age 属性
    所以 age 这个类属性添加成功
"""
Teacher.age = 30
print(Teacher.__dict__["name"])  # 李四
print(Teacher.__dict__["age"])  # 30
t1 = Teacher()
print(t1)  # 姓名:李四 → 年龄:30

# 尝试添加元类中并没有指定的属性
try:
    Teacher.address = "宇宙银河系"
except Exception as e:
    print(e)  # 不允许添加新属性: address
