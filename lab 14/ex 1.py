import socket
import threading
import sys
import gzip


def listener(sock):  # функция для принятия сообщений
    while sock.fileno() != -1:
        data = sock.recv(1000)
        if len(data) > 0:
            try:
                print(gzip.decompress(data).decode())
            except Exception:
                print(data.decode())


sock = socket.socket()  # Создаём сокет
sock.connect(('81.200.31.248', 9000))  # Соединяемся

threads = [threading.Thread(target=listener, args=(sock,))]  # запускаем пассивное прослушивание входящих сообщений
for thread in threads:
    thread.start()
while True:  # отправка сообщений серверу
    out = input()
    if out == 'exit':  # выход из цикла
        break
    if out == 'z':  # вариант ввода если вам нужно архивировать отправляемое сообщение (это нужно для задач начиная со второго)
        print('zipping: ', end='')
        out = input()
        sock.send(gzip.compress(out.encode()))
    else:  # простой ввод сообщения без архивирования
        sock.send(out.encode())
