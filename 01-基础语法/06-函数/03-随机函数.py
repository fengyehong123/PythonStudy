# 导入随机模块
import random

# choice() 方法返回一个列表，元组或字符串的随机项。
# 语法: random.choice( seq )

# 返回0到99的随机数(不包含100)
random1 = random.choice(range(100))
print(random1)  # 14

# 返回字符串中的随机字符
print(random.choice("123456789"))  # 6

"""
    如果要随机返回多个数字的话
    需要使用 random.choices(), 而不是 random.choice()
"""
random2 = random.choices(range(10), k = 3)
# 返回的值中可能存在重复值
print(random2)  # [6, 6, 3]

# 如果不想返回重复值的话，需要使用 random.sample(seq, k)
random3 = random.sample(range(10), k = 3)
print(random3)  # [1, 8, 2]

# 导入字符串模块
import string

# 创建一个密码生成器的函数
def generate_password(length):
    """
    定义密码可用字符集合
        string.ascii_letters
            所有字母（大写和小写）
        string.digits
            所有数字
        string.punctuation
            所有标点符号
    """
    chars = string.ascii_letters + string.digits + string.punctuation

    # 随机选择字符生成密码
    return ''.join(random.choice(chars) for _ in range(length))

# 调用函数生成一个6位数字的密码
random_passwd = generate_password(6)
print(random_passwd)  # Ed^%ba

# 生成0到4的随机数
for _ in range(random.randint(1, 4)):
    print("hello world...")