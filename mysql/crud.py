import mysql.connector


con = mysql.connector.connect(
    host ="localhost",
    user = "root",
    password="",
    port=3306,
    database="01maypython"
)

cursor = con.cursor()


# cursor.execute("insert into student(id,name,email) values(1,'avadha','avadah@gmail.com')")
# qry = "insert into student(id,name,email)values(%s,%s,%s)"
# val = (3,'akshat','akshay@gmial.com')
# cursor.execute(qry,val)
# con.commit()

# cursor.execute("select * from student")
# data = cursor.fetchall()
# print(data)
# for i in data:
#     for k in i:
#         print(k)









