#Jake Johnson Summer 2016

from PyQt4 import QtGui, QtCore
import sqlite3

class Pet(QtGui.QWidget):
	def __init__(self):
		#make this a widget
		QtGui.QWidget.__init__(self)

		#set user to use for app
		self.user = 'Jake'

		#connect to database
		connection = sqlite3.connect('../database/myDB.db', uri=True)

		#create a cursor to navigate database
		cursor = connection.cursor()

		#select the hp quantity from the database using sql commands
		cursor.execute('''SELECT health FROM info WHERE user="Jake"''')
		
		#create a variable that stores the fetched value from the above command
		#note that fetchone() returns a tuple so I want the '0' index of that tuple
		self.health = cursor.fetchone()[0]

		#select the hp quantity from the database using sql commands
		cursor.execute('''SELECT hunger FROM info WHERE user="Jake"''')
		
		#create a variable that stores the fetched value from the above command
		#note that fetchone() returns a tuple so I want the '0' index of that tuple
		self.hunger = cursor.fetchone()[0]

		#close connection
		connection.close()


