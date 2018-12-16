import mysql.connector

# create connection object to database yourdb
mydb_connection = mysql.connector.connect(
		host = "localhost",
		user = "username",
		password = "password",
		database = "yourdb"
)

# get connection command object
db_cursor = mydb_connection.cursor()

#execute create table command
db_cursor.execute("CREATE TABLE customers (employee VARCHAR(100), profile VARCHAR(50))")

#execure show tables to see if table is present
db_cursor.execute("SHOW TABLES")

for x in db_cursor:
	print(x)	


