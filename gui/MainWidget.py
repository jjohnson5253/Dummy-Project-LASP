
#Jake Johnson Summer 2016

from PyQt4 import QtGui, QtCore

import time
import sqlite3

from LogoWidget import LogoWidget
from DisplayWidget import DisplayWidget
from InfoDialog import InfoDialog
from Pet import Pet

class MainWidget(QtGui.QWidget):
	def __init__(self):
		#make this a widget
		QtGui.QWidget.__init__(self)

		#main layout will be a Horizontal Box layout
		self.mainLayout = QtGui.QHBoxLayout(self)

		#logowidget layout will be left-most layout within main layout
		self.LogoWidget = LogoWidget()
		self.LogoWidget.setStyleSheet("background-color:white;")
		self.mainLayout.addWidget(self.LogoWidget)

		#Display layout will be right-most layout
		self.DisplayWidget = DisplayWidget()
		self.mainLayout.addWidget(self.DisplayWidget)

		#connect Feed button to action
		self.DisplayWidget.feedButton.clicked.connect(self.feed)

		#connect info "?" button to action
		self.DisplayWidget.infoButton.clicked.connect(self.openInfoDialog)

		#instantiate the pet
		self.Pet = Pet()

		#get pet hunger value and set progress bar to display it
		self.hunger = self.Pet.hunger
		self.DisplayWidget.hungerProgressBar.setValue(self.hunger)

		#get pet health value and set progress bar to display it
		self.health = self.Pet.health
		self.DisplayWidget.healthProgressBar.setValue(self.health)

		#start hunger timer
		self.hungerTimer()

		#update hunger to see how hunger Marie got from last save
		self.updateHungerFromPreviousSave()

		#create an update timer to update application
		self.updateTimer = QtCore.QTimer()

		#update application every second
		self.updateTimer.start(1000)
		self.updateTimer.timeout.connect(self.update)


	def feed(self):
		#replenishes hunger

		self.hunger = self.hunger - 1
		self.DisplayWidget.hungerProgressBar.setValue(self.hunger)

	def openInfoDialog(self):
		self.InfoDialog = InfoDialog()
		self.InfoDialog.exec_()

	def hungerTimer(self):
		#calls getHungry() every 10000ms

		self.hungerTimer = QtCore.QTimer()
		#gains hunger every 10 seconds
		self.hungerTimer.start(10000)
		self.hungerTimer.timeout.connect(self.getHungry)

	def getHungry(self):
		#this method increases hunger, along with decreasing health (if hunger is low)

		#if health is less than 5, decrease health
		if(self.hunger > 95):
			self.health = self.health - 1
			self.DisplayWidget.healthProgressBar.setValue(self.health)
			#if health is 0 return so you stop losing hunger
			if(self.hunger == 100):
				return

		#increase hunger
		self.hunger = self.hunger + 1
		self.DisplayWidget.hungerProgressBar.setValue(self.hunger)

	def updateHungerFromPreviousSave(self):

		connection = sqlite3.connect('../database/myDB.db', uri=True)
		cursor = connection.cursor()
		cursor.execute('''SELECT time FROM info WHERE user=?''',(self.Pet.user,))
		self.prevTime = cursor.fetchone()[0]

		self.time = time.time()

		self.differenceInTime = self.time - self.prevTime

		print(self.differenceInTime)

		self.hunger = self.hunger + (self.differenceInTime / 10)
		self.DisplayWidget.hungerProgressBar.setValue(self.hunger)



	def update(self):

		#make sure hunger and health don't go out of bounds
		if(self.hunger > 100):
			self.hunger = 100
			self.DisplayWidget.hungerProgressBar.setValue(self.hunger)

		if(self.hunger < 0):
			self.hunger = 0
			self.DisplayWidget.hungerProgressBar.setValue(self.hunger)

		if(self.health > 100):
			self.health = 100
			self.DisplayWidget.healthProgressBar.setValue(self.health)

		if(self.health <= 0):
			self.health = 0
			self.DisplayWidget.healthProgressBar.setValue(self.health)
			self.DisplayWidget.label.setText("MARIE IS DEAD!")

		elif(self.hunger > 90):
			self.DisplayWidget.label.setText("MARIE is really hungry. Feed her!")

		elif(self.hunger > 50):
			self.DisplayWidget.label.setText("MARIE looks a bit hungry.")

		else:
			self.DisplayWidget.label.setText("MARIE seems happy and healthy.")







		