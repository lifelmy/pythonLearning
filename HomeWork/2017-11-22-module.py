'''
#datetime
from datetime import datetime
#获取当前时间
now=datetime.now()
print(now)
print(type(now))

#构造时间
date=datetime(2017,12,30,0,0,0)

#时间与时间戳互相转换
stamp=date.timestamp()
stamp2Date=datetime.fromtimestamp(stamp)
print(stamp)
print(stamp2Date)


#str转换为datetime
#第一个参数是字符串日期，第二个参数是当前字符串的格式，通过这两个参数转换为datatime
str2DateTime=datetime.strptime('2017/11/22 11:28:00','%Y/%m/%d %H:%M:%S')
print(type(str2DateTime))
print(str2DateTime)

#datetime转换为str
#第一个参数是datetime格式的时间，第二个参数是你要转换成字符串的格式
#https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior
#网址是日期和时间格式等含义
datetime2Str=datetime.strftime(now,'%Y-%m-%d %H-%M-%S  %A   %B')
print(datetime2Str)
'''

'''
#datetime的加减
from datetime import datetime,timedelta
import time
now=datetime.now()
print(now)
after1=now+timedelta(hours=1)
after2=now+timedelta(days=1,hours=2,minutes=10)
#不支持两个datetime直接相加
#after3=now+after2
print(after1)
print(after2)
'''

'''
#时区转换
from datetime import datetime,timedelta,timezone
# 拿到UTC时间，并强制设置时区为UTC+0:00:
utc_bt=datetime.utcnow().replace(tzinfo=timezone.utc)
print(utc_bt)
# astimezone()将转换时区为北京时间:
bj_dt=utc_bt.astimezone(timezone(timedelta(hours=8)))
print(bj_dt)
# astimezone()将转换时区为东京时间:

tokyo_dt=utc_bt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt)
# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2=bj_dt.astimezone(timezone(timedelta(hours=9)))
print(tokyo_dt2)
'''

'''
#HomeWork
import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    s= re.match(r'UTC([\-\+\s:][0-9]+):[0-9]{2}',tz_str)
    hour=int(s.group(1))
    time=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    previous=time.replace(tzinfo=timezone(timedelta(hours=hour)))
    stamp=previous.timestamp()
    return stamp
to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
'''




#------------------------collections--------------------------

'''
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数,并可以用属性而不是索引来引用tuple的某个元素。
#这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p=Point(10,20)
print(p)
print(p.x)
Circle=namedtuple('Circle',['x','y','r'])
c=Circle(0,0,5)
print(c)
'''

'''
#deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q=deque(['a','b','c'])
q.append('d')
q.appendleft(0)
q.pop()
q.popleft()
q.insert(2,'f')
q.reverse()
print(q)
'''

'''
#使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict
from collections import defaultdict

d=defaultdict(lambda :'NA')
d['love']='her'
print(d['love'])
print(d['hate'])

'''

'''
#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序
from collections import OrderedDict
ordinary=dict([('a',1),('b',2),('c',3),('f',4),('d',5)])
ordinary['e']=10
print(ordinary)
orderDict=OrderedDict([('a',1),('b',2),('c',3),('f',4),('d',5)])
print(orderDict)
'''

'''
#Counter是一个简单的计数器，例如，统计字符出现的个数
from collections import Counter
c=Counter()
for ch in 'collections':
    c[ch]=c[ch]+1
print(c)
'''

#--------------------Base64----------------------------

'''
import base64
en=base64.b64encode(b'abcd')
de=base64.b64decode(en)
print(en)
print(de)
#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，
# 所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：
en2=base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(en2)
safeEncode=base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(safeEncode)
'''

'''
#HomeWork
import base64
def safe_base64_decode(s):
    length=len(s)%4
    if(length==0):
        pass
    else:
        s=s+(b'='*(4-length))
        # print(s)
    return base64.standard_b64decode(s)
print(safe_base64_decode(b'YWJjZA'))
print(safe_base64_decode(b'YWJjZA=='))
'''

'''
#------------------------struct------------------------------
#struct的pack函数把任意数据类型变成bytes
#>表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
import struct
s=struct.pack('<I',123456)
print(s)
#根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
s2=struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(s2)
'''

#-------------------hashlib--------------------------------
'''
#md5
import hashlib
md5=hashlib.md5()
md5.update('hello'.encode('utf-8'))
print(md5.hexdigest())
'''

'''
#HomeWork
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    md5=hashlib.md5()
    md5.update(password.encode('utf-8'))
    str=md5.hexdigest()
    if db[user]==str:
        return True
    return False

if __name__=='__main__':
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')
'''

'''
#HomeWork
import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    p=password+user.salt
    if get_md5(p)==user.password:
        return True
    else:
        return False

if __name__=='__main__':
    # 测试:
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')
'''

'''
#hmac方法省去了我们自己加盐的过程
#  Keyed-Hashing for Message Authentication。它通过一个标准算法，在计算哈希的过程中，把key混入计算过程中
import hashlib, random,hmac

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    key=user.key
    if hmac_md5(key,password)==user.password:
        return True
    else:
        return False

if __name__=='__main__':
    # 测试:
    assert login('michael', '123456')
    assert login('bob', 'abc999')
    assert login('alice', 'alice2008')
    assert not login('michael', '1234567')
    assert not login('bob', '123456')
    assert not login('alice', 'Alice2008')
    print('ok')
'''




















