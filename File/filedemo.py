
# f = open("test.txt",'w')
# f.write("hello...")

# f = open("test.txt",'r')
# data = f.read()
# print(data)

# f = open("test.txt",'a')
# f.write("hello...python")
# f.close()


# f = open("test.txt",'r')
# data = f.readline()
# print(data)

# f = open("test.txt",'r')
# f.seek(12)
# # print(f.tell())
# data = f.read()
# print(data)


# with open("test.txt",'r') as f:
#     data = f.read()
#     print(data)


# with open("test.txt",'r') as f:
#     while True:
#         data = f.readline()
#         if not data:
#             break;
#         print(data.capitalize())

import os

# os.mkdir("Test")
os.rmdir("test")