

#简单输出
print('hello World')
print('世界你好')
#变量赋值
a=100
b=2
c=a+b
print(c)
#将一个代码写成多行，使用'\'
d=a\
    +b+\
        c
print(d)


#这是一个注释
'''
这是多行注释
这是多行注释这是多行注释
这是多行注释这是多行注释
'''

#对于字符串，使用单引号和双引号都可以，三引号可以将输入多行字符串
'''
word='字符串'
sentence="这是一个句子"
paragraph="""可以多行
            输入
            段落"""
print(paragraph)
'''


#使用imput来获取用户输入
#print("等待用户输入-------》");
#input("\n\nPress the enter key to exit.")


#同一行显示多条语句，使用分号分割
#import sys;x='runoob';sys.stdout.write(x+'\n')


'''
#实现print的不换行输出
print('..................')
x='a'
#print实现不换行功能，在后面加上end=""  这样下一个输出就会和上一个输出在同一行
print(x,end="")
print('不换行')
print('上一个不加，该行就会另起一行')
'''



'''
import 与 from...import
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''

#sys.argv[0]表示代码本身文件路径
#该示例导入sys模块
'''
import sys
print('=========================Python import mode==================================')
print('命令参数为：')
for i in sys.argv :
    print(i)
print('\n python路径为',sys.path)
'''

#该示例导入sys模块中的argv和path
'''
from sys import argv,path
print('=========================Python import mode==================================')
for i in argv:
    print(i)
print(path)
'''




















