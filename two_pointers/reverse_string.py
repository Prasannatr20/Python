#Leetcode 344. Reverse String



class Solution:
    def reverse(self, s):
        if len(s)<=1:
            return s
        left = 0
        right = len(s)-1
        while(left<right):
            temp = s[left]
            s[left]= s[right]
            s[right]= temp
            left+=1
            right-=1
        return s


str=["H","a","n","n","a","h"]
#instance variable
solver = Solution()
print(solver.reverse(str))