from tkinter import *
import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port=3306,
    database="01maypython"
)

def adduser(t1,t2,t3):
   cursor = con.cursor()
   qry = "insert into student(name,email,phone)values(%s,%s,%s)"
   val = (t1,t2,t3)
   cursor.execute(qry,val)
   con.commit()
   print("data inserted...")
   e1.delete(0,END)
   e2.delete(0,END)
   e3.delete(0,END)

form = Tk()
form.geometry("500x500")


title = Label(form,text="User Registration",fg="Red",bg="yellow",font=("Helvetica",20,"bold")).place(x=100, y=50);

uname = Label(form,text="Username").place(x=100,y=100)
email = Label(form,text="Email").place(x=100,y=150)
Phone = Label(form,text="Phone").place(x=100,y=200)

e1 = Entry(form)
e1.place(x=200,y=100)
e2 = Entry(form)
e2.place(x=200,y=150)
e3 = Entry(form)
e3.place(x=200,y=200)

b1 = Button(form, text="Submit",width="10",bg="yellow" , fg="red",command=lambda:adduser(e1.get(),e2.get(),e3.get())).place(x=200,y=250);


form.mainloop()