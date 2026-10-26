n = 1234
m = n
length = len(str(m))

def amtsrong_number(num):
    copy = num
    prod = 1
    sum = 0
    while(copy!=0):
        temp = copy%10
        prod = pow(temp, length)
        sum+=prod
        copy=copy//10
    if num==sum:
        return True
    else:
        return False

    
print(amtsrong_number(m))