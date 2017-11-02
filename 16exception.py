
#使用try和except来处理异常
'''
def fail():
    i=1/0

def main():
    try:
        fail()
    except ZeroDivisionError as err:
        print("出错了",err)
main()

'''

#抛出异常，它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）
#raise NameError('HiThere')
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
'''


'''
#自定义的异常
class MyError(Exception):
    def __init__(self,value):
        self.value=value

    def __str__(self) :
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as err:
    print('出错了，错误信息是',err.value)
'''


#预定义的清理行为

#当执行完毕后，文件会保持打开状态，并没有被关闭。
for line in open('E:/Python/test.txt','r'):
    print(line.strip())

print('-------------------------')
#关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with  open('E:/Python/test.txt','r') as f:
    for line in f:
        print(line.strip())