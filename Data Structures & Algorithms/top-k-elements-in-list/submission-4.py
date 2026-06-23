from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        freq = [ [] for i in range(len(nums) + 1) ]

        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        
        for n, c in counter.items():
            freq[c].append(n)           # you are putting the values into freq list, not counter dict

        result = []
        for i in range(len(freq) - 1, 0, -1):

            for num in freq[i]:         # in order to access list in freq do freq[i], if you do regular freq then u will return all the lists not just the numbers
                result.append(num)

                if len(result) == k:
                    return result











        