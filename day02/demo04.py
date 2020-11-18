'''
字典dict
key:value
字典是无序的
key是唯一的
value可以重复
'''
names = ['徐美斌','白宝蕾','陈杏梅','党海斌','冯凯']
scores = [88,60,90,95,77]

# 字典
# 字典是无序的
d = {'徐美斌':88,'白宝蕾':60,'陈杏梅':90,'党海斌':95,'冯凯':95}
# 查
print(d['徐美斌'])
# GB  TB  PB
# 增
d['文杰英'] = 70
print(d)
# 改
d['白宝蕾'] = 99
print(d)

# 异常
if '徐美兵' in d: # 查看字典d中是否包含一个叫做'徐美兵'的可以，是则返回true，否则返回false
    print(d['徐美兵'])

print('徐美兵' in d)
print('welcome')

# get(key)方法获取key对应的value，如果key不存在，则返回None
print(d.get('徐美兵')) 

# 删除
value = d.pop('徐美斌') # 返回值是key对应的value
print(value)
print(d)

# set
