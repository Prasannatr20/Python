#977
#Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
# Example 1:

# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# Example 2:

# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

import random

class Solution:
    def sort(self, nums):
        return sorted([i*i for i in nums])
    #     if len(nums)<=1:
    #         return nums
    #     pivot = random.choice(nums)
    #     left=[i for i in nums if i<pivot]
    #     right=[i for i in nums if i>pivot]
    #     middle=[i for i in nums if i==pivot]
    #     return self.sort(left)+middle+self.sort(right)
    
    # def sortedsquares(self, nums):
    #     for i in range(len(nums)):
    #         nums[i]= nums[i]**2
    #     return self.sort(nums)



arr=[-7,-3,2,3,11]
sol= Solution()
print(sol.sort(arr))