class Solution:
    def isPalindrome(self, s: str) -> bool:

        perfectString = ""

        for c in s:
            if c.isalnum():
                perfectString += c.lower()


        left = 0
        right = len(perfectString) - 1

        while left < right:
            if perfectString[left] != perfectString[right]:
                return False

            left += 1
            right -= 1
        return True

        
        


        