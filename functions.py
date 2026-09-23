# def sum(a,b,c):
#     result = c
#     return c
# print(sum(4,8,6))

# def avg(a,b,c):
#     return a+b+c/3
# avg = avg(10,20,25)
# print(avg)

# def prod(a=2, b=5):
#     return a*b
# print(prod(3))

#practise

# def length(list):
#     return len(list)

# print(length([1,2,3,4,5,6,32,3,2,5,3,34]))

# def printHeros(list):
#     for i in list:
#         print(i, end=" ")

# heros=["Batman","Spiderman","Shakthiman"]
# printHeros(heros)

# def fact(n):
#     fact=1
#     while(n>=1):
#         fact*=n
#         n-=1
#     print(fact)
# fact(5)

# def conv(usd):
#     return usd*95.6
# print(conv(5))

# def evenOdd(n):
#     if(n%2==0):
#         print("EVEN")
#     else:
#         print("ODD")
# evenOdd(2)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(5)

# def fact(n):
#     if n==0 or n==1:
#         return 1
#     return fact(n-1)* n

# print(fact(4))

#Practise

# def sum(n):
#     if(n==0):
#         return 0
#     return sum(n-1)+n

# print(sum(5))


list=[1,"St",2,3,4,5]

def printList(idx, list ):
    if(idx==len(list)):
        return
    print(list[idx])
    printList(idx+1, list)
printList(0, list)