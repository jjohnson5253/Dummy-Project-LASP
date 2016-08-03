#!/usr/bin/env python3

import sqlite3

#variable to be added to hunger row in database
hunger = 14

#connect to database
connection = sqlite3.connect('my-db.db', uri=True)

#create a cursor to navigate database
cursor = connection.cursor()

#execute sql command with python variable as parameter
#note the '?' in the sql command is a placeholder and the variable
#must be passed in as a tuple for whatever reason
cursor.execute('''UPDATE attributes SET quantity=? 
	WHERE attribute='hunger';''', (hunger,))

#select the hp quantity from the database using sql commands
cursor.execute('''SELECT quantity FROM attributes WHERE attribute="hp"''')

#create a variable that stores the fetched value from the above command
#note that fetchone() returns a tuple so I want the '0' index of that tuple
hp = cursor.fetchone()[0]

#print fetched variable
print(hp)

#must call this to save changes
connection.commit()

#close connection
connection.close()