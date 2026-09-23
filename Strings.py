# a='This "is" a string'
# print(a)

# str="First line \nSecond line"
# tab= "Before space \tAfter space"
# print(str)
# print(tab)


#Concatination

# str1="Hi"
# str2="Hello"
# print(str1+" "+str2)
# print("Hi"+ " Hello")
# print(len(str1))
# print(len("Hello"))

#Index

# str="Prasanna"
# print(str[6])

#Slicing

str= "I am Prasanna"
print(str[1:5])
print(str[0:9])
print(str[0:len(str)])
print(str[2:]) #Will go till the last index
print(str[:5])#Will take from the 0th index
print(str[-3:-1])

ends="nna"
print(str.endswith(ends))
print(str.capitalize())
print(str.replace("am","haha"))
print(str.find("am"))
print(str.count("a"))