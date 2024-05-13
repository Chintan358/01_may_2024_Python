
data = "sun Rises In East "

print(len(data))
print(data.capitalize())
print(data.casefold())
print(data.center(21,"*"))

print(data.count('s',0,9))

print(data.endswith("st1"))
print(data.endswith("n",0,3))

print(data.find('k',4,9))
print('s' in data)
# print(data.index('k',4,9))

a = "dfd123asd"

print(a.isalnum())
print(a.isalpha())
print(a.isdigit())
print(a.isidentifier())

print(data.join("sfd"))

print(data.ljust(25,'*'))