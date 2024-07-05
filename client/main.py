"""Тестовий клієнт для сервера"""


import socket
import chiper


connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_socket.connect(("127.0.0.1", 5555))
key = connection_socket.recv(1024)
key = chiper.loads(key)
key = chiper.Chiper(key)
connection_socket.send(key.encrypt({"type": "client_ok"}))
data = connection_socket.recv(1024)
data = key.decrypt(data)
print(data)