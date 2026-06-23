class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
        if ( len(s) != len(t) ):
            return False

        # Create counter for the values for each repeating char in the string
        counterS, counterT = {}, {}

        #Build the hashmap
        for i in range(len(s)):
            counterS [s[i]] = 1 + counterS.get( s[i], 0 )
            counterT [t[i]] = 1 + counterT.get( t[i], 0 )
        
        return counterS == counterT
            



