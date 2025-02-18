# 创建一个类
class Person:

    """
        类的构造方法
        self代表类的实例对象
    """
    def __init__(self, name, age):
        # 类中的公开属性
        self.name = name
        # 单下划线 _ 开头的属性或方法被称为受保护的 (protected)
        # 类的外部虽然也可以访问, 但是约定俗成不要在类的外部访问
        self._hobby = ["吃饭", "睡觉", "打豆豆"]
        # 双下划线 __ 开头的类中的私有属性, 类的外部无法访问
        self.__age = age

    # Python中的普通方法
    def drink(self, liquid):
        print(f"名字叫做{self.name}的人,正在喝{liquid}")
    
    """
        Python中的私有方法和私有属性类似
        都是以 __ 开头
    """
    def __sleep(self):
        print("__sleep的私有方法执行了...")

    """
        重写 __str__ 方法
        修改打印异常类时显示在控制台上的字符串
    """
    def __str__(self):
        # 类的私有方法可以在类的内部使用
        self.__sleep()  # __sleep的私有方法执行了...

        # 类的私有属性无法通过类的实例对象来访问, 但是可以在类的内容自由使用
        return f"姓名:{self.name} → 年龄:{self.__age}"

# 创建一个类的实例对象
person = Person("贾飞天", 18)

# 因为类的 __str__ 方法已经被重写, 因此我们打印类实例对象的输出内容是自定义的
print(person)  # 姓名:贾飞天 → 年龄:18

# 调用类的方法
person.drink("啤酒")  # 名字叫做贾飞天的人,正在喝啤酒

try:
    # 类的实例对象访问公开属性
    print(person.name)  # 贾飞天

    # 受保护的属性约定俗称不建议在类的外部访问, 但还是可以直接访问的
    print(person._hobby)  # ['吃饭', '睡觉', '打豆豆']

    # 因为age是私有属性, 因此无法通过实例对象来访问
    print(person.age)
except Exception as e:
    print(e)  # 'Person' object has no attribute 'age'

"""
    Python 实际上并不真正支持严格的私有, 而是采用名称重整 (Name Mangling)
    __age 的私有属性会被Python内容重命名为 _Class名称__私有属性名称
    从而避免了从外部直接访问
"""
# 但是还是可以通过下面的这种方式进行访问(不建议这么做)
print(person._Person__age)

try:
    # 私有方法和私有属性相同, 都无法通过类的实例进行访问, 都只能在类的内部使用
    person.sleep()
except Exception as e:
    print(e)  # 'Person' object has no attribute 'sleep'

"""
    使用下面这种方法也可以在类之外, 使用类的实例对象来访问类的私有方法(不建议这么做)
"""
person._Person__sleep()  # __sleep的私有方法执行了...