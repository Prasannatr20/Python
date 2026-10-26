n = 12345
m=n

def count_digits(num):
    count=0
    while (num!=0):
        count+=1
        num=num//10
    return count

print(count_digits(m))


#Coverting to string

#print(len(str(m)))