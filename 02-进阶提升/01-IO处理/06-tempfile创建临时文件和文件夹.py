"""
    tempfile 模块提供了多种创建临时文件和临时目录的方法，通常用于测试和需要短期使用的文件。
    它为临时文件的创建提供了一个简单、安全的接口。
"""
import tempfile

# 指定以可读写模式创建一个文件
with tempfile.TemporaryFile(mode='w+', encoding='utf-8') as temp_file:

    # 写入一些测试数据
    temp_file.write("我写入了一些测试数据")

    """
        当文件完成写入之后，文件指针此时的位置位于数据的末尾
        因此需要通过下面这行代码将文件指针移到文件的开头
        这样通过 .read() 方法读取到的才不会是空数据
    """
    temp_file.seek(0)  
    # 从开头读取数据
    print(temp_file.read())
print('\033[91m-----------------------------------------------\033[0m')

"""
    创建临时文件，指定模式、编码、前缀、后缀等
    创建的文件可以通过name属性来获取临时文件的路径
    由于指定了 delete=False , 所以文件并不会自动被删除, 需要手动删除
"""
# 将参数放入字典进行封装
temp_file_params = {
    'mode': 'w+',
    'encoding': 'utf-8',
    'prefix': 'my_temp_',
    'suffix': '.txt',
    'delete': False
}
# 通过 kwargs 的方式对字典进行解包，简化代码
with tempfile.NamedTemporaryFile(**temp_file_params) as temp_file:

    # 获取临时文件的路径
    filePath = temp_file.name
    print(f"临时文件名：{filePath}")

    # 写入数据之后,将文件的指针放到文件的开头
    temp_file.write(f"我是 → {filePath} 文件中的临时数据")
    temp_file.seek(0)

    # 读取数据
    print(temp_file.read())
print('\033[91m-----------------------------------------------\033[0m')

"""
    tempfile.mkstemp()
        创建一个临时文件并返回文件描述符和路径。
        它不会自动删除，适用于需要文件描述符的场景。
"""
fd, path = tempfile.mkstemp()
print(f"临时文件路径: {path}")

with open(fd, 'w+', encoding='utf-8') as f:
    f.write("写入一些临时数据...")
    f.seek(0)
    print(f.read())
print('\033[91m-----------------------------------------------\033[0m')

"""
    tempfile.mkdtemp()
        创建一个临时目录并返回其路径。临时目录不会自动删除。
"""
temp_dir = tempfile.mkdtemp()
print(f"临时目录路径: {temp_dir}")
print('\033[91m-----------------------------------------------\033[0m')

"""
    tempfile.gettempdir()
        返回系统使用的临时目录路径。
"""
temp_dir = tempfile.gettempdir()
print(f"系统临时目录: {temp_dir}")