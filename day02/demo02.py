'''
程序3大结构
    顺序
    分支
    循环
'''

'''分支'''
age = int(input('请输入年龄：')) # "22" "abc"
# if和else是互斥的，只能执行一个
if age<18:
    print("你今年是%d岁"%age)
    print('未成年')
elif age<30:
    print('青年')
elif age<60:
    print('中年')
else:
    print("你今年是%d岁"%age)
    print('老年')

print("鉴定完毕！")

