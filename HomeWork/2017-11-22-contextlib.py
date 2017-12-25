
'''
#任何对象，只要正确实现了上下文管理，就可以用于with语句
#实现上下文管理是通过__enter__和__exit__这两个方法实现的
class Student(object):
    def __init__(self,name):
        self.name=name
    def __enter__(self):
        #如果指定了as variable说明符，则variable是上下文管理器expression调用__enter__()函数返回的对象
        #因此该方法要返回as 的对象
        print('entry')
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
    def show(self):
        print(self.name)

with Student('hello') as stu:
    stu.show()
'''


'''
#@contextmanager这个decorator接受一个generator，用yield语句把with ... as var把变量输出出去，
# 然后，with语句就可以正常地工作了
from contextlib import contextmanager
class Student(object):
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

@contextmanager
def createStudent(name):
    print('start')
    stu=Student(name)
    yield stu
    print('end')

with createStudent('lmy') as s:
    s.show()
'''

'''
#使用@contextmanager之后，先执行yield之前的代码，然后会执行with语句内部的所有语句，最后执行yield之后的语句
#使用@contextmanager
from contextlib import contextmanager
@contextmanager
def test():
    print('<h1>')
    yield
    print('<h1>')

with test() :
    print('hello')
    print('world')
'''


#如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。
from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('http://www.baidu.com'))as t:
    for x in t:
        print(x)















