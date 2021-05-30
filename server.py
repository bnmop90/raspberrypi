import socket

ip = 'localhost'
port = 5555
size = 1024
addr = (ip, port)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(addr)
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()

        msg = client_socket.recv(size)

        print(msg)

        client_socket.sendall('welcome'.encode())
        client_socket.close()


