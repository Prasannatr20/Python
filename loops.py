#count = 1
# i=5
# while i>=1:
#     # print("hello")
#     print(i)
#     i-=1

#Practise

# count=1
# while count<=100:
#     print(count)
#     count+=1

# count = 100
# while count>=1:
#     print(count)
#     count-=1

# n = int(input("Enter a number: "))
# count = 1
# while count<=10:
#     print(n, " *", count, "= ", n*count)
#     count+=1

# count=1
# list = []
# while count<=10:
#     list.append(count*count)
#     count+=1
# print(list)

# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# i =0
# print(len(tup))
# found =False
# n= int(input("Enter a number: "))
# while i<len(tup):
#     if(tup[i]==n):
#         print(i)
#         found=True
#     i+=1
# if(found==False):
#     print("Entered number is not present")

# i = 1
# while i<=5:
#     if(i==3):
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i<=100:
#     if(i%2!=0):
#         i+=1
#         continue
#     print(i)
#     i+=1

# i=1
# while i<=10:
#     if(i==5):
#         break
#     print(i)
#     i+=1
# else:
#     print("End")

# list=[1,4,25,36,49,64,81,100]
# for val in list:
#     print(val)

# list=[1,4,9,16,25,36,49,64,81,100]
# num = int(input("Enter a number: "))
# found = False
# i=0
# for val in list:
#     if num==val:
#         print(i)
#         found=True
#         break
#     i+=1
# if not found:
#     print("Number is not available")


# for i in range(0, 11, 2):
#     print(i)

# for i in range(1, 101):
#     print(i)

# for i in range(100, 0, -1):
#     print(i)

# n = int(input("Enter a number: "))
# for i in range(1, 11):
#     print(n*i)

# i = 1
# sum=0
# while i<=10:
#     sum+=i
#     i+=1
# print(sum)


# fact=1
# for i in range(6, 0, -1):
#     fact*=i
# print(fact)


# a=0
# b=1
# print(a)
# print(b)
# for i in range(11):
#     c=a+b
#     a=b
#     b=c
#     print(c)


# a="abuc"
# b=""
# for i in range(len(a)-1, -1, -1):
#     b+=a[i]
# print(b)