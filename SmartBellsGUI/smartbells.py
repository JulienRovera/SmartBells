import tkinter as tk
import ViewModel as vm 
import SessionsView as sv
import GraphView as gv
import threading
import time 
#class secondFrame(tk.Frame):
	#def __init__(self):



class App(tk.Tk):
	viewModel = vm.ViewModel()
	def __init__(self):
		#initializes main window and sets up scroolbar
		super().__init__()
		self.title("SmartBells!")
		self.geometry('750x500')
		self.main_frame = tk.Frame(self)
		self.main_frame.pack(fill = tk.BOTH, expand = 1)
		self.my_canvas = tk.Canvas(self.main_frame)
		self.my_canvas.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
		self.my_scrollbar = tk.Scrollbar(self.main_frame, orient = tk.VERTICAL, command = self.my_canvas.yview)
		self.my_scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
		self.my_canvas.configure(yscrollcommand = self.my_scrollbar.set)
		self.my_canvas.bind('<Configure>', lambda e: self.my_canvas.configure(scrollregion = self.my_canvas.bbox('all')))
		self.second_frame = tk.Frame(self.my_canvas)
		self.my_canvas.create_window((0,0), window = self.second_frame, anchor = "nw")

		#initializes main widgets
		self.quitButton = tk.Button(master = self.second_frame, command = self.quit, text = "Quit")
		self.quitButton.grid(row = 0, column = 0)
		self.recordButton = tk.Button(master = self.second_frame, command = self.record, text = "+")
		self.recordButton.grid(row = 0, column = 1)

		if(self.viewModel.displayedDetails == -1):
			self.graphView = tk.Label(master = self.second_frame, text = "No session chosen")
			self.graphView.grid(row = 1, column = 0)
		else:
			self.graphView = gv.GraphView(self.second_frame, self.viewModel, 'data.csv')
			self.graphView.canvas.draw()
			self.graphView.canvas.get_tk_widget().grid(row = 1, column = 0)

		self.clearGraphButton = tk.Button(master = self.second_frame, command = self.clearGraph, text = self.viewModel.testButtonText)
		self.clearGraphButton.grid(row = 2, column = 0)
		self.sessView = sv.SessionsView(self.second_frame, self.viewModel, self)
		self.sessView.sessionsFrame.grid(row = 3, column = 0)
	#def refresh(self):
		#self.destroy()
		#self.__init__()
	def record(self):
		if(self.viewModel.isRecording):
			self.viewModel.stopRecording()
			self.recordButton.config(text = "+")
			self.sessView.sessionsFrame.destroy()
			self.sessView.__init__(self.second_frame, self.viewModel, self)
			self.sessView.sessionsFrame.grid(row=3, column = 0)
		else:
			self.recordButton.config(text = "Stop")
			self.viewModel.beginRecording()
			try:
				self.graphView.canvas.get_tk_widget().destroy()
			except:
				pass
			self.graphView = gv.GraphView(self.second_frame, self.viewModel, "", True)
			self.viewModel.displayedDetails = 1
			self.graphView.canvas.draw()
			self.graphView.canvas.get_tk_widget().grid(row = 1, column = 0)

	def clearGraph(self):
		#self.toggleGraphButton.config(text = "I've been clicked")	
		if self.viewModel.displayedDetails == -1:
			print("cannot celear")
			return
		self.graphView.canvas.get_tk_widget().destroy()
		self.graphView = tk.Label(master = self.second_frame, text = "No session chosen")
		self.graphView.grid(row = 1, column = 0)
		self.viewModel.displayedDetails = -1
	def quit(self):
		self.viewModel.isRecording = False
		exit()

	def outputDetails(self, index):
		self.viewModel.displayedDetails = index
		try:
			self.graphView.destroy()
		except AttributeError as e:
			self.graphView.canvas.get_tk_widget().destroy()
		self.graphView = gv.GraphView(self.second_frame, self.viewModel, self.viewModel.sessionsList[index].filePath, False)
		self.graphView.canvas.draw()
		self.graphView.canvas.get_tk_widget().grid(row = 1, column = 0)
		#print(index)

	def realTimeGraph(self):
		print("started real time graph")
		#while self.viewModel.isRecording:
			#try:
				#self.graphView.destroy()
			#except AttributeError as e:
				#self.graphView.canvas.get_tk_widget().destroy()
		
if __name__ == "__main__":
		app = App()
		app.mainloop()