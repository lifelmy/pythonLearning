from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
import queue,random,time
class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器
server_addr='127.0.0.1'
print('Connet to server %s'%server_addr)
m=QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()
task=m.get_task_queue()
result=m.get_result_queue()

for i in range(10):
    try:
        n=task.get(timeout=1)
        print('run task %d *%d'%(n,n))
        time.sleep(1)
        r=n*n
        result.put(r)
    except queue.Empty:
        print('task queue is empty')
print('worker exit.')
