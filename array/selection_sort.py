class Solution:
    def selection_sort(self, nums):
        for i in range(len(nums)-1):
            min =i
            for j in range(i+1, len(nums)):
                if nums[min]>nums[j]:
                    min=j
            if min!=i:
                nums[i], nums[min]= nums[min], nums[i]
        return nums
arr=[5,4,2,1,3]
solver = Solution()
print(solver.selection_sort(arr))