from typing import NamedTuple, List, Tuple

"""
    NamedTuple 允许你创建类似 class 的 不可变对象
    但它的底层仍然是 元组，适用于存储结构化数据。
"""
class Message(NamedTuple):
    
    # 消息ID（字符串）
    msgid: str
    # 符号（字符串）
    symbol: str
    # 旧名字的列表，默认值为空列表
    old_names: List[Tuple[str, str]] = []

# 通过这一些参数创建一个类的实例对象
paramDict = {
    "msgid": "110120",
    "symbol": "→",
    "old_names": [
        ("name1", "贾飞天"),
        ("name2", "枫叶红")
    ]
}
msg = Message(**paramDict)
print(msg)  # Message(msgid='110120', symbol='→', old_names=[('name1', '贾飞天'), ('name2', '枫叶红')])

try:
    # 由于是不可变对象, 因此无法修改实例对象的属性
    msg.symbol = '○'
except Exception as e:
    print(e)  # can't set attribute



