#Jake Johnson Summer 2016

from PyQt4 import QtGui, QtCore

class LogoWidget(QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)

		#main layout to put the framed layout within
		self.mainLayout = QtGui.QVBoxLayout(self)

		self.LaspLogo = QtGui.QPixmap("img/lasp.jpeg").scaled(125,30)
		self.LaspLabel = QtGui.QLabel()
		self.LaspLabel.setPixmap(self.LaspLogo)
		self.mainLayout.addWidget(self.LaspLabel)

		self.NasaLogo = QtGui.QPixmap("img/nasa.png").scaled(125,100)
		self.NasaLabel = QtGui.QLabel()
		self.NasaLabel.setPixmap(self.NasaLogo)
		self.mainLayout.addWidget(self.NasaLabel)

		self.setStyleSheet("background-color:white;")
