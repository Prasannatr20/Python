#680. Valid Palindrome II
#Given a string s, return true if the s can be palindrome after deleting at most one character from it.


class Solution:
    def palindrome(self, s):
        if len(s)==1:
            return True
        left =0
        right =len(s)-1
        count =0
        while(left<right):
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                left+=1
                right-=1
                count+=1
                if count>1: return False
                elif count>=1 and len(s)<4: return False
            return True
    

s = "tebbem"
sol = Solution()
print(sol.palindrome(s))