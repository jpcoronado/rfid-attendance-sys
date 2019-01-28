from tkinter import *
import mysql.connector
import serial

ser = serial.Serial('COM4', 9600)

cnx = mysql.connector.connect(user='cs', database='test')
cursor = cnx.cursor()

query = "SELECT classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid FROM students20 WHERE rfid = '{}'"

def scan():    #Scan using Arduino, returns UID
    print("\nScanning...\n")
    while True:
        line = str(ser.readline())[2:][:-5]
        if "Card UID: " in line:
            print(line)
            return line[-11:]


class AIDSApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        
        self.title("AIDS in UPIS")
        self.geometry("1000x1000")
        
        self.protocol('WM_DELETE_WINDOW', self.closeApp) 
        
        self.option_add("*Font", "Lucida 20")
        
        
        self.container = Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        self.home = HomeScreen(parent=self.container)
        self.home.grid(row=0, column=0, sticky="nsew")
        
        self.accept = AcceptScreen(parent=self.container)
        self.accept.grid(row=0, column=0, sticky="nsew")
        
        self.deny = DenyScreen(parent=self.container)
        self.deny.grid(row=0, column=0, sticky="nsew")
        
#        for F in (HomeScreen, AcceptScreen, DenyScreen):
#            pageName = F.__name__
#            frame = F(parent=self.container)
#            self.frames[pageName] = frame
#            frame.grid(row=0, column=0, sticky="nsew")
        
        self.home.tkraise()
        
    def closeApp(self):
        print("!!CLOSING!!")
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.destroy()
            cnx.close()
        print("!!CLOSED!!")
    

class HomeScreen(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
#        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.nameText = Label(self, text="Welcome to UPIS!\nTap your card to record your attendance.")
        self.nameText.config(bg="#aff")
        self.nameText.pack(fill="both", expand=True)

class AcceptScreen(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.initVars()
#        self.pack()
#        self.config(bg="#aff")
        self.createWidgets()
        
    def initVars(self):
        self.classNum = IntVar()
        self.surname = StringVar()
        self.firstName = StringVar()
        self.middleName = StringVar()
        self.sex = StringVar()
        self.section = StringVar()
        self.gName = StringVar()
        self.gNum = StringVar()
        self.rfid = StringVar()
        self.pic = StringVar()
    
    def createWidgets(self):
        self.cnText = Label(self, textvariable=self.classNum)
        self.cnText.pack()
        
        self.nameText = Label(self, textvariable=self.firstName)
        self.nameText.pack()
        
        self.surnameTest = Label(self, textvariable=self.surname)
        self.surnameTest.pack()
        
        self.sexText = Label(self, textvariable=self.sex)
        self.sexText.pack()
        
        self.picBox = Label(self) #Change to picture
        self.picBox["textvariable"] = self.pic
        self.picBox.pack()
        
        self.sectionText = Label(self, textvariable=self.section)
        self.sectionText.pack()
        
        self.rfidText = Label(self, textvariable=self.rfid)
        self.rfidText.pack()
        
class DenyScreen(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
#        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.text = Label(self, text="Sorry that card is not registered.")
        self.text.config(bg="#aff")
        self.text.pack()
        
def checkDb(rfid):
    cursor.execute(query.format(rfid))
    for (classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid) in cursor:
        print("{} has tapped with rfid code {}.".format(firstName, rfid))
        print("Name:",firstName,middleName,surname,"Sex:",sex)
        print("Section:", section)
        print("Class Number:", classNum)
        if(gName != "nan" and gNum != "nan"):
            print("Contact",gName,"through",gNum)
        return classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid 
    return False

def main():
    app = AIDSApp()
    
    app.update_idletasks()
    app.update()
    
    while True:
        scanned = scan()
        result = checkDb(scanned)
        print(result)
        if(result):
            classNum, surname, firstName, middleName, sex, section, gName, gNum, rfid = result
            app.accept.classNum.set(classNum)
            app.accept.surname.set(surname)
            app.accept.firstName.set(firstName)
            app.accept.middleName.set(middleName)
            app.accept.sex.set(sex)
            app.accept.section.set(section)
            app.accept.gName.set(gName)
            app.accept.gNum.set(gNum)
            app.accept.rfid.set(rfid)
#            app.accept.pic.set()   #Set once pics are ready
            app.accept.tkraise()
        else:
            app.deny.tkraise()
        app.update_idletasks()
        app.update()
        

if __name__ == "__main__":
    main()