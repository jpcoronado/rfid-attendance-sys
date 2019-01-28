import mysql.connector

cnx = mysql.connector.connect(user='cs', database='test')
cursor = cnx.cursor()

queryRecordTap = "INSERT INTO taprecords() VALUES(0,'{}','{}', CURDATE(), CURTIME());"  #Format with studentId, rfid

queryShowRecords = "SELECT * FROM taprecords JOIN students20 ON taprecords.studentId=students20.id;"

querySearch = "SELECT classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid FROM students20 WHERE rfid = '{}'"

def checkDb(rfid):
    cursor.execute(querySearch.format(rfid))
    for (classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid) in cursor:
        print("{} has tapped with rfid code {}.".format(firstName, rfid))
        print("Name:",firstName,middleName,surname,"Sex:",sex)
        print("Section:", section)
        print("Class Number:", classNum)
        if(gName != "nan" and gNum != "nan"):
            print("Contact",gName,"through",gNum)
        return classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid
    return False

def recordTap(studentId, rfid):
    cursor.execute(queryRecordTap.format(studentId, rfid))
    cnx.commit()

def showRecords():
    cursor.execute(queryShowRecords)
    for a in cursor:
        print(a)

def main():
    while(True):
        recordTap(input("studentId: "),None)
        showRecords()

if __name__ == "__main__":
    main()
