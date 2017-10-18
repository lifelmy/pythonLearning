'''
age=int(input('请输入狗的年龄'))
print('')
if age<0:
    print('逗我吧。。。')
elif age==1:
    print('相当于人14岁')
else:
    print('不谈了')

i=0
sum=0
while i<=100:
    sum+=i
    i+=1
print(sum)

languages=['java','c++','c','python']
for x in languages:
    print(x)
    if x=='c':
        break

'''

'''
for i in range(5,10):
    print(i)
'''

#循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,
#但循环被break终止时不执行。
'''
for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"等于",x,"*",n//x);
            break;
    else:
        print(n,'是质数')

'''
#使用迭代器
'''
list1=[1,2,3,4]
it=iter(list1)
print(next(it))
print(next(it))
'''

'''
list1=[1,2,3,4]
it=iter(list1)
for x in it:
    print(x)
'''

'''
import  sys
list1=[1,2,3,4]
it2=iter(list1)
while True:
    try:
        print(next(it2))
    except StopIteration:
        sys.exit()
'''

#使用生成器
import  sys
def fibonacci(n):
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b=b,a+b
        counter+=1

for x in fibonacci(10):
    print(x)

'''
f=fibonacci(10)
while True:
    try:
        print(next(f),end="")
    except StopIteration:
        sys.exit()
'''












