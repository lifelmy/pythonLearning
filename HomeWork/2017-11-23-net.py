'''
import socket
#AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
#SOCK_STREAM指定使用面向流的TCP协议
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#参数是一个tuple，包含地址和端口号
s.connect(('www.sina.com.cn',80))
# 发送数据:
s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
buff=[]
while True:
    d=s.recv(1024)
    if d:
        buff.append(d)
    else:
        break
data=b''.join(buff)
s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
# 把接收的数据写入文件:
with open('E:/sina.html', 'wb') as f:
    f.write(html)
'''

import socket,threading,time
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('127.0.0.1',9999))
server.listen(5)
print('Waiting for connection ')

def handler(socket,address):
    print('accept socket connection from %s %s'%address)
    socket.send('welcome'.encode('utf-8'))
    while True:
        data=socket.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8')=='exit':
            break
        socket.send(('hello %s'%data.decode('utf-8')).encode('utf-8'))
    socket.close()
    print('connection from  is closed')

while True:
    sock, addr=server.accept()
    t=threading.Thread(target=handler,args=(sock,addr))
    print(addr)
    t.start()


