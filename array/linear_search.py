class Solution:
    def linear_search(self, nums, tar):

        for i in range(0, len(nums)):
            if(nums[i]==tar):
                return i
        return "Not present"

#instance variable


arr=[1,2,3,4,5,2,344,55,8]
target = 344
sol= Solution()

print(sol.linear_search(arr, target))