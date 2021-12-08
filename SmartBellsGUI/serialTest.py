import serial

serial_port = serial.Serial(port = "COM5", baudrate = 9600, parity = serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)
serial_port.flushInput()
while 1 == 1:
	print(serial_port.readline().decode())
	
serial_port.close()