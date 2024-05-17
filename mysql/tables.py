import mysql.connector


con = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password="",
    port=3306,
    database="01maypython"
)

cursor = con.cursor()

# cursor.execute("create table student(id int primary key, name varchar(20),email varchar(50))")

cursor.execute("show tables")
data = cursor.fetchall()
print(data)