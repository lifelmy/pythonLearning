'''
def welcome(name,age=10):
    print("wolcome", name,"---","age=",age)
welcome("lmy",10)
'''

'''
#传递列表类似于引用传递
def change(a):
    a[2]=0

a=[1,2,3,4]
change(a)
print(a[2])
'''

'''
#在后面加上end="",实现下一行接着该行输出，不换行
print("123",end="")
print("456")
print("789")
'''

'''
from sys import argv,path
print('=========================Python import mode==================================')
for i in argv:
    print(i)
print(path)
'''
'''
str='lifelmy'
print(str)
print(str[0:-2]) # 输出第一个到倒数第二个的所有字符
print(str[1:])
'''

'''
a=20;
b=20;
print(a is b)   #true
print(id(a) is id(b))   #false   id()取得是地址
'''

'''
#python是以内容为基准的，只要内容相同，指向的内存是相通的，python中没有++操作
num1=111111111111111111
num2=111111111111111111
print(num1 is num2)         #true
print(id(num1))
print(id(num2))

str1='ddddddddddd'
str2='ddddddddddd'
print(str1 is str2)         #true
'''

'''
#5,6,7,8,9
for i in range(5,10):
    print(i)
'''

'''
#使用迭代器返回的结果    1   2
list1=[1,2,3,4]
it=iter(list1)
print(next(it))
print(next(it))
'''

'''
#1 2 3 4
list1=[1,2,3,4]
it=iter(list1)
for x in it:
    print(x)
'''
'''
#对于异常的处理
import  sys
list1=[1,2,3,4]
it2=iter(list1)
while True:
    try:
        print(next(it2))
    except StopIteration:
        sys.exit()
'''


'''
#使用生成器
#使用yeild类似于一个中断，当执行到Yeild的时候中断返回一个数据，然后再次调用next的时候继续执行
import  sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1
#在for循环中，会自动遵循迭代规则，每次调用next()函数
for x in fibonacci(10):
    print(x)


#不使用for循环，每次调用next方法
f=fibonacci(10)
while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
'''

'''
#可变参数
def show(name,gender,*vartuple ):
    print("name:", name,"\ngender:",gender)
    for x in vartuple:
        print(x)
show('snow','male',1,2,3,4,)

'''

'''
#如果在方法中需要修改全局变量，先使用global关键字声明一下，再进行修改
a=1
def change():
    global a
    a=2
change()
print(a)
'''


'''
#内部方法要修改外部方法的变量，需要nonlocal关键字
def outer():
    a=2
    def inner():
        nonlocal a
        a=3
    inner()
    print(a)

outer()
'''