#125. Valid Palindrome

class Solution:
    def palindrome(self, s):
        s=s.lower()
        left = 0
        right = len(s)-1

        while(left<=right):
            if left <= right and not (('a' <= s[left] <= 'z') or ('0' <= s[left] <= '9')):
                left+=1
            elif left<= right and not (('a' <= s[right] <= 'z' or ('0' <= s[right] <= '9'))):
                right-=1
            elif(s[left]==s[right]):
                left+=1
                right-=1
            else:
                return False

        return True

str = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.palindrome(str))