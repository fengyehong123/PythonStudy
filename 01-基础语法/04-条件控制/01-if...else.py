# if else 语句
age = 18

if age < 18:
    print('未成年')
elif age >= 18 and age <= 35:
    print('青年人')  # 青年人
elif age > 35 and age <= 50:
    print('中年人')
else:
    print('老年人')

flag1 = True
if flag1:
    print('flag的值是True')  # flag的值是True

flag2 = False
if not flag2:
    print('flag的值是Flase')  # flag的值是Flase