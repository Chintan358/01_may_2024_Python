import mysql.connector

con = mysql.connector.connect(

    host = "localhost",
    user="root",
    password="",
    port=3306

)
cursor = con.cursor()

cursor.execute("show databases")

data = cursor.fetchall()

for i in data:
    print(i)