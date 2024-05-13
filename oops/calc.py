
class Calc:

    def square(self,a):
        print(a*a)

    def add(self,a,b):
        print(a+b)
    
    def cube(self,a):
        return a*a*a

c  = Calc()
c.square(10)
c.add(10,20)
k =  c.cube(10)
print(k)
print(c.cube(20))