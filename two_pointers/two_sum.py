#Two sum in a sorted array


class Solution:
    def twosum(self, numbers,target):
        left = 0
        right = len(numbers)-1

        while(left<right):
            if numbers[left]+numbers[right]==target:
                return [left+1, right+1]
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1


arr=[2,3,4]
tar=6
solver = Solution()
result = solver.twosum(arr, tar)
print(result)