'''
def area(width,height):
    return width*height

def printMe():
    print("printMe")

print(area(5,6))
printMe()
'''

#传递不可变对象和可变对象
#不可变对象： 整数、字符串、元组,类似于传递的是形参
#可变对象： 列表，字典，类似于引用传递
'''
def change(a):
    a[0]=0

b=[1,2,3]
change(b)
print(b)
'''


#关键字参数(调用时的参数顺序可以和方法定义时不一样)
'''
def show(name,age):
    print("name:",name,"age",age)
show(age=16,name='hehe')
'''

#默认参数

def show(name,gender,age=20):
    print("name:", name, "age", age,"gender",gender)
show(gender='male',name='sb')
show(gender='male',name='sb',age=12)


#可变参数

'''
def show(name,gender,*vartuple ):
    print("name:", name,"\ngender:",gender)
    for x in vartuple:
        print(x)
show('snow','male',1,2,3,4,)
'''

#匿名函数
'''
sum=lambda a,b:a+b
print(sum(1,2))
'''

#使用return返回
'''
def sum(a,b):
    return a+b
total=sum(3,2)
print(total)
'''

#变量作用域


'''
x = int(2.9)  # 内建作用域
print(x)
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
'''

#if/while/for中定义的变量外部可以使用,但是在方法中定义的变量外部是不能访问的，这一点和以前一致
'''
if True:
    a=100

def test():
    print(a)

test()
'''

#如果在方法中需要修改全局变量，先使用global关键字声明一下，再进行修改
'''
a=1
def change():
    global a
    a=2
change()
print(a)
'''

#内部方法要修改外部方法的变量，需要nonlocal关键字
'''
def outer():
    a=10
    def inner():
       nonlocal a
       a=5

    inner()
    print(a)
outer()

'''

