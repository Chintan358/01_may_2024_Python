import sqlite3

con = sqlite3.connect("mydb.db")


# con.execute("create table reg(id int primary key, name varchar(20),email varchar(50))")

# con.execute("insert into reg(id,name,email)values(3,'akshay','aks@gmial.com')")
# con.commit()


# con.execute("update reg set email='vishrut@gmial.com' where id=2")
# con.commit()

# con.execute("delete from reg where id = 3")
# con.commit()



# data = con.execute("select * from reg")

# for i in data:
#     print(i)

con.execute("update reg set name='' where id=2")
con.commit()