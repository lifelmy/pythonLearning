#删除列表元素
list=['google','baidu','yahoo']
del list[1]
print(list)

#拼接列表
list2=[1,2,3]+list
print(list2)

#嵌套列表
list3=[list,list2]
print(list3[0])
print(list3[0][0])

#列表函数
list4=[1,2,3,4]
print('list4中的最大元素%d'%(max(list4)))
print('列表长度%d'%(len(list4)))

list4.append(5)
print(list4)

#a,b,c都指向同一个内存单元，改变一个其它的都会改变
#d,e则是新开辟的内存单元，改变a并不会改变d,e
import copy
a=[1,2,3,4]
b=a
c=[]
c=a
d=a[:]
e=copy.copy(a)
b[0]=123
print(e)