import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import tkinter as tk
import ViewModel as vm
import numpy as np
import getPos as gp

class GraphView():
	def __init__(self, second_frame, viewModel, filePath, animate):
		#set this ncols to three when adding third graph again
		self.figure, self.axis = plt.subplots(nrows = 1,ncols = 3)
		self.figure.set_size_inches(7, 2.5)
		if animate:
			return self.init_animated_graph(viewModel, second_frame)

		#try:
			#data2 = pd.read_csv(filePath)
		#except OSError as e:
			#messagebox.showinfo("error", "You must record data to output it") 
		#time = data2['Unnamed: 0']
		#print(viewModel.x_acc)
		#print(viewModel.time)
		#x_acc = data2['x_acc']
		#y_acc = data2['y_acc']
		#z_acc = data2['z_acc']
		#x_rot = data2['x_rot']
		#y_rot = data2['y_rot']
		#z_rot = data2['z_rot']
		
		#print(x_acc)
		#x_mag = data2['x_mag']
		#y_mag = data2['y_mag']
		#z_mag = data2['z_mag']
		#self.axis[0].cla()
		#self.axis[1].cla()
		#axis[2].cla()
		#self.axis[0].plot(time, x_acc, label = 'x acceleration')
		#self.axis[0].plot(time, y_acc, label = 'y acceleration')
		#self.axis[0].plot(time, z_acc, label = 'z acceleration')
		#self.axis[1].plot(time, x_rot, label = 'x rotation rate')
		#self.axis[1].plot(time, y_rot, label = 'y rotation rate')
		#self.axis[1].plot(time, z_rot, label = 'z rotation rate')
		#self.axis[2].plot(time, x_mag, label = 'x magnetometer reading')
		#self.axis[2].plot(time, y_mag, label = 'y magnetometer reading')
		#self.axis[2].plot(time, z_mag, label = 'z magnetometer reading')

		#self.axis[0].legend(loc='upper left')
		#self.axis[1].legend(loc='upper left')
		#axis[2].legend(loc='upper left')
		#self.axis[0].set_title('Acceleration Values')
		#self.axis[1].set_title('Rotation Rate Values')
		#self.axis[2].set_title('Megnetometer Readings')
		self.figure, self.axis = plt.subplots(nrows = 1,ncols = 1)
		self.figure.set_size_inches(3, 3)
		posData = gp.plot_trajectory(filePath)
		#print("\n\n\n\n\n\n")
		#print(posData)
		self.axis.cla()
		self.axis = plt.axes(projection = '3d')
		self.axis.scatter3D(posData[:,0], posData[:,1], posData[:,2])

		self.canvas = FigureCanvasTkAgg(self.figure, master = second_frame)
		#canvas.draw()
		#canvas.get_tk_widget().grid(row = 0, column = 0)

	def init_animated_graph(self, viewModel, second_frame):
		time = np.array(viewModel.time)
		x_acc = np.array(viewModel.x_acc)
		y_acc = np.array(viewModel.y_acc)
		z_acc = np.array(viewModel.z_acc)
		x_rot = np.array(viewModel.x_rot)
		y_rot = np.array(viewModel.y_rot)
		z_rot = np.array(viewModel.z_rot)
		x_mag = np.array(viewModel.x_mag)
		y_mag = np.array(viewModel.y_mag)
		z_mag = np.array(viewModel.z_mag)

		self.viewModel = viewModel
		self.axis[0].cla()
		self.axis[1].cla()
		self.axis[2].cla()
		self.axis[0].plot(time, x_acc, label = 'x acceleration')
		self.axis[0].plot(time, y_acc, label = 'y acceleration')
		self.axis[0].plot(time, z_acc, label = 'z acceleration')
		self.axis[1].plot(time, x_rot, label = 'x rotation rate')
		self.axis[1].plot(time, y_rot, label = 'y rotation rate')
		self.axis[1].plot(time, z_rot, label = 'z rotation rate')
		self.axis[2].plot(time, x_mag, label = 'x magnetometer reading')
		self.axis[2].plot(time, y_mag, label = 'y magnetometer reading')
		self.axis[2].plot(time, z_mag, label = 'z magnetometer reading')
		self.axis[0].legend(loc='upper left')
		self.axis[1].legend(loc='upper left')
		self.axis[2].legend(loc = 'upper left')
		self.axis[0].set_title('Acceleration Values')
		self.axis[1].set_title('Rotation Rate Values')
		self.axis[2].set_title('Magnetometer Readings')

		self.canvas = FigureCanvasTkAgg(self.figure, master = second_frame)
		self.ani = FuncAnimation(self.figure, self.animate, interval = 500)

	def animate(self, self2):
		time = np.array(self.viewModel.time)
		x_acc = np.array(self.viewModel.x_acc)
		y_acc = np.array(self.viewModel.y_acc)
		z_acc = np.array(self.viewModel.z_acc)
		x_rot = np.array(self.viewModel.x_rot)
		y_rot = np.array(self.viewModel.y_rot)
		z_rot = np.array(self.viewModel.z_rot)
		x_mag = np.array(self.viewModel.x_mag)
		y_mag = np.array(self.viewModel.y_mag)
		z_mag = np.array(self.viewModel.z_mag)

		self.axis[0].cla()
		self.axis[1].cla()
		self.axis[2].cla()

		self.axis[0].plot(time, x_acc, label = 'x acceleration')
		self.axis[0].plot(time, y_acc, label = 'y acceleration')
		self.axis[0].plot(time, z_acc, label = 'z acceleration')
		self.axis[1].plot(time, x_rot, label = 'x rotation rate')
		self.axis[1].plot(time, y_rot, label = 'y rotation rate')
		self.axis[1].plot(time, z_rot, label = 'z rotation rate')
		self.axis[2].plot(time, x_mag, label = 'x magnetometer reading')
		self.axis[2].plot(time, y_mag, label = 'y magnetometer reading')
		self.axis[2].plot(time, z_mag, label = 'z magnetometer reading')
		#self.axis[0].legend(loc='upper left')
		#self.axis[1].legend(loc='upper left')
		#self.axis[2].legend(loc = 'upper left')
		self.axis[0].set_title('Acceleration Values')
		self.axis[1].set_title('Rotation Rate Values')
		self.axis[2].set_title('Magnetometer Readings')