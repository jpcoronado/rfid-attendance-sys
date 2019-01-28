import serial
import mysql.connector

ser = serial.Serial('COM4', 9600)


query = "SELECT name, rfid FROM students WHERE rfid = '{}'"

def scan():
    print("\nScanning...\n")
    while True:
        line = str(ser.readline())[2:][:-5]
        if "Card UID: " in line:
            print(line)
            return line[-11:]
            break
            
def checkDb(rfid):
    #This is inside if you need to update the database while this is running
    cnx = mysql.connector.connect(user='cs', database='test')
    cursor = cnx.cursor()
    
    cursor.execute(query.format(rfid))
    for (name, rfid) in cursor:
        print("{} has tapped with rfid code {}.".format(name, rfid))
        return name
    return None

def interface(name):
    if(name != None):
        print("Welcome to UPIS,", name)
    else:
        print("Sorry, are you sure that card is registered?")
        

if __name__ == "__main__":
    while True:
        interface(checkDb(scan()))

#        cursor.close()
#        cnx.close()
