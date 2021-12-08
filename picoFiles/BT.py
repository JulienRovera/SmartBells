from machine import Pin,UART

uart = UART(0,9600)

LedGPIO = 16
led = Pin(LedGPIO, Pin.OUT)
while True:
    # print('checking BT')
    if uart.any():
        command = uart.readline()
        print(command)