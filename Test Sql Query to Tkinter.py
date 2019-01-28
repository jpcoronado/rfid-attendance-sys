from tkinter import *
import mysql.connector

query = "SELECT name, rfid FROM students WHERE rfid = '{}'"

scanned = "E1 B7 D0 2D" #Assume we scanned a card


#def scan():    #Scan using Arduino, returns UID
#    print("\nScanning...\n")
#    while True:
#        line = str(ser.readline())[2:][:-5]
#        if "Card UID: " in line:
#            print(line)
#            return line[-11:]
#            break

class Application(Frame):
    def initVars(self):
        self.studentName = StringVar()
        self.studentPic = StringVar()
        self.studentRfid = StringVar()
        
    def createWidgets(self):
        self.nameText = Label(self)
        self.nameText["textvariable"] = self.studentName
        
        self.nameText.pack()
        
        self.picBox = Label(self) #Change to picture
        self.picBox["textvariable"] = self.studentPic
        
        self.picBox.pack()
        
        self.rfidText = Label(self)
        self.rfidText["textvariable"] = self.studentRfid
        
        self.rfidText.pack()
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initVars()
        self.createWidgets()
        
    def checkDb(self, rfid):
        cnx = mysql.connector.connect(user='cs', database='test')
        cursor = cnx.cursor()
        cursor.execute(query.format(rfid))
        for (name, rfid) in cursor:
            print("{} has tapped with rfid code {}.".format(name, rfid))
            app.studentName.set(name)
            app.studentRfid.set(rfid)
            return name
        app.studentName.set(name)
        app.studentRfid.set(rfid)
        return None  


#if __name__ == "__main__":
root = Tk()
app = Application(master=root)  

while True:
    app.checkDb(scanned)        
    app.update_idletasks()
    app.update()
