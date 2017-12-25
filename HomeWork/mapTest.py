#测试map()函数
#map函数第一个参数是一个函数，第二个参数是一个列表，将列表中的每个参数依次调用函数，并最后返回一个列表
'''
def transform(name):
   return name.title()

names=['adam', 'LISA', 'barT']

for r in map(transform,names):
    print(r)
'''


#测试reduce()函数
#reduce()函数，第一个参数是一个函数，第二个参数是一个列表，reduce函数将通过参数计算的结果作为下一次内置函数计算的参数
'''
from functools import reduce

def calculate(x,y):
    return x*y
def prod(L):
    return (reduce(calculate,L))

print(prod([1,2,3,4]))
'''

'''
from functools import reduce

def prod(L):
    return (reduce(lambda x,y:x*y,L))

print(prod([1,2,3,4]))
'''


'''
#将字符串转为浮点数
from functools import reduce
import math
def str2float(s) :
    count=0

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':'.'}[s]

    def fn(x,y):

        nonlocal count
        if(y=='.'):
            count=1
            return x
        else:
            if (count==0):
                return x*10+y
            else:
                x=x+y*math.pow(0.1,count)
                count = count + 1
                return x

    return reduce(fn,map(char2num,s))

print(str2float('123.456'))

'''


'''
#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_palindrome(n):
    l=[]
    while(n>0):
        m=n%10
        n=(int)(n/10)
        l.append(m)
    length=l.__len__()
    print(length)
    for x in range((int)(length/2)):
        if l[x]!=l[length-1-x]:
           return False
    return True
if(is_palindrome(101101)):
    print('true')
'''


#sorted()函数第一个参数是变量，第二个参数可以通过key指定一个函数，
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
'''
def by_name(t):
   return t[0].lower()
L2 = sorted(L, key=by_name)
print(L2)


def by_score(t):
    return t[1]
L3 = sorted(L, key=by_score)
print(L3)

'''

'''
#函数作为返回值
def createCounter():
    i=1
    def counter():
        nonlocal i
        j=i
        i+=1
        return j
    return counter
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())
counterB = createCounter()
print(counterB(), counterB(), counterB(), counterB(), counterB())

'''



'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__=='__main__':
    test()
'''



