#创建字典
dict1={'name':'lmy','age':22,'gender':'male',112:112}
print(dict1['name'])
print(dict1[112])

#修改字典的数据
dict1['name']='life'
print(dict1)

#删除字典中的数据
del dict1[112]
print(dict1)

#清空字典
#dict1.clear()
#print(dict1)

#删除字典
#del dict1

print(str(dict1))

#判断键是否在在字典中
print('name' in  dict1)

print(dict1.keys())
