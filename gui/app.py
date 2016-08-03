#!/usr/bin/env python3

#Jake Johnson Summer 2016

from PyQt4 import QtGui, QtCore

import sys

from MainWidget import MainWidget

import sqlite3

import time

class App(QtGui.QApplication):
	def __init__(self):
		#initialize this class as a QApplication
		QtGui.QApplication.__init__(self, sys.argv)

		#set application name
		self.setApplicationName("MARIE")

		#instantiate the main window
		self.mainWindow = MainWindow()

		#display the window
		self.mainWindow.show()

class MainWindow(QtGui.QMainWindow):
	#This is the main GUI window.  This is what contains all the QWidgets seen in the app
	def __init__(self):
		#initialize this class as a QMainWindow
		QtGui.QMainWindow.__init__(self)

		#self.setStyleSheet("background-color:orange;")

		#set window title
		self.setWindowTitle("Marie")

		#set window size
		self.resize(700,200)

		#insert main widget into this window
		self.mainWidget = MainWidget()

		#set central widget to main widget
		self.setCentralWidget(self.mainWidget)

		#self.myCloseEvent = closeEvent()

	def closeEvent(self,evnt):

		connection = sqlite3.connect('../database/myDB.db', uri=True)
		cursor = connection.cursor()
		#save hunger
		cursor.execute('''UPDATE info SET hunger=? 
		WHERE user=?;''', (self.mainWidget.hunger,self.mainWidget.Pet.user,))
		#save health
		cursor.execute('''UPDATE info SET health=? 
		WHERE user=?;''', (self.mainWidget.health,self.mainWidget.Pet.user,))
		#save time
		cursor.execute('''UPDATE info SET time=? 
		WHERE user=?;''', (time.time(),self.mainWidget.Pet.user,))

		connection.commit()
		connection.close()

def main():
	app = App()

	#start the application loop
	sys.exit(app.exec_())

if(__name__=="__main__"):
	main()

