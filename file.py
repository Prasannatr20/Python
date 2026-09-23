# f = open("text.txt", "r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()


# f =open("demo.txt", "r+")
# f.write("Hi!")
# f.write("Line 2")
# print(f.read())
# f.close()

# with open("demo.txt", "a+") as p:
#     p.write("Hello from last")
#     print(p.read())

import os
os.remove("demo.txt")