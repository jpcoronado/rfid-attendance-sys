import eel
import mysql.connector
from mysql.connector import errorcode

eel.init('web')

# sql stuff start

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

table = '<table><tr><th>ID</th><th>Class Number</th><th>Section</th><th>Last Name</th><th>First Name</th><th>Middle Name</th><th>Sex</th></tr>'

for (id, classnum, section, lastname, firstname, midname, sex) in cursor:
	table += "<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(id, classnum, section, lastname, firstname, midname, sex)

table += "</table>"

# sql stuff end

eel.start('data_display.html', block=False)

eel.writeToHTML(table)

while True:
	eel.sleep(10)