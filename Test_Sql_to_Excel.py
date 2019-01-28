import mysql.connector

cnx = mysql.connector.connect(user='cs', database='test')
cursor = cnx.cursor()
