import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 8080))
print('연결되었습니다.')

client.sendall(b'Hello, Server!')
data = client.recv(1024)
print(data.decode())

client.close()