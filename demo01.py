'''
元组tuple
'''

# 定义元组，元组使用小括号定义
names = ('董洁','王菲','李芷','郑爽','欧阳')
# 元组是不可变的
print(names[0])
# 'tuple' object does not support item assignment
# names[0] = '张一山'
print(names)

# 定义单个元素时，需要加一个逗号
t = ('tom',)
print(t)

# 定义空元组
s = ()
print(s)

# 元组真的不可变吗？
t = ('tom','mike',['julia','jerry'])
print(t)
print (t[2][0])
(t[2][0]) = 'angela'
print(t[2][0])
print(t)