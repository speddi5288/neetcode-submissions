class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0              # Left pointer of the window
        longest = 0        # Result variable
        sett = set()       # Hash set to track characters in current window

        # Iterate right pointer 'r' across the string
        for r in range(len(s)):
            # If current char is already in set, shrink window from left
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            # Add the current character to the set
            sett.add(s[r])
            
            # Calculate current window size and update max length
            win = (r - l) + 1
            longest = max(longest, win)
        
        return longest