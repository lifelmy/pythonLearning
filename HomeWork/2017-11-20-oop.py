#面向对象高级

'''
class Animal():
    def run(self):
        print('running')

class Dog(Animal):
    def run(self):
        print('dog is running')

class Cat(Animal):
    def run(self):
        print('cat is running')

class Timer(object):
    def run(self):
        print('Start...')

def test(animal):
    animal.run()
#因为test()中的参数没有指定类型，只要对象中有run方法就可以调用test()方法，这就是动态语言的特点
#而Java要想调用，必须是Animal对象。
test(Timer())
'''

'''
#如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir('ABC'))

print(isinstance(dir('ABC'),list))

print(type(dir('ABC')) )

#len()函数实际上调用的也是__len()__
len('ABC')
'''

'''
#使用python中的内置函数hasattr(object,attrName)判断对象有没有给定的属性和方法
#使用 setattr(obj,'y',111)为一个对象设置一个属性
#使用getattr(obj,'y')获取对象的属性,可以传入一个default参数，如果属性不存在，就返回默认值。如name
class Timer(object):
    def run(self):
        print('Start...')

def test(obj):
    if hasattr(obj,'run'):
         obj.run()
    else:
        print('没有该属性')
    setattr(obj,'y',111)
    print(getattr(obj,'y'))
    print(getattr(obj,'name','404'))
test(Timer())
'''


'''
#类变量
class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        # self.__class__.count+=1
        Student.count+=1
print(Student.count)
bart = Student('Bart')
cat=Student('cat')
print(Student.count)
'''



'''
#动态的给类绑定方法，这个方法对所有的实例都起作用
class Student():
    pass

def say(self):
    print('haha')
#添加方法
Student.say=say
#为类添加一个属性
Student.gender='male'
s=Student()
s.say()
print(s.gender)
s2=Student()
s2.say()
s2.gender='female'
print(s2.gender)

#动态的为对象绑定方法，但是该方法只对该对象起作用，对其它对象不起作用
def setAge(self,age):
    self.age=age
from types import MethodType
s.setAge=MethodType(setAge,s)
s.setAge(11)
print(s.age)
'''


'''
#要想限制类的属性，使用__slot__方法限制,只允许属性，添加其它属性会报错
#__slot__只对该类起作用，对于继承的子类不起作用
class Student():
    __slots__ = ('name','age')
s=Student()
s.name='lucy'
s.age=19

class JuiorStudent(Student):
    pass

js=JuiorStudent()
js.gender='male'
print(js.gender)
'''

'''
class Student():
    def get_score(self):
        return self._score
    def set_score(self,value):
        if not isinstance(value,int):
            print('格式不对')
        elif (value<0 or value>100):
            print('数字不对')
        else:
            self._score=value
s=Student()
s.set_score(20)
print(s.get_score())

'''

'''
#Python内置的@property装饰器就是负责把一个方法变成属性调用，比上面的调用简单些
class Student():
    @property
    def score(self):
        return self._score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            print('格式不对')
        elif (value<0 or value>100):
            print('数字不对')
        else:
            self._score=value
s=Student()
s.score=10
print(s.score)
'''


'''
#HomeWork
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,w):
        self.__width=w

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        self.__height = h

    @property
    def resolution(self):
        return self.__width*self.__height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')
'''

'''
#在命令行不使用print打印s，调用的是__repr__()
#__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
class Student():
    def __init__(self):
        self.__name='hello'
    def __str__(self):
        return 'my name is %s'%self.__name
    __repr__=__str__
s=Student()
print(s)
'''

'''
#如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
# 该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环
class Fib():
    def __init__(self):
        self.a=0
        self.b=1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if(self.a>1000):
            raise StopIteration
        return self.a
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
#要实现切片，需要判断传入的是下标还是切片
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
    #可以在对象身上调用
    def __call__(self, *args, **kwargs):
        return '调用自己'
for n in Fib():
    print(n)
print(Fib()[5])
print(Fib()[:10])
f=Fib()
print(f())
'''

'''
#枚举类型
#枚举类型成员名称不允许重复，如果定义red=2会报错
# 默认情况下，不同的成员值允许相同。但是两个相同值的成员，第二个成员的名称被视作第一个成员的别名　
#如果要限制定义枚举时，不能定义相同值的成员。可以使用装饰器@unique【要导入unique模块】
from enum import Enum,unique
@unique
class Color(Enum):
    red = 1
   # hehe=1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7
#通过成员值取成员
print(Color(1))
#通过成员的名称来获取成员
print(Color['red'])
#通过成员，来获取它的名称和值
a=Color.red
print(a.name)
print(a.value)
#遍历
for color in Color:
    print(color)
#可以比较，但是不能比较大小
print(color.red is color.red)
print(color.red is color.blue)
#print(color.red > color.blue)  不能比较大小
'''

'''
#type()函数可以查看一个类型或变量的类型
#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数
#type()函数既可以返回一个对象的类型，又可以创建出新的类型,下一个例子创建使用type()创建类
class Hello:
    pass
print(type(Hello))  #<class 'type'>

hello=Hello()
print(type(hello))  #<class '__main__.Hello'>
'''



'''
#由于python是动态语言，我们可以动态的创建类
def fn(self):
    print('hello world')
#第一个参数是类的名称，第二个是一个元组，表示要继承的类，元组只有一个的时候的写法要加一个逗号
#第三个参数是一个字典，表示在该类中你定义的方法叫什么名字
Hello=type('Hello',(object,),dict(hello=fn))
h=Hello()
h.hello()
'''


'''
def foo(s):
    n = int(s)
    if n==0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n

def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise

bar()
'''

'''
#使用断言，断言的意思是断定此时该变量不会为0，否则接下来不能继续运行
#assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
def foo(n):
    n=int(n)
    assert n!=0,'n is not zero'
    return 10/n
def bar(n):
    foo(n)
bar(0)
'''


'''
#单元测试作业
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score<0 or self.score>100:
            raise ValueError
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        return 'C'
'''














