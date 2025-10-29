import socket

HOST = '192.168.10.57'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto(b"Hello, SErver!", (HOST, PORT))

data, addr = client.recvfrom(1024)
print(f"서버로부터 받은 메시지: {data.decode()}")