import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8080))
server.listen(1)
print('서버가 클라이언트의 연결 요청을 기다리고 있습니다.')

connection, address = server.accept()
print('소캣 서버 연결')

data = connection.recv(1024)

print(data.decode())

connection.sendall(b'Hello, Client!')

connection.close()
server.close()