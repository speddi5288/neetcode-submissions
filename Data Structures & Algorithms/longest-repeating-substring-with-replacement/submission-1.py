class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}  # hashmap for counting the freq of each char
        res = 0     # tells us the longest substring we can create w/ k replacements

        l = 0 

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)    # stores each char amt in counts maps

            while ((r-l) + 1 - max(count.values())) > k:      # if current winLen is NOT valid
                count[s[l]] -= 1              # decrement the count amt of leftmost char(removes)
                l += 1                              # increment left ptr since NOT valid(move)

            res = max(res, r-l+1)
        
        return res        