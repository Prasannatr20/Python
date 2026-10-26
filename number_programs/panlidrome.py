n = 1221
m = n

def palindrome(num):
    copy = num
    rev=0
    while(copy!=0):
        temp=copy%10
        rev = (rev*10)+temp
        copy=copy//10
    if rev == num:
        return True
    else:
        return False

print(palindrome(m))