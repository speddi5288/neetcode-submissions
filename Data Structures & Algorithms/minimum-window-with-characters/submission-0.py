class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "" : return ""      # edge case

        # countT -> t string counter (what you need)
        # window -> what you have so far in the curr window
        countT = defaultdict(int)
        window = defaultdict(int)

        # for char in string t, countT never changes so j set up its count amts
        for c in t:
            countT[c] += 1
        
        have = 0            # have -> (since we dont have the chars we need init)
        need = len(countT)  # need -> len of counterT (unique chars in string T)

        res = [-1,-1]   # l, r init at -1
        resLen = float('inf')   # can put any val less than infinity
        l = 0
        for r in range(len(s)):     # right ptr goes through string 's' & gets winLen
            c = s[r]            # store curr char in variable - c
            window[c] += 1      # inc the window map with char: num (key:val pairs)

            if c in countT and window[c] == countT[c]:      # if char in T and chars have same amt
                have += 1   # inc the have amt to be closer to need
            
            # does have equal need exactly?
            while have == need:
                # then update our res (new min res?)
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = (r-l+1)
                # pop from left of window to make it as small as possible
                window[s[l]] -= 1       # rem. leftmost char val
                # possible have != need so check s[l] is in T, & if the count amt is < need again
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l: r+1] if resLen != float('inf') else ""      
        