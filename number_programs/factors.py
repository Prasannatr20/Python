
#Brute force
# n = int(input("Enter a number: "))

# def factors(num):
#     res=[]
#     for i in range(1, (num//2)+1):
#         if num%i==0:
#             res.append(i)
#     res.append(num)
#     return res

# print(factors(n))


#Optimal method

import math
n = int(input("Enter a number: "))

def factors(num):
    res=[]
    for i in range(1, int((math.sqrt(num))+1)):
        if num%i==0:
            res.append(i)
        if num//i!=i:
            res.append(num//i)
    #res.sort()
    return res


print(factors(n))