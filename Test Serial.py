import serial

ser = serial.Serial('COM4', 9600)

def scan():
    print("\nScanning...\n")
    while True:
        line = str(ser.readline())[2:][:-5]
        
        if "Card UID: " in line:
            print(line)
            print(line[-11:])
#            if 'E1 B7 D0 2D' in line:
#                print("YOU GOT IT! THIS IS THE CARD! YEAAA")
#                print("**WAIT, I meant to say 'The Only Card' kasi wala pa tayong ibang RFID CARDS HAHAHAHHA")
#            else:
#                print("I dont know ya sari")
#            scan()
            break
            
if __name__ == "__main__":
    scan()
