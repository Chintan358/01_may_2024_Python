
def msg():
    print("Hello")

def square(a):
    print(a*a)

def add(a,b):
    print(a+b)

def cube(a):
    return a*a*a

def inter(base,time,rate=12):
    print(base * (1+rate*time))


def vararg(*k,**a):
    print(k)

def vararg1(**k):
    print(k)


x = lambda :print(k+10)

msg()
square(20)
add(10,20)
k = cube(10)
print(k)
inter(time =2,base=2000)
vararg(10,20,30,40,50,60)
vararg1(test=10,tech=20)

x(10)