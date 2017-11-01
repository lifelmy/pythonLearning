'''
#把list当作堆栈使用，后进先出
stack=[2,5,6,8]
stack.append(9)
stack.append(10)
print(stack)
print(stack.pop())
'''

'''
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
for weapon in freshfruit:
    print( weapon.strip())
'''
'''
#删除list中的元素
list=[1,2,3,4,5]
del list[2:4]
print(list)
'''

'''
#列表和元组的嵌套使用
list=[1,2,3]
list2=[list,[4,5,6]]
print(list2)
print(list2[0][0])
t=('hello','world',1,2,3,4)
u=(t,(5,6,7))
print(u)
'''

'''
#字典的基本操作

student={'name':'lmy','gender':'male'}
#新增键值对
student['age']=22
print(student)
#根据键修改值
student['name']='lifelmy'
print(student)
#获取值的集合
for x in student.values():
    print(x)
#遍历items
for k,v in student.items():
    print(k,v)

#使用enumerate()函数可以获取位置和值
list=[111,222,333]
for x,v in enumerate(list):
    print(x,v)

for x,v in enumerate(student):
    print(x,v,student[v])

'''

'''
#同时遍历两个列表，使用zip()组合
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    print('what is your %s ? It is %s'%(q,a))
'''












