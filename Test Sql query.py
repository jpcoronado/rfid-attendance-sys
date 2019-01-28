import mysql.connector

cnx = mysql.connector.connect(user='cs', database='test')
cursor = cnx.cursor()

query = "SELECT name, rfid FROM students WHERE rfid = '{}'"

scanned = "E1 B7 D0 2D"

cursor.execute(query.format(scanned))

allowed = False
for (name, rfid) in cursor:
    print("{} has tapped with rfid code {}.".format(name, rfid))
    allowed = True
    break;

if(allowed):
    print("Welcome to UPIS!")
else:
    print("Sorry, is this card registered?")

cursor.close()
cnx.close()