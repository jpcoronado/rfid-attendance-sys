import serial

ser = serial.Serial('COM4', 9600)

while(True):
    line = str(ser.readline())[2:][:-5]
    print(line)
    if("WARNING" not in line):
        print("Ready!")
    else:
        print("RFID Scanner cannot be detected.")