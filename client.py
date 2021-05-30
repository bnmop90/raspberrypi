import socket
import time
import datetime as dt
import serial

ser = serial.Serial("/dev/ttyUSB0", 9600, timeout = 1)

server_ip = 'localhost'
server_port = 5555
size =1024
server_addr = (server_ip, server_port)
#socket.send('HELLO'.encode())
        
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect(server_addr)
        client_socket.send('hi'.encode())
        x = dt.datetime.now()
        msg = client_socket.recv(size)
        serial_value = ser.readline().decode()
        print(serial_value)
        print(f'{msg.decode()}')
        time.sleep(0.1)
        client_socket.close()
