class Demo:

    
    # def sample(self,a,b):
    #     print("sample method calling",a,b)

    # def sample(self,a):
    #     print("sample method calling",a)

    def sample(self,*a):
        print(a)
    

d = Demo()
d.sample(10)
d.sample(10,20)
d.sample(10,20,30,40,"Avadh",'Vishrut')