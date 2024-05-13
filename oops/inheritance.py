

class Pen:
    
    price = 10
    color = "red"
    company = "cello"
    def toWrite(self):
        
        print("write somting...")
        print(f"{self.price} - {self.color} - {self.company}")

class NoteBook(Pen):
    pages = 100;
    def display(self):
        print("display something.")
        print(f"{self.price} - {self.color} - {self.company} - {self.pages}")
        
class Test(NoteBook):
    pass

p = Pen()
n = NoteBook()

p.toWrite()
n.display()
n.toWrite()

