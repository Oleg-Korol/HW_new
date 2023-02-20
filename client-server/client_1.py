import socket


SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5678

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_HOST,SERVER_PORT))
name = input("Введите свое имя:")

sock.send(name.encode())
responce = sock.recv(2**16)

print(responce.decode("utf-8"))