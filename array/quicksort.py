import random

class Solution:
    def quicksort(self, nums):
        if len(nums)<=1:
            return nums
        pivot = random.choice(nums)
        left =[i for i in nums if i<pivot]
        right =[i for i in nums if i> pivot]
        middle=[i for i in nums if i==pivot]
        return self.quicksort(left)+middle+self.quicksort(right)

arr =[2,4,5,1,3,9,4,8,10,7,6]

sol =Solution()
print(sol.quicksort(arr))