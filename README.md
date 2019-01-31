# rfid-attendance-sys
Automated attendance system using radio-frequency identification.

# Test Serial.py
  Reads serial from COM4 from arduino. Prints stuff if "CARD UID: " in line, else prints something else.

# Test Sql query.py
  Search in mysql using query of a set variable rfid. Returns True if found in database, else False.

# Test Tkinter UI.py 
  Tried tkinter.
  
# Test Rfid to Sql to Result.py
  Reads arduino serial for RFID UID then searches in MySql then prints if registered or no.
  
# Test Sql Query to Tkinter.py
  Set variable RFID, search in MySql then display in tkinter.
  
# Excel to Sql.py
  Used to transfer classlist from excel to MySql.
  
# Test CheckRFIDScanner.py
  Check if the arduino is detected.

# Test Update rfid in Sql.py
  Used to set RFID Cards in MySql.

# LATEST: Test Rfid, Sql, Tkinter.py
  Scan arduino serial, search in database, display in tkinter.
  
# Test_Record_Tap_in_Sql.py
  From manual input, records in MySql database.

# Test_Sql_to_Excel.py
  Not yet working.
  Export MySql attendance records and classlist to excel.
  
# Test_Create_Excel.py
  Create excel file from database classlist + attendance.
