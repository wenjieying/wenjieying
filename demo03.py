'''
循环结构
#while和if的区别
#知道循环次数，就用for循环；一般用for循环
# 不知道循环次数，用while循环
'''

s = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(s)

# for循环(重点)
s = 0
for i in [1,2,3]:
    '''
    第一次循环
    i = 1
    s = 0 + 1 = 1
    第二次循环
    i = 2
    s = 1 + 2 = 3
    第三次循环
    i = 3
    s = 3 + 3 = 6
    第四次执行
    无元素，退出循环
    '''
    s = s + i

print(s) #输出s

names = ('董洁','王菲','李芷','郑爽','欧阳')
#遍历列表
for name in names:
    print(name)

# range()函数-生成一个整数数列,range是可迭代对象
print(list(range(0,5)))
print(list(range(5)))
# 前边闭区间，后边开区间
print(list(range(5,10))) 
# 10以内的奇数；(2)是步长
print(list(range(1,10,2))) 
# 100以内的偶数
print(list(range(0,101,2))) 
#递减
print(list(range(10,0,-1))) 
print(list(range(0,-101,-1))) 

# 求0-1000的和
s = 0
for i in range(101):
    s = s + i
print(s)

# 求100以内的偶数的和
q = 0
for t in range(0,101,2):
    q = q + t
print(q)

#while循环
#求100以内的偶数的和
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
    if s >50:
        break#提前终止循环
    s = s + i
print(s)

# 求100以内的偶数的和
s = 0
n = 0
while n < 101:
    n = n + 1
    if n%2!=0:#奇数
        continue#跳出当前循环
    s = s + n
print(s)

# 死循环
# s = 0
# while True:
#     s += 1  # s = s + 1
#     print(s)

#非 false,0,None以外的值，都可以看作True
# s = 0
# while 1:
#     s += 1 
#     print(s)