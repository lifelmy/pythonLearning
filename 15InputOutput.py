'''
s='hello,world\n'
print(str(s))
print('s')
#  repr() 函数可以转义字符串中的特殊字符,把\n当成普通字符输出
print(repr(s))
print('s')
'''


#输出格式美化
'''
#rjust() 方法, 它可以将字符串靠右, 并在左边填充空格
for x in range(1,11):
    print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
    print(repr(x*x*x).rjust(4))

for x in range(1,11):
    print('{0:2d} {1:3d} {2:4d}'.format(x,x*x,x*x*x))

print()
#zfill(),位数不够会在前面加0，够了不做任何改变
print('12'.zfill(5))
print('-0.12'.zfill(8))
print('2.2556545'.zfill(5))

#format()的使用，按照参数的序号
print('这是第一个参数{0},这是第二个{1}'.format('hello','world'))
print('这是第二个参数{1},这是第一个{0}'.format('hello','world'))
#format()使用关键字输出
print('name={name} gener={gender}'.format(name='lmy',gender='male'))
#序号和关键字的组合
print('序号和关键字组合{0},{1},{love}'.format('吴哥窟','童话镇',love='lr'))


#使用‘:’可以更好的格式化数字
import math
print('{0:.3f}'.format(math.pi))#三位小数
print('%d'%123456)

#通过变量名取值
table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
print('Runoob: {0[Runoob]:3d}; Google: {0[Google]:3d}; Taobao: {0[Taobao]:3d}'.format(table))

#传统的数据格式化，但是推荐使用format()
print('常量PI的近似值是%5.3f'%math.pi)

'''


'''
#读取键盘输入
s=input('请输入。。。\n')
print(str(s))
'''

'''
#读写文件 open(filename, mode)  第一个是文件，第二个是读写模式
f=open('E:/Python/test.txt','w+')
f.write('whoami')
f.close()
'''

'''
#read()函数
f=open('E:/Python/test.txt','r')
content=f.read()
print(content)
f.close()
'''

'''
#readline()函数
f=open('E:/Python/test.txt','r')
s1=f.readline()
print(s1)
s2=f.readline()
print(s2)
s3=f.readline()
print(s3)
f.close()
'''

'''
#readlines()函数
f=open('E:/Python/test.txt','r')
s=f.readlines()
print(s)
for x in s:
    print(str(x),end='')
f.close()
'''

'''
#write()写入函数返回写入的字符数
f=open('E:/Python/test.txt','w')
num=f.write('python is a very goog language')
print(num)
f.close()
'''

'''
#要写入的东西不是字符串，先转换
value={'name':'lmy','gender':'male'}
f=open('E:/Python/test.txt','w')
s=str(value)
f.write(s)
print(f.tell())
f.close()
'''

'''
#改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数
#from_what 的值,  0 表示开头, 1 表示当前位置, 2 表示文件的结尾
#seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
f=open('E:/Python/test.txt','wb+')
num=f.write(b'0123456789abcdef')
print(num)
f.seek(5)
s1=f.read(1)
print(s1)
f.seek(-3,2)
s2=f.read(1)
print(s2)
f.close()
'''




#Pickle用于将数据序列化和反序列化
#通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
#通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
'''
import pickle
data1 = {'a': [222, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}
selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('E:/Python/data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()
'''

'''
#pprint 用于打印 Python 数据结构  输出格式比较美观
import pprint, pickle
pkl_file = open('E:/Python/data.pkl', 'rb')
data1 = pickle.load(pkl_file)
pprint.pprint(data1)
data2 = pickle.load(pkl_file)
pprint.pprint(data2)
pkl_file.close()
'''






