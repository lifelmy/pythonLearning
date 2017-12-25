'''
from urllib import request
import json
with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
    data=f.read()
    print('Status',f.status,f.reason)
    #将字节转为字符串
    s=data.decode('utf-8')
    #将字符串转为
    j=json.loads(s)
    print(type(j))
    for k,v in f.getheaders():
        print(k,':',v)
'''

'''
#如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器
from urllib import request
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))

'''

'''
#Post请求

from urllib import request,parse

email=input('email:')
password=input('password')
login_data=parse.urlencode(
    [
        ('username',email),
        ('password',password),
        ('entry','mweibo'),
        ('client_id',''),
        ('savestate','1'),
        ('ec',''),
        ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F'),
    ]
)
req=request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('status',f.status,f.reason)
    for k,v in f.getheaders():
        print(k,':',v)
'''

