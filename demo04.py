'''
字典dict
key：value
同一字典中，key是唯一的；value可以重复
'''
names = ['董洁','王菲','李芷','郑爽','欧阳']
scores = [88,60,90,95,77]

# 字典
# 字典是无序的 
# 只能有一个 value
d = {'董洁':88,'王菲':60,'李芷':90,'郑爽':95,'欧阳':77}
# 查询
print(d['董洁']) #通过key来获得value
d['若水'] = 70
print(d)
# 修改
d['李芷'] = 80
print(d)

# 异常
if '董杰' in d: # 查看字典d中是否包含一个叫‘董杰’的人，若可以，返回true，否则返回false
    print(d['董杰'])
print('董杰' in d)
print('welcome')

# get()方法获取可以对应的value，如果key不存在，则返回None
print(d.get('董杰'))

# 删除
value = d.pop('董洁')# 返回值是key对应的value
print(value)
print(d)

# list和dict的区别
# list 节省空间   运做慢
# dict 浪费空间 冗余50%-70%的空间   运做快
       #空间换时间