import socket

def connect_client(host, port):
  server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  server.bind((host, port))


