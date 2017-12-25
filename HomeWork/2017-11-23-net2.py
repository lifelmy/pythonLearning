import socket
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('127.0.0.1',9999))
print(client.recv(1024).decode('utf-8'))
for data in ['1','2','3']:
    client.send(data.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))
client.send('exit'.encode('utf-8'))
client.close()