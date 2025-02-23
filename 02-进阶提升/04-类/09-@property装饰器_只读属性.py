class Config:
    
    # 用于将方法变为只读属性
    @property
    def PI(self):
        return 3.14159

config = Config()
print(config.PI)  # 3.14159

try:
    # 尝试进行修改，因为属性是只读的，所以报错了
    config.PI = 3.14
except Exception as e:
    print(e)  # property 'PI' of 'Config' object has no setter
