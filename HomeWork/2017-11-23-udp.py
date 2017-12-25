#udp服务器端
import socket,threading
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',9999))
def handle(data,add):
    print(data.decode('utf-8'))
while True:
    data,address=s.recvfrom(1024)
    t=threading.Thread(target=handle,args=(data,address))
    t.start()