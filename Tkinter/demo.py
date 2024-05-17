from tkinter import *

tops =  Tk()
tops.geometry("500x500")

# b1 = Button(tops,text="Right").pack(side=RIGHT)
# b2 = Button(tops,text="Left").pack(side=LEFT)
# b3 = Button(tops,text="Top").pack(side=TOP)
# b4 = Button(tops,text="Bottom").pack(side=BOTTOM)


# name = Label(tops,text="Username").grid(row=1,column=1)
# email = Label(tops,text="Email").grid(row=2,column=1)
# phone = Label(tops,text="Phone").grid(row=3,column=1)

# e1 = Entry(tops)
# e1.grid(row=1,column=2)
# e2 = Entry(tops)
# e2.grid(row=2,column=2)
# e3 = Entry(tops)
# e3.grid(row=3,column=2)

# btn = Button(tops,text="Submit").grid(row=4,column=2)



name = Label(tops,text="Username").place(x=50,y=10)
email = Label(tops,text="Email").place(x=50,y=50)
phone = Label(tops,text="Phone").place(x=50,y=90)

e1 = Entry(tops)
e1.place(x=150,y=10)
e2 = Entry(tops)
e2.place(x=150,y=50)
e3 = Entry(tops)
e3.place(x=150,y=90)

btn = Button(tops,text="Submit").place(x=150,y=130)


tops.mainloop()