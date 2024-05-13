

class Student:

    # id = ""
    # name=""

    def __init__(self,id,name):
       self.id = id 
       self.name=name

    def display(self):
        print(self.id,self.name)

    def __str__(self) :
       return f"{self.id} : {self.name}"


s = Student(10,"avadh")
s.display()


s1 = Student(11,"Akshay")
s1.display()


print(s)
print(s1)