import mysql.connector

# get mysql connection object

my_dbconnection = mysql.connector.connect(
	host = "localhost",
	user = "user",
	password = "password",
	database = "yourdb" 
	)

db_cursor = my_dbconnection.cursor()

sql = "insert into customers(employee, profile) values (%s,%s)"
val = [
		('Pradeer', 'developer'),
		('rahul', 'desginer')
		]

db_cursor.executemany(sql,val)

my_dbconnection.commit()		

print(db_cursor.rowcount," rows inserted")