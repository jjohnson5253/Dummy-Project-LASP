#Jake Johnson Summer 2016

from PyQt4 import QtGui, QtCore

class DisplayWidget(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		#main layout to put the framed layout within
		self.mainLayout = QtGui.QHBoxLayout(self)

		#make frame
		#self.frame = QtGui.QFrame()
		#self.frame.setFrameShape(2)

		#create vertical layout to hold button layout and status bar layout
		self.vlayout = QtGui.QVBoxLayout()

		#add stretch
		self.vlayout.addStretch()

		#######################USER INPUT STUFF#########################


		self.buttonLayout = QtGui.QHBoxLayout()

		#add label
		self.label = QtGui.QLabel("MARIE booted up!")
		self.buttonLayout.addWidget(self.label)

		#add stretch
		self.buttonLayout.addStretch()

		#make feed button
		self.feedButton = QtGui.QPushButton("Feed")
		self.feedButton.setMaximumSize(150,45)
		self.buttonLayout.addWidget(self.feedButton)

		self.infoButton = QtGui.QPushButton("?")
		self.infoButton.setMaximumSize(30,45)
		self.buttonLayout.addWidget(self.infoButton)


		self.vlayout.addLayout(self.buttonLayout)

		##############STRETCH BETWEEN BUTTON AND STATUS BAR##############
		self.vlayout.addStretch()

		#####################STATUS BAR STUFF############################

		#create status bar frame
		self.statusBarFrame = QtGui.QFrame()
		self.statusBarFrame.setFrameShape(2)

		#create status bar layout
		self.statusBarLayout = QtGui.QVBoxLayout(self.statusBarFrame)

		#create hlayout for health
		self.healthStatusLayout = QtGui.QHBoxLayout()

		#Add health label to health status layout
		self.healthLabel = QtGui.QLabel("Health  ")
		self.healthStatusLayout.addWidget(self.healthLabel)

		#add progress bar to statusBarLayout
		self.healthProgressBar = ProgressBar()
		self.healthStatusLayout.addWidget(self.healthProgressBar)

		#add health status layout to status bar layout
		self.statusBarLayout.addLayout(self.healthStatusLayout)

		#create hlayout for hunger
		self.hungerStatusLayout = QtGui.QHBoxLayout()

		#add hunger label to hunger status layout
		self.hungerLabel = QtGui.QLabel("Hunger")
		self.hungerStatusLayout.addWidget(self.hungerLabel)

		#add hunger progress bar to hunger status layout
		self.hungerProgressBar = ProgressBar()
		self.hungerStatusLayout.addWidget(self.hungerProgressBar)

		#add hunger status layout to status bar layout
		self.statusBarLayout.addLayout(self.hungerStatusLayout)

		#add status bar to vlayout
		self.vlayout.addWidget(self.statusBarFrame)

		#####################END STATUS BAR STUFF########################

		#add Marie image to vlayout
		#self.pixmap = QtGui.QPixmap("img/marie.jpg")
		#self.imageLabel = QtGui.QLabel()
		#self.imageLabel.setPixmap(self.pixmap)
		#self.vlayout.addWidget(self.imageLabel)

		#add frame with vlayout to mainLayout
		self.mainLayout.addLayout(self.vlayout)

class ProgressBar(QtGui.QProgressBar):
	def __init__(self):
		QtGui.QProgressBar.__init__(self)




		