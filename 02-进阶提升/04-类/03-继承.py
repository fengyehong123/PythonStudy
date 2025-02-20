# 定义一个动物的父类
class Animal:

    def speak(self):
        print("动物会说话...")
    
    def drink(self):
        print("动物会喝水...")

# 定义一个狗的子类, 继承动物的父类
class Dog(Animal):

    # 子类重写父类的方法
    def speak(self):
        print("狗正在说话...")
    
    def otherSkill(self):
        # 在子类中通过 super() 来调用父类中的方法
        super().drink()

# 实例化一个dog对象
dog = Dog()

dog.speak()  # 狗正在说话...
dog.otherSkill()  # 动物会喝水...

# 定义一个普通的类, 该类并没有继承任何父类
class BigDog:

    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"名字叫做{self.name}的狗, 会工作...")
    
    def drink(self):
        print(f"名字叫做{self.name}的狗, 会喝水...")

"""
    Python 支持多重继承，即一个子类可以继承多个父类。
"""
class SuperDog(BigDog, Animal):

    """
        子类重写继承自父类的 __init__ 方法
        子类如果不重写 __init__ 方法的话, 
        Python 会按照 MRO 继承最近的 __init__ 方法（在 MRO 列表中靠前的类）
    """
    def __init__(self, name):
        # 调用父类中的构造方法
        super().__init__(name)
        self.superName = name

    def study(self):
        print(f"{self.superName}居然可以学习...")

# 创建一个子类对象
superDog = SuperDog("智能狗狗")
# 子类调用父类的方法
superDog.work()

"""
    子类继承的两个父类都有drink方法, 此时按照继承的先后顺序来
    Python 使用 Method Resolution Order (MRO) 来确定方法调用的顺序。
"""
print(SuperDog.mro())  # [<class '__main__.SuperDog'>, <class '__main__.BigDog'>, <class '__main__.Animal'>, <class 'object'>]
superDog.drink()  # 名字叫做智能狗狗的狗, 会喝水..

# 子类调用自己独有的方法
superDog.study()  # 智能狗狗居然可以学习...

