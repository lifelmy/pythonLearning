'''
#使用线程
import threading,time
def loop():
    print('current thread name is ',threading.current_thread().name)
    for n in range(5):
        print('%s >> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('%s end'%(threading.current_thread().name))

if __name__=="__main__":
    print(threading.current_thread().name,'start')
    t=threading.Thread(target=loop,name='LoopThread')
    t.start()
    t.join()
    print(threading.current_thread().name, 'end')
'''

'''
#使用多线程，对互斥操作加锁
import threading
balance=0
lock = threading.Lock()
def change(n):
    global balance
    balance+=n
    balance-=n
def threadRun(n):
    for i in range(100000):
        lock.acquire()
        try:
            change(n)
        finally:
            lock.release()
if __name__=="__main__":
    thread1=threading.Thread(target=threadRun,args=(5,))
    thread2=threading.Thread(target=threadRun,args=(8,))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print(balance)
'''
#一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。
# ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
#ThreadLocal类似于一个dict,根据当前线程的id保存变量，取出的时候根据id再取出
import threading

school=threading.local()

def showName():
    # 获取当前线程关联的student:
    print(school.student)

def save(name):
    # 绑定ThreadLocal的student:
    school.student=name
    showName()

if __name__=="__main__":
    thread1=threading.Thread(target=save,args=('lmy',))
    thread2 = threading.Thread(target=save, args=('lr',))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

















