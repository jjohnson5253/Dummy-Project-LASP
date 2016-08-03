#Jake Johnson Summer 2016

from PyQt4 import QtGui, QtCore

class InfoDialog(QtGui.QDialog):
	def __init__(self):
		QtGui.QDialog.__init__(self)

		self.setWindowTitle("Information")

		self.resize(200,300)

		self.mainLayout = QtGui.QHBoxLayout()
		self.setLayout(self.mainLayout)

		self.InfoLabel = QtGui.QLabel("""
			\n
			Welcome to the MARIE Navigation Controller! \n 
			MARIE is short for Mars Interactive Explorer.  Her mission is to explore 
			 the surface of Mars.  Your job is to keep her alive! \n 
			 As she explores, she is constantly using energy and getting hungry.  Even 
			 while you are away, she is getting hungry.  Make sure you check in periodically 
			 to ensure she is well fed, otherwise if her hunger reaches maximum, she will begin 
			 to lose health.  Keep MARIE alive to continue her exploration and pursue knowledge 
			 for all of humanity!
			""")

		self.mainLayout.addWidget(self.InfoLabel)