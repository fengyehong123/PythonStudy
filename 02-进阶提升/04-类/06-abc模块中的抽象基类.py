# 在 Python 中，可以用 抽象基类（Abstract Base Class, ABC） 来实现类似 Java 接口的行为：
from abc import ABC, abstractmethod

# 定义抽象基类（类似 Java 接口）
class Animal(ABC):

    # 定义子类必须实现的抽象方法
    @abstractmethod
    def make_sound(self):
        pass

# 具体子类必须实现抽象方法，否则会报错
class Dog(Animal):

    def make_sound(self):
        return "我是狗, 我汪汪的叫..."

class Cat(Animal):

    def make_sound(self):
        return "我是猫, 我喵喵的叫..."


try:
    # 不能实例化抽象类，会报错
    Animal()
except Exception as e:
    print(e)  # Can't instantiate abstract class Animal without an implementation for abstract method 'make_sound'

dog = Dog()
print(dog.make_sound())  # 我是狗, 我汪汪的叫...

cat = Cat()
print(cat.make_sound())  # 我是猫, 我喵喵的叫...
print('\033[91m-----------------------------------------------\033[0m')

def make_sound(animal: Animal):
    print(animal.make_sound())
    # 我是狗, 我汪汪的叫...
    # 我是猫, 我喵喵的叫...

for animal in [dog, cat]:
    make_sound(animal)