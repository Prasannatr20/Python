#Given a list of integers, return its second-largest distinct value.

arr = [23, 44, 2, 334, 2, 456]

def second_largest(nums):
    largest = float('-inf')
    second_largest = float('-inf')
    for i in nums:
        if i>largest:
            second_largest = largest
            largest =i
        elif i>second_largest and i<largest:
            second_largest=i

    if second_largest == float('-inf'):
        second_largest= None
    return second_largest

print(second_largest(arr))