
'''
#基本变量赋值
counter=100
miles=1000.00
name='lmy'
print(counter)
print(miles)
print(name)
'''

'''
#多个变量赋值
a=b=c=1
print(a,end="")
print(b,end="")
print(c)

a,b,c=1,2,'lmy'
print(a)
print(b)
print(c)

'''

'''
#获取变量类型
#type()不会认为子类是一种父类类型。
#isinstance()会认为子类是一种父类类型。

a,b,c,d,e=20,5.5,True,4+3j,"hello"
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(isinstance(e,str))


class A:
    a=10

class B(A):
    b=10

print(isinstance(B(),A))
print(type(B())==A)

'''

'''
# /得到浮点数    //得到一个整数
#   **乘方
a,b=2,4
print(a/b)
print(a//b)
print(a%b)
print(a*b)
print(a**b)
'''

'''
#String
str='lifelmy'
print(str)
print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
print(str[0])
print(str[2:5])  # 输出从第三个开始到第五个的字符,开始取到，结束不取
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str*2)
print(str+" is the best")


#Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
print('ru\nnoob')
print(r'ru\nnoob')

word='lifelmy';
print(word[0],word[5])
print(word[-1])
word='123jkl'
print(word)

#Python中的字符串不能改变，下面修改的代码会报错
#word[0]='a'
#print(word)

'''

#list的操作
'''
list=['abcd',123,1.2,'hello',23.3]
tinylist=[232,'dasdf']
print(list)
print(list[0])
print(list[1:3]) #输出从第二个到第四个（不包含）的元素
print(list[2:]) #输出从第3个到最后的元素
print(tinylist*2) #重复两次
print(list+tinylist)#连接操作

a=[1,2,3,4,5];
#为list中的元素重新赋值
a[0]=0;
a[1:4]=[1,2,3]
print(a)
#0,1,2,3,5
a[2:4]=[]   #删除
print(a)
'''

#元组的操作(Tuple)
'''
#基本操作，输出元素，拼接
tuple=('abcd',132,32.3,'hello',232.3333)
tinytuple=(123,'world')
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tinytuple*2)
print(tuple+tinytuple)

#tuple[0]='a'  报错，与list不同的是，元组不支持修改元素，与字符串一样，因此可以说字符串是特殊的元组
#但是元组中可以包含可变的对象，如list
list1=[2,3,4]
list2=[5,6,7]
tuplelist=(list1,list2)
print(tuplelist)

#空元组和只有一个元素的元组比较特殊
tup1=()
#只有一个元素的元组，需要加一个逗号，如果不加逗号，例如tup2=(2),这样tup2只是2这个数字，而不是元组了
tup2=(2,)
print(tup1)
print(tup2)
'''

#Set:无序不重复的序列
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典

'''
student={'jon','tim','andy','jon','helen'}
student2=set('spam')
student3=set([2,3,5,8])
print(student)  #输出{'andy', 'helen', 'jon', 'tim'},重复的元素会被去掉
print(student2)  #输出{'a', 's', 'm', 'p'},无序
print(student3)  #输出{8, 2, 3, 5}

if('jon' in student):
    print('jon 在集合中')
else:
    print('jon 不在集合中')

a=set('abcd')
b=set('abce')
print(a-b)  #计算a和b的差集
print(a|b)  #计算a和b的并集
print(a&b)  #计算a和b的交集
print(a^b)  #计算a和b不同时不存在的元素

'''

#Dictionary字典
#列表是有序的对象结合，字典是无序的对象集合。key-value

'''
dict={}
dict['one']="菜鸟教程"
dict[2]="菜鸟工具"
tinydict={"name":'lmy','age':22,'gender':'male'}
print(dict['one'])
print(dict[2])
print(tinydict)
print(dict.keys())
print(dict.values())

for x in (2,4,6):
    dict.__setitem__(x,x**2)
print(dict)
print('========================================')
seconddict={"name":'lmy','age':22,'gender':'male'}

for c in seconddict:
    print(c,":",seconddict[c])

'''
























