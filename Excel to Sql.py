import pandas as pd
import mysql.connector

#df['Section'], df['Class Number'], df['Surname'], df['First Name'], df['Middle Name'], df['Guardian Name'], df["Guardian's Number"], df['Sex'])

cnx = mysql.connector.connect(user='cs', database='test')
cursor = cnx.cursor()

query = "INSERT INTO students20(section, classNum, surname, firstName, middleName, gName, gNum, sex) VALUES ('{}',{},'{}','{}','{}','{}','{}','{}');"


for i in ('11-Hernandez', '11-Banzon', '11-Sycip'):
    df = pd.read_excel("D:\Christiaaan's\Academic\Grade 11\Thesis\Data\School Student Roster Nov26.xlsx", \
    sheet_name=i)
    for(a,b,c,d,e,f,g,h) in zip(\
        df['Section'], df['Class Number'], df['Surname'], df['First Name'], df['Middle Name'], df['Guardian Name'], df["Guardian's Number"], df['Sex']):
        print(a,b,c,d,e,h)
        cursor.execute(query.format(a,b,c,d,e,f,g,h))
        
#cnx.commit() #Send the data to mysql [THIS WILL WRITE ON THE DATABASE]