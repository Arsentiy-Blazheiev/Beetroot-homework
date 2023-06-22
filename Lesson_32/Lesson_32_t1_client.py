# На уроці ми створили сервер і клієнт, які використовують протокол TCP/IP для зв'язку через сокети.
# У цьому завданні вам потрібно створити сервер і клієнт,
# які будуть використовувати для зв'язку протокол користувацьких дейтаграм (UDP).

import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = b"hello, server!"

sock.sendto(msg, (UDP_IP, UDP_PORT))

data, addr = sock.recvfrom(1024)

print("Відповідь:", data)
print("Сервер:", addr)
