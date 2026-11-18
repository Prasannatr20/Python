#You are given a sorted list of integers. Remove the duplicates in place so that each distinct element appears only once.
#Return the number of distinct elements, k. The first k positions of the list must contain the unique elements in sorted order.
#Do not create another list or use a set.


arr = [1, 1, 2]

def remove_dup(nums):
    j=0
    for i in range(1, len(nums)):
        if nums[i]!= nums[i-1]:
            nums[j]= nums[i]
            j+=1
    return nums



print(remove_dup(arr))