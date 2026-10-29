class Solution:
    def bubble_sort(self, nums):
        for i in range(0, len(nums)-1):
            swap = False
            for j in range(0, len(nums)-i-1):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]= nums[j+1], nums[j]
                    swap = True
            if swap is False:
                return nums
        return nums


    # def bubble_sort(self, nums):
    #     a=0
    #     while(True):
    #         flag= False
    #         for i in range(len(nums)-a-1):
    #             if nums[i]>nums[i+1]:
    #                 nums[i], nums[i+1]= nums[i+1], nums[i]
    #                 flag = True
    #         a+=1
    #         if flag is False:
    #             return nums

arr=[1,26,2,11,32,34,2]

sol = Solution()
print(sol.bubble_sort(arr))