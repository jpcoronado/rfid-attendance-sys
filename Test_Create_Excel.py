import xlsxwriter
import mysql.connector

cnx = mysql.connector.connect(user='cs', database='test')
cursor = cnx.cursor()


def deciToAnci(deci):
    output = ""
    while (deci != 0):
        r = (deci -1) % 26
        deci = deci - r
        output = output + chr(r + 65)
        deci = deci // 26
    return output
    print("Column is",output)

labels = ["Class Number", "Surname", "First Name", "Middle Name", "Sex"]
names = ["Marew","JP","Bregg"]
color = ["Pink", "red", "greg"]
address = ["fish", "ham", "kwek"]


workbook = xlsxwriter.Workbook('test.xlsx')
worksheet = workbook.add_worksheet()

bold = workbook.add_format({'bold': True})


################### Class list (BATCH, split this to sections)
i = 1
for label in labels:
    worksheet.write(deciToAnci(i)+"1", label, bold)
    i += 1

i = 1
for something in [names, color, address]:
    j = 2
    for some in something:
        worksheet.write(deciToAnci(i) + str(j), some)
        j += 1
    i += 1


querySearch = "SELECT classNum, surname, firstName, middleName, sex \
              FROM students20;"

cursor.execute(querySearch)

row = 2 #Numbers
column = 1  #Letters
for (classNum, surname, firstName, middleName, sex) in cursor:
    worksheet.write("A"+str(row), classNum)
    worksheet.write("B"+str(row), surname)
    worksheet.write("C"+str(row), firstName)
    worksheet.write("D"+str(row), middleName)
    worksheet.write("E"+str(row), sex)
    row += 1
##################

################## Set Dates as column

queryDays = "select date from taprecords group by date;"



##################

################## Set attendance per student per day ((hekhek per section))



##################





workbook.close()