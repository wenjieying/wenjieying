'''
循环结构
循环次数已知,用for循环
循环次数未知,用while循环
'''

s = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(s)

# for循环(重点)
s = 0
for i in (1,2,3,4,5,6,7,8,9,10):
    '''
    第一次循环
    i = 1
    s = 0 + 1
    第二次循环
    i = 2
    s = 1 + 2
    第三次循环
    i = 3
    s = 3 + 3
    '''
    s = s + i
print(s)

names = ('徐美斌','白宝蕾','陈杏梅','党海斌','冯凯')
# print(names[0])
# print(names[1])
# 遍历列表
for name in names:
    print(name)

# range()函数-生成一个整数数列
print(list(range(0,5,1)))
print(list(range(5)))
print(list(range(5,10)))
# 10以内的奇数
print(list(range(1,10,2)))
# 100以内的偶数
print(list(range(0,101,2)))
# 10，9，8，7，6，5，4，3，2，1
print(list(range(10,0,-1)))

# 求0-100的和
s = 0
for i in range(101):
    s = s + i
print(s)


# while循环

# 求100以内的偶数的和
s = 0
n = 100
while n>0:
    s = s + n
    n = n - 2
print(s)

# break 终止循环
# 当和大于50时终止
s = 0
for i in range(101):
    if s>50:
        break #提前终止循环
    s = s + i
print(s)


# continue
# 求100以内的偶数的和
s = 0
n = 0
while n<101:
    n = n + 1
    if n%2!=0: #奇数
        continue # 跳过当前循环
    s = s + n
print(s)

# 死循环
s = 0
# while True:
#     s += 1 # s = s + 1
#     print(s)

# 非 False,0,None以外的值，都可以看做True
# while 1: 
#     s += 1
#     print(s) 