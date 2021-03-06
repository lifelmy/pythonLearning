from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
import queue,random,time
task_queue=queue.Queue()
result_queue=queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass


#win7 64 貌似不支持callable下调用匿名函数lambda，这里封装一下
def return_task_queue():
    global task_queue
    return task_queue
def return_result_queue():
    global result_queue
    return result_queue

def test():
    #把两个Queue都注册到网络上，callable参数关联了Queue对象
    QueueManager.register('get_task_queue',callable=return_task_queue)
    QueueManager.register('get_result_queue',callable=return_result_queue)
    #绑定端口5000，设置验证码‘abc’
    manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    #启动Queue
    manager.start()
    #获得通过网络访问的Queue对象
    task=manager.get_task_queue()
    result=manager.get_result_queue()
    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')

if __name__=="__main__":
    freeze_support()
    test()