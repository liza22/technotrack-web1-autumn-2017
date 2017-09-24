# -*- coding: utf-8 -*-
import socket
import os

def get_response(request):
    request = request.decode()
    type = request.split(' ', maxsplit=1)[0]
    path = request.split(' ', maxsplit=2)[1]
    
    files = os.listdir('./files')
    files_list = '\n'.join(files)

    if (type != "GET"):
        answer = "HTTP/1.1 405 Method Not Allowed\n\n"
    elif (path == '/'):
        user_agent = request.partition('User-Agent: ')[2]
        user_agent = user_agent.split('\n', maxsplit=1)[0]
        answer = "HTTP/1.1 200 OK\n\n" + "Hello mister!\nYou are: " + user_agent + "\n"
    elif (path == '/test/'):
        answer = "HTTP/1.1 200 OK\n\n"+request+'\n'
    elif (path.startswith('/media/')):
        file_name = path.partition('/media/')[2]
        if (file_name == ""):
            answer = 'HTTP/1.1 200 OK\n\n' + files_list + "\n"
        else:
            try:
                file = open('./files/' + file_name)
            except IOError:
                answer = 'HTTP/1.1 404 Not found\n\n' + "File not found\n"
            else:
                text = file.read()
                file.close()
                answer = 'HTTP/1.1 200 OK\n\n' + text + "\n"
    else:
        answer = 'HTTP/1.1 404 Not found\n\n' + 'Page not found\n'
    return answer.encode()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('localhost', 8000))  # связывание сокета с хостом и портом
server_socket.listen(0)  # устанавливаем прослушивание

print('Started')

while 1:
    try:
        (client_socket, address) = server_socket.accept()
        print('Got new client', client_socket.getsockname())  # Печатаем имя клиента(хост и порт)
        request_string = client_socket.recv(2048)  # получаем данные порциями по 2 Кб
        client_socket.send(get_response(request_string))  # отправляем клиенту ответ на запрос
        client_socket.close()
    except KeyboardInterrupt:  # если произошло прерывание с клавиатуры(Ctrl+C)
        print('Stopped')
        server_socket.close()  # закрываем соединение
        exit()
