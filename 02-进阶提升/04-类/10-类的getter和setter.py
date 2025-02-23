"""
    可以封装私有属性
    可以控制 setter 行为
    可以禁止 del 操作
"""
class Person:

    def __init__(self, name, age, num):
        # 设置私有属性
        self.__name = name
        self.__age = age
        self.__num = num

    """
        只读属性
        相当于Java中的getter
    """
    @property
    def name(self):
        return self.__name
    
    @property
    def num(self):
        return self.__num
    
    """
        相当于设置计算属性
    """
    @property
    def nameUpper(self):
        return self.__name.upper()

    """
        相当于Java中的setter
        @属性名.setter
    """
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("名字不能为空")
        self.__name = value
    
    # @属性名.setter
    @num.setter
    def num(self, value):
        if not value:
            raise ValueError("num不能为空")
        self.__num = value

    """
        禁止属性被删除
    """
    @name.deleter
    def name(self):
        raise AttributeError("名字不能被删除")

person = Person("贾飞天", 18, 20)
# 因为使用了 getter, 所以可以获取到私有属性
print(person.name)  # 贾飞天

try:
    # 因为是私有属性, 并且没有设置getter, 所以报错了
    print(person.age)
except Exception as e:
    print(e)  # 'Person' object has no attribute 'age'

# 因为设置了 setter , 所以私有属性可以修改成功
person.name = "fengyehong"
print(person.name)  # fengyehong

try:
    # 尝试去删除私有属性, 因为设置了 @name.deleter, 所以无法删除
    del person.name
except Exception as e:
    print(e)  # 名字不能被删除

# 计算属性
print(person.nameUpper)  # FENGYEHONG
print('\033[91m-----------------------------------------------\033[0m')

# 设置num属性值
person.num = 10
print(person.num) # 10
