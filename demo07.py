'''
函数的参数
'''

'''
positional argument:位置参数
调用函数时，位置参数必须传参，并且是按照形参的位置传递实参
'''

def power (x):  # x为形参
    return x*x

# TypeError: power() missing 1 required positional argument: 'x'
# print(power())

print(power(0)) # 3为实参