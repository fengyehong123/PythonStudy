# 定义一个类
class MathUtils:

    # 类中的静态方法
    @staticmethod
    def add(num1, num2):
        return num1 + num2

# 无需创建类的实例对象, 类可以直接调用类中的静态方法
print(MathUtils.add(30, 70))  # 100

"""
    类方法的使用
    1. 使用 @classmethod 装饰的方法。
    2. 第一个参数必须是 cls(类本身), 而不是 self
    3. 主要用于修改类属性 或 创建类的不同实例。
"""
class Person:

    # 类的构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类方法
    @classmethod
    def create_instance_from_string(cls, strInfo):
        """通过传入的字符串来创建实例"""
        name, age = strInfo.split("-")
        return cls(name, int(age))
    
    def __str__(self):
        return f"{self.name} --> {self.age}"

# 通过类的构造方法创建实例
person1 = Person("贾飞天", 18)
print(person1)  # 贾飞天 --> 18

# 使用类方法直接通过字符串来创建对象
person2 = Person.create_instance_from_string("张三天-20")
print(person2)  # 张三天 --> 20

"""
    使用类方法来实现单例模式
"""
class Database:

    # 存储单例对象
    _instance = None

    def __init__(self, name):
        self.name = name
    
    # 在 Python 中, __new__ 方法负责控制实例的创建
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    # 标记为类方法
    @classmethod
    def get_instance(cls, name="DefaultDB"):
        """确保类只有一个实例"""
        if cls._instance is None:
            cls._instance = cls(name)
        # 返回单例对象
        return cls._instance

Database("1212")

# 通过类对象创建一个MainDB的单例对象
mainDB = Database.get_instance("MainDB")
# 尝试创建一个 BackupDB 对象
db2 = Database.get_instance("BackupDB")

# 因为是单例模式, 所以所谓的两个类对象实际上是一个
print(mainDB is db2)  # True

# 可以看到,两个类实例对象的name属性是相同的
print(mainDB.name)  # MainDB
print(db2.name)  # MainDB
