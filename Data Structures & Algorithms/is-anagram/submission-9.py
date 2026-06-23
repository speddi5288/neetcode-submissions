from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        char_frq_s, char_frq_t = defaultdict(int), defaultdict(int)

        for i in range(len(s)):
            char_frq_s[s[i]] += 1
            char_frq_t[t[i]] += 1
            
        if char_frq_s == char_frq_t:
            return True

        return False



        
        