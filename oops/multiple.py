

class Avadh:
    
    def display1(self):
        print("**avadh***")

class Akshay:
    def display2(self):
        print("**Akshay***")

class Visrut:
    def display3(self):
        print("**Vishrut***")

class Faculty(Avadh,Akshay,Visrut):
    pass

f = Faculty()
f.display1()
f.display2()
f.display3()