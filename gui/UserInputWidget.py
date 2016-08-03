#Jake Johnson Summer 2016

from PyQt4 import QtGui, QtCore

class UserInputWidget(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		#main layout to put the framed layout within
		self.mainLayout = QtGui.QHBoxLayout(self)

		#make frame
		self.frame = QtGui.QFrame()
		self.frame.setFrameShape(2)

		#create vertical layout that inherits the frame
		self.vlayout = QtGui.QVBoxLayout(self.frame)

		#make feed button
		self.feedButton = QtGui.QPushButton("Feed")
		self.vlayout.addWidget(self.feedButton)

		#add frame with vlayout to main layout
		self.mainLayout.addWidget(self.frame)