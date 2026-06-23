# Input: two strings s & t
# Output: True or False
# What is an anagram?
'''
both strings have exact same amount of chars and same chars but can be in diff orders
Ex:
racecar
carrace
Should store into a hashmap
 key, val
 char, #count of that char 

if the char hashmaps match then i will return true
else I will return false

How should i start the code?
I want to first go through ONE OF THE STRINGS
One thing i noticed -> if string lengths are not the same -> return False

Next i will iterate through the first string
for each index i will put the char of string: s into the map and string: t into map with its t index
once reached end of string do a check if to see if the two hashmaps are equal


'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):           # unever lens means cant be an anagram
            return False

        my_mapT = defaultdict(int)     # char, #count
        my_mapS = defaultdict(int)     # char, #count

        n = len(s)

        for i in range(n):
            my_mapS[s[i]] += 1     # j: 1, a: 1, r: 1
            my_mapT[t[i]] += 1     # j: 1, a: 1, m: 1
        
        if my_mapS != my_mapT:
            return False
    
        return True

    

        