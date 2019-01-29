import mysql.connector
from mysql.connector import errorcode


# Creates connection to MySQL Server.
# Handles connection errors.

config = {
	'user': 'root',
	'password': '10432200bcAt',
	'host': '127.0.0.1',
	'database': 'attendance_system',
	'raise_on_warnings': True
}

try:
	cnx = mysql.connector.connect(**config)
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your username or password.")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist.")
	else:
		print(err)
else:
	print("Database connection successful.")
	

cursor = cnx.cursor()

query = ("SELECT * FROM students")

cursor.execute(query)

for (id, classnum, section, lastname, firstname, midname, sex) in cursor:
	print(id, classnum, section, lastname, firstname, midname, sex)


cnx.close()
print("Database connection closed.")

wait = input('...')
