'''
函数
'''
import math

# y = f(x,y) = 2x+5y+3+9......
# f(5)+g(5)

# 自定义函数
# def : define，定义函数
# f : 函数名
# (x):参数列表
def f(x): # f(x) = x*x
    # 函数体
    return x*x # return：指定返回值

# 系统函数
print('hi')
print(int('12'))
print(abs(-5))
# 调用函数
print(f(3))

# 自定义一个my_abs函数,实现求绝对值的功能
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-3))

def g(): # 可以没有参数
    print('hi')
    return 3
    # return #可以没有return语句

r = g()
print(r)

# 多个返回值
def move(x,y,step,angle):
    nx = x + step*math.cos(angle)
    ny = y + step*math.sin(angle)
    # return [nx,ny]
    # 原则上只能返回一个值
    # 当有多个值返回时，会自动封装为一个元组
    return nx,ny  #(nx,ny)

print(move(4,10,5,math.pi/6))
x, y = move(4,10,5,math.pi/6) # 自动拆箱
print(x,y)
