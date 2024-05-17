



class Point:

    
    def __init__(self,a,b):
        self.a = a;
        self.b = b
        
   
    def __add__(self,other):
        return self.a+other.a ,self.b+other.b
       
    def __mul__(self,other):
        return self.a*other.a ,self.b*other.b

    def __str__(self):
        return (f"{self.a},{self.b}")


p1 = Point(10,20)
p2 = Point(30,40)

print(p1)
print(p2)
print(p1+p2)
print(p1*p2)