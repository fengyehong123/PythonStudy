"""
    Python 3.10 引入了 match-case 结构，
    可以用于类实例匹配，非常适合解析 JSON 或解构数据对象。
"""
# 创建一个图形类
class Shape:
    pass

# 创建一个圆类, 继承图形类
class Circle(Shape):

    # 圆的半径
    def __init__(self, radius):
        self.radius = radius

# 创建一个长方形类, 继承图形类
class Rectangle(Shape):

    # 长方形的宽和高
    def __init__(self, width, height):
        self.width = width
        self.height = height

# 获取图形的面积
def get_area(shape: Shape):
    
    match shape:
        # 如果该图形是圆形, 则解构出原型的半径
        case Circle(radius = r):
            # 计算原型的面积
            return 3.14 * r * r
        # 如果该图形是长方形, 则解构出长方形的宽和高
        case Rectangle(width = w, height = h):
            # 计算长方形的面积
            return w * h
        case _:
            return "Unknown shape"

# 计算圆形的面积
print(get_area(Circle(10)))  # 314.0
# 计算长方形的面积
print(get_area(Rectangle(4, 5)))  # 20
print('\033[91m-----------------------------------------------\033[0m')

# 导入json模块
import json

# 定义一个json字符串
json_data = '''
{
    "type": "message",
    "sender": "贾飞天",
    "content": "好久不见, 你还过的好吗?"
}
'''

# 将json字符串转换为json对象
data = json.loads(json_data)
print(type(data))  # <class 'dict'>

# 使用 match-case 进行模式匹配
match data:
    case {"type": "message", "sender": sender, "content": content}:
        print(f"收到来自 {sender} 的消息：{content}")  # 收到来自 贾飞天 的消息：好久不见, 你还过的好吗?
    case {"type": "notification", "message": message}:
        print(f"通知：{message}")
    case _:
        print("未知数据类型")