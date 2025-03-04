"""
    __str__用来打印类对象的时候,显示定义好的信息
    __repr__和__str__的作用类似,在命令行输入类对象的时候,打印的是__repr__的信息
    注意: 当一个类中只有__repr__的时候,repr会替代__str__的作用
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):

       return f"name={self.name}, age={self.age}"

    # 当在命令行或者类中不存在 __str__ 方法的时候, __repr__ 方法会起到作用
    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"


p = Person("枫叶红", 24)
print(p)  # name=枫叶红, age=24


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 当在命令行或者类中不存在__str__方法的时候,__repr__方法会起到作用
    def __repr__(self):
        return f"name: {self.name}, age: {self.age}"


s = Student("张三", 24)
print(s)  # name: 张三, age: 24