#udp客户端
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.connect(('127.0.0.1',9999))
s.send('hello'.encode('utf-8'))

