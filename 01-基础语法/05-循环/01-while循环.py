"""
    使用 while 循环来计算 1 到 100 的总和
"""

# 总和
sumCount = 0

# 计数
counter = 1
n = 100

while counter <= n:
    sumCount = sumCount + counter
    counter += 1
# 如果 while 后面的条件语句为 false 时，则执行 else 的语句块
else:
    print('while循环执行完毕...')  # while循环执行完毕...
print(f"1到{n}之间的和为: {sumCount}")  # 1到100之间的和为: 5050

# 使用无限循环
flag = True
while True:
    try:
        num = int(input("输入一个数字  :"))
        print(f"你输入的数字是: {num}")
    except Exception as e:
        print(e)
        print('你输入的不是数字，请重新输入...')
    