class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) <= 2:
            return True
        
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return self.isPalin(s, left + 1, right) or self.isPalin(s, left, right - 1)
            else:
                left += 1
                right -= 1

        return True

    def isPalin(self, string, left, right):

        while left < right:
            if string[left] != string[right]:
                return False
            else: 
                left += 1
                right -=1

        return True
