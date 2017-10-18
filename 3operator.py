
#python逻辑运算符  not用来取反
'''
a=True;
print(not a)
'''

#python成员运算符
'''
a=1
b=20
list=[1,2,3,4,5]
if(a in list):
    print('1.变量a在list中')
else:
    print('1.变量a不在list中')


if(b not in list):
    print('2.变量b不在list中')
else:
    print('2.变量a在list中')
'''

#python身份运算符
'''
a=20;
b=20;

print(a is b)
print(a is not b)
print(id(a)==id(b))     # id() 函数用于获取对象内存地址。

b=30
print(a is b)
print(a is not b)
'''

#2进制，8进制和16进制的输出
a=0b1000
b=0o0011
c=0x0010
print(a)
print(bin(a))

print(b)
print(oct(b))
print(c)
print(hex(c))

#python是以内容为基准的，只要内容相同，指向的内存是相通的，python中没有++操作
num1=5
num2=5
print(num1 is num2)
print(id(num1))
print(id(num2))









