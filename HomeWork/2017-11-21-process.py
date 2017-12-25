'''
#Process类来代表一个进程对象,使用Process创建一个进程
from multiprocessing import Process
import os
def doSome(p):
    print('子进程总要输出点什么',p)
    print(os.getpid())

if __name__=='__main__':
    print(os.getpid())
    p=Process(target=doSome,args=('hello',))
    p.start()
    #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('child process end')
'''

'''
#创建和使用线程池
from multiprocessing import Pool
import time,os,random
def long_time_work(i):
    print('进程%s开始工作了'%(i))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('进程%s工作结束了,用时%0.2f seconds' % (i,end-start))
if __name__=='__main__':
    p=Pool(8)
    for i in range(10):
        p.apply_async(long_time_work(i))
    p.close()
    p.join()
'''

from multiprocessing import Queue,Process
import random,os,time
def write(obj):
    for x in range(5):
        print('put',x)
        obj.put(x)
        time.sleep(random.random()*3)
def get(obj):
    while(True):
        if obj.qsize()>0:
            value=obj.get()
            print('pop',value)

if __name__=="__main__":
    q=Queue()
    push=Process(target=write,args=(q,))
    pop=Process(target=get,args=(q,))
    push.start()
    pop.start()
    push.join()
    pop.terminate()















