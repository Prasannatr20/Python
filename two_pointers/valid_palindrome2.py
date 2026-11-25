"""Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false"""

#Leetcode 680
class Solution:
    def validPalindrome(self, s):
        if len(s)<=1:
            return True
        left =0
        right =len(s)-1
        count=0
        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return self.removeChar(s,left+1,right) or self.removeChar(s, left, right-1)
        return True
    
    def removeChar(self, s, left, right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True

solver=Solution()
s="abbab"
print(solver.validPalindrome(s))