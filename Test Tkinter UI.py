from tkinter import *

class Application(Frame):
    def say_hi(self):
        print("Heeeello, World!")
        
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
        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        
        self.QUIT.pack({"side":"left"})
        
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello!"
        self.hi_there["command"] = self.say_hi
        
        self.hi_there.pack()
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.initVars()
        self.createWidgets()
        self.entrythingy = Entry()
        self.entrythingy.pack()

        # here is the application variable
        self.contents = StringVar()
        # set it to some value
        self.contents.set("this is a variable")
        # tell the entry widget to watch this variable
        self.entrythingy["textvariable"] = self.contents

        # and here we get a callback when the user hits return.
        # we will have the program print out the value of the
        # application variable when the user hits return
        self.entrythingy.bind('<Key-Return>',
                              self.print_contents)

    def print_contents(self, event):
        print("hi. contents of entry is now ---->", \
              self.contents.get())
        self.contents.set(input("Change var"))
        
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()