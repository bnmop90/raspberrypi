import spidev
import wiringpi
import socket

ip = 'localhost'
port = 5585
size =1024
addr = (ip, port)

obj = 0xA0
sen = 0xA1

spi = spidev.SpiDev()
spi.open(0, 0)
spi.mode = 3
spi.max_speed_hz = 1000000

wiringpi.wiringPiSetup()
wiringpi.pinMode(22, 1)
wiringpi.wiringPiSPISetup(0, 1000000)
wiringpi.delay(500)

def spi_command(x):
    d = [x, 0x22, 0x22]
    
    print(d)
    
    wiringpi.pinMode(22, 0)
    wiringpi.delayMicroseconds(10)
    d[0] = spi.xfer2([d[0]])
    wiringpi.delayMicroseconds(10)
    d[1] = spi.xfer2([d[1]])
    wiringpi.delayMicroseconds(10)
    d[2] = spi.xfer2([d[2]])
    wiringpi.delayMicroseconds(10)
    wiringpi.pinMode(22, 1)
    #print((c[0]*256)+a[0])a
    #print(d)

    return d[2][0]*256 + d[1][0]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind(addr)
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()

        msg = client_socket.recv(size)

        sen_res = spi_command(sen)
        wiringpi.delayMicroseconds(10)
        
        obj_res = spi_command(obj)
        wiringpi.delay(500)
        
        sensor_data, object_data  = float(sen_res)/100, float(obj_res)/100
        
        client_socket.sendall(f'{sensor_data} {object_data}'.encode())
        client_socket.close()

spi.close()

