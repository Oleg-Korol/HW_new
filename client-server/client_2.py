import socket
import sys
import time

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5678

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_HOST, SERVER_PORT))

message_in = sys.stdin
message_out = sys.stdout

while True:
    try:
        for mes in message_in:
            sock.sendall(mes.encode('utf-8'))    #отправка данных в сокет
            data = sock.recv(2048)               #получение данных из сокета
            message = data.decode('utf-8')
            for mesg in message:
                   message_out.flush()
                   time.sleep(0.5)
                   message_out.write(mesg)


    except KeyboardInterrupt:
        sock.close()
        sys.exit()


# падает по:
# ConnectionAbortedError: [WinError 10053] Программа на вашем хост-компьютере разорвала установленное подключение