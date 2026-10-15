nums = []

def insert_arr(arr, index, value):
    if(index<0 or index> len(arr)):
        return "Enter a valid index"
    elif(index==len(arr) or len(arr)==0):
        arr.append(value)
        return arr
    arr.append(0)
    j=len(arr)-2
    while j>=index:
        arr[j+1] = arr[j]
        j-=1
    arr[index]= value
    return arr

print(insert_arr(nums, 0, 99))