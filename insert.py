import mysql.connector

# get mysql connection object

my_db_connection = mysql.connector.connect(
		host = "localhost",
		user = "username",
		password = "password",
		database = "yourdbname"
	)

# create command objacet using connecion
db_cursor = my_db_connection.cursor()

sql = "insert into customers (employee,profile) values (%s, %s)"
val = ("Pramod","Software")

# execute insert
db_cursor.execute(sql,val)

# commit inserion to database
my_db_connection.commit()

# get number of rows updated
print(db_cursor.rowcount,s " rows inserted")