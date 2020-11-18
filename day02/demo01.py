'''
元组tuple
'''

# 定义元组 ，元组使用小括号定义
names = ('徐美斌','白宝蕾','陈杏梅','党海斌','冯凯')
# 元组是不可变的
print(names[0])
# 'tuple' object does not support item assignment
# names[0] = '陆凯利'
print(names)

# 定义单个元素时，需要加一个逗号
t = ('tom',)
print(t)

# 定义空元组
s = ()
print(s)

# 元组真的不可变吗？
# 可以给元组里插入列表
p = ['julia','jerry']
t = ('tom','mike',p)
print(t)
print(t[2][0])
t[2][0] = 'angela'
print(t[2][0])
print(t)