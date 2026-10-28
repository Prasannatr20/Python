class Solution:
    def binary_search(self, nums, tar):
        left = 0
        right = len(nums)-1

        while left<=right:
            middle=(left+right)//2
            if nums[middle]==tar:
                return middle
            elif nums[middle]>tar:
                right = middle-1
            else:
                left=middle+1
        return -1



arr=[1,2,3,4,5,6,7,8,9,10]
sol = Solution()
print(sol.binary_search(arr, 8))