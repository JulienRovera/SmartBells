from datetime import datetime
import pandas as pd
import serial
import time
import threading

class Session:
	def __init__(self, filePath):
		self.filePath = filePath
		self.time = 0.0
		self.reps = 0
		self.date = datetime.today().strftime('%Y-%m-%d')


class ViewModel:
	testButtonText = "Clear Graph"
	isRecording = False
	numSessions = 0
	x_acc = []
	y_acc = []
	z_acc = []
	x_rot = []
	y_rot = []
	z_rot = []
	time = []
	timeCounter = 0
	def __init__(self):
		self.displayedDetails = -1
		self.sessionsList = []

	def beginRecording(self):
		self.numSessions += 1
		self.isRecording = True
		#while(self.isRecording):
			#print("test")
		self.readThread = threading.Thread(target = self.readData)
		self.readThread.start()

	def stopRecording(self):
		#data.to_csv('C:/Users/julie/Desktop/data.csv', header = ['x_acc', 'y_acc','z_acc','x_rot','y_rot','z_rot',])
		self.isRecording = False
		self.readThread.join()
		#newSessionFilePath = "session" + str(self.numSessions) + ".csv"
		#sessionData = pd.read_csv('data.txt', header = None)
		#sessionData.to_csv(newSessionFilePath, header = ['x_acc', 'y_acc','z_acc','x_rot','y_rot','z_rot', 'x_mag','y_mag', 'z_mag'])
		#print(self.newSessionFilePath)
		self.createSession(self.newSessionFilePath)

	def readData(self):
		self.x_acc = []
		self.y_acc = []
		self.z_acc = []
		self.x_rot = []
		self.y_rot = []
		self.z_rot = []
		self.x_mag = []
		self.y_mag = []
		self.z_mag = []
		self.time = []
		self.timeCounter = 0.0
		self.newSessionFilePath = "session" + str(self.numSessions) + ".txt"
		tempFile = open(self.newSessionFilePath, 'w')
		self.serial_port = serial.Serial(port = "COM5", baudrate = 9600, parity = serial.PARITY_EVEN, stopbits=serial.STOPBITS_ONE)
		self.serial_port.flushInput()
		self.serial_port.readline().decode()
		while(self.isRecording):
			#print(self.serial_port.readline().decode())\
			nextLine = self.serial_port.readline().decode()
			nextLineValues = nextLine.split(",")
			self.x_rot.append(float(nextLineValues[0]))
			self.y_rot.append(float(nextLineValues[1]))
			self.z_rot.append(float(nextLineValues[2]))
			self.x_acc.append(float(nextLineValues[3]))
			self.y_acc.append(float(nextLineValues[4]))
			self.z_acc.append(float(nextLineValues[5]))
			self.x_mag.append(float(nextLineValues[6]))
			self.y_mag.append(float(nextLineValues[7]))
			self.z_mag.append(float(nextLineValues[8].replace("\n", "")))
			self.time.append(self.timeCounter)
			tempFile.write(nextLine)
			self.timeCounter += 1
		self.serial_port.close()
		tempFile.close()

	def setTestButtonText(self, newText):
		self.testButtonText = newText

	def createSession(self, sessionFilePath):
		newSession = Session(sessionFilePath)
		self.sessionsList.insert(0, newSession)

	def seeDetails(self, index):
		self.displayedDetails = index