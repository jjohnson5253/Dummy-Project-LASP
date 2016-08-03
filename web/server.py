#!/usr/bin/env python3

import cherrypy

import os
import sqlite3

class Main(object):
	@cherrypy.expose
	def index(self):
			return """
			<!doctype html>

<html>

<head>

<title>Marie</title>

<link rel="stylesheet" type="text/css" href="css/index.css">

</head>

<body>

<div id = "container">

<header>

</header>

<div id="description">

<br><br>

<audio controls style="margin-left: 100px;margin-right: auto;">
	<source src="audio/star-wars.ogg" type="audio/ogg">
</audio>

<br><br>

<h1 style="text-align: center;">WELCOME
</h1>
<p>to the Mars Interactive Explorer (MARIE) Information Site!</p>
<p>MARIE's mission is to better understand our not so different planet Mars and find clues about life in our galaxy.</p>
<p>Click the 'Check' button to see information about MARIE's current endeavours!</p>

</div> <!--end description div-->

<a href="check">
<div id="checkButton" class = "hvr-pulse-shrink">
Check
</div> <!--end checkButton-->
</a>

</div> <!--end container div-->

</body>

</html>

			"""


	@cherrypy.expose
	def check(self):

		#set user to to check on
		self.user = 'Jake'

		connection = sqlite3.connect('../database/myDB.db', uri=True)
		cursor = connection.cursor()
		cursor.execute('''SELECT health FROM info WHERE user=?''',(self.user,))
		health = cursor.fetchone()[0]
		cursor.execute('''SELECT hunger FROM info WHERE user=?''',(self.user,))
		hunger = cursor.fetchone()[0]
		return """
			<!doctype html>

			<html>

			<head>

			<title>Marie</title>

			<link rel="stylesheet" type="text/css" href="css/check.css">


			</head>

			<body>

			<div id = "container">

			<header>

			</header>

			<div id = "status">

			<p>
			USER1234@MARIE ~ $./status
			</p>
			<p>
			MARIE's health was last known to be: 
			</p>""" + str(health) + """
			<br>
			<p>
			MARIE's hunger was last known to be:
			</p>""" + str(hunger) + """
			<br>
			</div><!--end status div-->

			</div> <!--end container div-->

			</body>

			</html>

			"""

if __name__ == '__main__':

	cherrypy.config.update({'server.socket_host': '127.0.0.1',
                        'server.socket_port': 8080,
                       })

	cherrypy.quickstart(Main(),config={

		'/css':
		{
		'tools.staticdir.on':True,
		'tools.staticdir.dir':"~/Desktop/marie/firstTry/web/css"
		},
		'/img':
		{
		'tools.staticdir.on':True,
		'tools.staticdir.dir':"~/Desktop/marie/firstTry/web/img"
		},
		'/audio':
		{
		'tools.staticdir.on':True,
		'tools.staticdir.dir':"~/Desktop/marie/firstTry/web/audio"
		}


	})