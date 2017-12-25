'''
with open('E:/123.txt','r') as f :
    s=f.read(10)
    while(s):
        print(s.strip())
        s=f.read(5)
'''

'''
#文本复制
oldFile=input()
position=oldFile.rfind('.')
newFileFront=oldFile[0:position]+'复件'
newFileSuffix=oldFile[position:]
print(newFileFront)
print(newFileSuffix)
newName=newFileFront+newFileSuffixs
print(newName)
with open('E:/'+oldFile,'r') as f :
    with open('E:/'+newName,'w+') as p :
        s = f.read(1024)
        while (s):
            print(s)
            p.write(s)
            s = f.read(1024)

'''


'''
import os
print(os.name)
#print(os.environ)
print(os.path.abspath('.'))
os.mkdir('E:/123')
os.rmdir('E:/123')
#连接两个路径
path=os.path.join('E:\Python\pythonLearning','123.txt')
print('path=%s'%path)
#拆分路径
splitPath=os.path.split(path)
print('拆分后的路径为',splitPath)
#直接得到后缀名
suffix=os.path.splitext(path)
print('后缀名=',suffix[1])
'''

'''
import os
#print(os.path.abspath('.'))
#重命名文件
#os.rename('E:/123.txt','E:/2.txt')
root='E:/'
for x in os.listdir(root):
    #判断是文件还是文件夹时，需要使用绝对路径，不能使用相对路径，不然一直返回False
    x=os.path.join(root,x)
    if os.path.isdir(x):
        print('文件夹',x)
    if os.path.isfile(x):
        print('文件',x)
'''

'''
import  os
for x in os.listdir('.'):
    print(x)
    if os.path.isfile(x) and os.path.splitext(x)[1]=='.py':
        print(x)
'''

'''
#在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件
import os
def search(path,name):
    for x in os.listdir(path):
        x=os.path.join(path,x)
        if os.path.isdir(x):
            search(x,name)
        if os.path.isfile(x):
            fileName=os.path.split(x)[1]
            if(name in fileName):
                print(x)
path='E:\Python'
name='re'
search(path,name)
'''