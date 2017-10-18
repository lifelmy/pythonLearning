'''
#创建元组
tup1=('google','baidu','sougou')
print(tup1)
print(tup1[1])

#元组只有一个元素时，需要加上逗号
tup2=(2)
tup3=(2,)
print(type(tup2))   #<class 'int'>
print(type(tup3))   #<class 'tuple'>

#删除元组
del tup1
'''

#元组中的元素不能修改和删除，但是可以对多个元组连接
tup1=(1,2,3)
tup2=(4,5)
#tup1[0]=0  #这个代码会报错，不允许更改
tup3=tup1+tup2
print(tup3)

print(max(tup1))
print(min(tup1))









