#15. 3Sum
""""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

class Solution:
    def threeSum(self, nums):
        left =0
        right = left +1




arr = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(arr))