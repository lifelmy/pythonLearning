'''
import sys
print('命令行参数如下')
for x in sys.argv:
    print(x)
print('sys的路径为',sys.path)
'''


#导入自定义的模块
import hello
hello.function('lmy')


