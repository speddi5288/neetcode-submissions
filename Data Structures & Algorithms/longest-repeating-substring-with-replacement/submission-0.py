class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}  # count the occurences of each character
        res = 0

        l = 0
        for r in range ( len(s) ):

            count[s[r]] = 1 + count.get( s[r], 0 ) # gets the freq of each char 
            # s[r] means go in str s and use index(r) to get the value at that index

            while (r-l+1) - max(count.values()) >  k:     # window length - the count of the most freq. character in the counts map
                count[s[l]] -= 1     # decrement left ptr if we have too many values/chars to replace
                l +=  1     # increment left ptr if we can't replace all the values to make a valid answer


            res = max(res, r-l+1)   # curr size vs overall win len size
        return res



        
        