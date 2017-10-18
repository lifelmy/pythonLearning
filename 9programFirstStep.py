# Fibonacci series: 斐波纳契数列
a,b=0,1
while b<10:
    print(b)
    a,b=b,a+b   #右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。

a,b=0,1
while b<100:
    print(b,end=' ')
    a,b=b,a+b

#print() sep 参数使用,分隔各个输出元素
print()
a,b,c=1,2,3
print(a,b,c,sep='#')


def fab(n):
    if n<1:
        print('输入有误，请重新输入')
        return -1
    if  n==1 or n==2:
        return 1
    else:
        return fab(n-2)+fab(n-1)

print(fab(4))