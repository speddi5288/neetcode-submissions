class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        mapS = {}
        mapT = {}

        for char in s:
            if char not in mapS:
                mapS[char] = 1
            elif char in mapS:
                mapS[char] += 1
        
        for char in t:
            if char not in mapT:
                mapT[char] = 1
            elif char in mapT:
                mapT[char] += 1
            

        if mapT == mapS:
            return True
        
        return False
        

            

        