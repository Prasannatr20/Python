#Your task is to move every zero in an integer array,to the end
# without changing the relative order of the non-zero elements.


# arr = [0, 1, 0, 2, 0, 3, 4]

# def move_zeroes(nums):
#     for i in nums:
#         if i==0:
#             nums.remove(0)
#             nums.append(0)
#     return nums

# print(move_zeroes(arr))


arr=[0, 0, 0]

def move_zeroes(nums):
    j=0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j]= nums[i]
            j+=1
    while(j <len(nums)):
        nums[j]=0
        j+=1
    return nums

print(move_zeroes(arr))