import tkinter as tk
import ViewModel as vm
import smartbells as sb
class SessionsView:

	def __init__(self, second_frame, viewModel, app):
		self.sessionsFrame = tk.Frame(master = second_frame)
		if len(viewModel.sessionsList) == 0:
			self.testLabel = tk.Label(master = self.sessionsFrame, text = "No sessions logged, click + to begin recording a session")
			self.testLabel.grid(row = 0, column = 0)
		else:
			for i in range(0, len(viewModel.sessionsList)):
				tempSessionFrame = SessionFrame(self.sessionsFrame, viewModel, i, app)
				tempSessionFrame.sessionFrame.grid(row = i, column = 0)

class SessionFrame:

	def __init__(self, sessionsFrame, viewModel, i, app):
		self.index = i
		self.sessionFrame = tk.Frame(master = sessionsFrame)
		self.dateLabel = tk.Label(master = self.sessionFrame, text = "Date Logged: " + viewModel.sessionsList[i].date)
		self.repLabel = tk.Label(master = self.sessionFrame, text = "\tNumber of reps: " + str(viewModel.sessionsList[i].reps))
		self.detailButton = tk.Button(master = self.sessionFrame, command = lambda: app.outputDetails(i), text = "See session details")
		self.dateLabel.grid(row = 0, column = 0)
		self.repLabel.grid(row = 0, column = 1)
		self.detailButton.grid(row = 0, column = 2)