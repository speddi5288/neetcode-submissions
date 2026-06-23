from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        char_frq_s = defaultdict(int)
        char_frq_t = defaultdict(int)

        for ch in s:
            char_frq_s[ch] += 1
        for ch in t:
            char_frq_t[ch] += 1
        
        if char_frq_s == char_frq_t:
            return True

        return False



        
        