class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)         # EX: [1,1,0...0] : [ab,ba] 

        for s in strs:                  # a,b,c,...z
            count = [0] * 26            # [0,0,0...]

            for ch in s:
                count[ord(ch) - ord('a')] += 1        # 80 - 80 = 0 -> index 0 will have value of 1
                
            
            res[tuple(count)].append(s)

        return list(res.values())
        