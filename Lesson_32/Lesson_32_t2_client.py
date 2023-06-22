# Розширити ехо-сервер, який повертає клієнту дані,
# зашифровані за допомогою алгоритму шифру Цезаря певним ключем, отриманим від клієнта.

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
key = "1"
msg = key.encode()

sock.sendto(msg, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)

print("Відповідь:", data.decode())
print("Сервер:", addr)
