# Import mysql connector to create create connection

import mysql.connector

# create connecting string

myDbConnection = mysql.connector.connect(
	host = "localhost",
	user = "username",
	password = "password"
	)

# connect to database

db_cursor = myDbConnection.cursor()

# execute the command using cursor to create database

db_cursor.execute("CREATE DATABASE PracticeDB")

# check whether database we created exists or not

db_cursor.execute("SHOW DATABASES")

# List Down DB's and PracticeDB should present there.

for x in db_cursor:
	print(x)