import serial
import mysql.connector

ser = serial.Serial('COM4', 9600)

cnx = mysql.connector.connect(user='cs', database='test')
cursor = cnx.cursor()

rfidQuery = "select * from students20 where rfid='{}'"
surnameQuery = "select * from students20 where surname='{}'"
updateQuery = "update students20 set rfid='{}' where id='{}'"

def scan():    #Scan using Arduino, returns UID
    print("\nScanning...\n")
    while True:
        line = str(ser.readline())[2:][:-5]
        if "Card UID: " in line:
            print(line)
            return line[-11:]  

def checkIfOwned(rfid):
    cursor.execute(rfidQuery.format(rfid))
    cursor.fetchall()
    rows = cursor.rowcount
    print(rows)
    if(rows == 0):
        print("Card unregisted.")
        ask(rfid)
    else:
        print("This card is already registered to {} rows.".format(rows))
        cursor.execute(rfidQuery.format(rfid))
        for (id, classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid) in cursor:
            print(id, classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid)
        if(input("Do you want to register this to another row? [y/n] ")=='y'):
            ask(rfid)
        else:
            print("Ended")
    

def ask(rfid):      #Asks for the Surname of the new owner of the RFID
    surname = input("Found card {}, what is the SURNAME of the new owner? [Enter surname] ".format(rfid))
    checkDb(surname,rfid)

def checkDb(surname, scannedRfid):      #Checks the database for the SURNAME and returns a list
    results = []
    cursor.execute(surnameQuery.format(surname))
    cursor.fetchall()
    rows = cursor.rowcount
    
    print("\n{} found.".format(rows))
    if(rows != 0 ):
        cursor.execute(surnameQuery.format(surname))
        print("id, classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid")
        for (id, classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid) in cursor:
            print(id, classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid)
            results.append((id, classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid))
        row = selectRow(results)
        askUpdate(scannedRfid, row)
    else:
        if(input("No result found. Do you want to try again? [y/n] ") == 'y'):
            ask(rfid)
        else:
            print("Ended.")
     
def selectRow(results):        #Makes the ADMIN choose 1 row and returns it
    if(len(results) == 1):
        print("\nOnly 1 row found. Proceed.")
        return results[0]
    else:
        id = input("Who do you want to own the RFID Card? [Enter the id] ")
        for row in results:
            if(row[0] == id):
                return row
     
def askUpdate(rfid, row):      #Asks the ADMIN if s/he wants to update that row's rfid
    if(input(("\nDo you want to update {} {}'s RFID Card to {}? [y/n] ").format(row[3],row[2],rfid)) == 'y'):
        try:
            cursor.execute(updateQuery.format(rfid, row[0]))
            cnx.commit()
            print("\nSuccesfully updated!")
        except Exception as e:
            print("Error occured.\n",e)

def main():
    while(True):
        try:
            rfid = scan()
            checkIfOwned(rfid)
        except Exception as e:
            print("Error!", e)
if __name__ == "__main__":
    main() 