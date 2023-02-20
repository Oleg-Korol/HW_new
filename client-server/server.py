import socket
import  sys

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5678

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
srv_sock.bind((SERVER_HOST,SERVER_PORT))
srv_sock.listen(1000)

try:
    while True:
        client, address =srv_sock.accept()
        data = client.recv(2**16)
        print(data.decode("utf-8"))
        print(client,address)
        client.send( b"Hello, " + data )
        client.close()
except  KeyboardInterrupt:
    srv_sock.close()
    print(end="\r")
    sys.exit()
