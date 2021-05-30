import wiringpi
import time

SCE = 22
CHANNEL = 0
SPEED = 1000000
MODE = 3
OBJECT = 0xA0
SENSOR = 0xA1

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(SCE, 1)
wiringpi.wiringPiSPISetup(CHANNEL, SPEED)
wiringpi.delay(500)

def spi_command(x):
    data = [0] * 3
    data[0] = x
    data[1] = 0x22
    data[2] = 0x22
    wiringpi.digitalWrite(SCE, 0)
    
    for i in data:
        print(i)
        wiringpi.delayMicroseconds(10)
        retlen, retdata = wiringpi.wiringPiSPIDataRW(CHANNEL, i)

    wiringpi.delayMicroseconds(10)
    wiringpi.digitalWrite(SCE, 1)

while True:
    spi_command(SENSOR)


