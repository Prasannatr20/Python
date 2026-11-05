# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

class Solution:
    def maxArea(self, height):
        left =0
        right= len(height)-1
        res=-1
        while(left<right):
            min= right-left
            if height[left]<height[right]:
                if height[left]*min>res:
                    res=height[left]*min
                left+=1
            else:
                if height[right]*min>res:
                    res = height[right]*min
                right-=1
        return res


arr=[1,8,6,2,5,4,8,3,7]
sol = Solution()
print(sol.maxArea(arr))